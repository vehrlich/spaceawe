from django.db import models
from django.core.urlresolvers import reverse
from django.conf import global_settings
from django.utils.translation import get_language_info
from ckeditor.fields import RichTextField
from sorl.thumbnail import ImageField
from sorl.thumbnail import get_thumbnail
from parler.models import TranslatableModel, TranslatedFieldsModel
from parler.managers import TranslatableManager, TranslatableQuerySet

from django_ext.models import PublishingModel, PublishingManager
from search.mixins import SearchModel
from institutions.models import Institution


class ArticleQuerySet(TranslatableQuerySet):
    pass


class ArticleManager(PublishingManager, TranslatableManager):
    queryset_class = ArticleQuerySet


class Article(TranslatableModel, PublishingModel, SearchModel):
    cover = ImageField(null=True, blank=True, upload_to='news')
    event_organiser = models.ForeignKey(Institution, blank=True, null=True)
    _event_language = models.CharField(blank=True, null=True, max_length=10, choices=global_settings.LANGUAGES, db_column='event_language', verbose_name='event language')
    event_download_url = models.URLField(blank=True, null=True, max_length=255, help_text='Link to downloadable file, e.g. event programme')
    event_website_url = models.URLField(blank=True, null=True, max_length=255, )

    @property
    def event_language(self):
        li = get_language_info(self._event_language)
        return li['name']  # , li['name_local'], li['bidi'])

    @event_language.setter
    def event_language(self, value):
        self._event_language = value

    objects = ArticleManager()

    @property
    def main_visual(self):
        return self.cover.file if self.cover else None

    def thumb(self):
        return u'<img src="%s" />' % (get_thumbnail(self.main_visual, 'x50', crop='center', quality=95).url)
    thumb.short_description = 'Main visual'
    thumb.allow_tags = True

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('news:detail', kwargs={'slug': self.slug, })

    class Meta:
        ordering = ['-release_date']
        verbose_name = 'news item'


class ArticleTranslation(TranslatedFieldsModel):
    master = models.ForeignKey(Article, related_name='translations', null=True)
    title = models.CharField(unique=True, blank=False, max_length=255, help_text='Short (and commonly used) name', )
    slug = models.SlugField(unique=True, blank=False, max_length=255, help_text='The Slug must be unique, and closely match the title for better SEO; it is used as part of the URL.', )
    teaser = models.CharField(max_length=255, blank=True, )
    story = RichTextField(blank=True, null=True, config_name='default', help_text='Text to appear in Article page')

    class Meta:
        unique_together = (
            ('language_code', 'master'),
            ('language_code', 'slug'),
        )


class Highlight(models.Model):
    from spacescoops.models import Article as Scoop
    from activities.models import Activity
    from games.models import Game

    news = models.ForeignKey(Article, blank=True, null=True)
    scoop = models.ForeignKey(Scoop, blank=True, null=True)
    game = models.ForeignKey(Game, blank=True, null=True)
    activity = models.ForeignKey(Activity, blank=True, null=True)

    @property
    def item(self):
        result = None
        if self.news:
            result = self.news
        elif self.scoop:
            result = self.scoop
        elif self.game:
            result = self.game
        elif self.activity:
            result = self.activity
        return result

    # @property
    # def title(self):
    #     return self.item.title if self.item else ''

    # @property
    # def teaser(self):
    #     return self.item.teaser if self.item and self.item.has_attr(teaser) else ''

    def __str__(self):
        if self.item:
            result = ":".join([self.item._meta.verbose_name, self.item.title])
        else:
            result = 'Undefined highlight'
        return result
        # if self.news:
        #     result = 'News: ' + self.news.title
        # elif self.scoop:
        #     result = 'Space Scoop: ' + self.scoop.title
        # elif self.game:
        #     result = 'Game: ' + self.game.title
        # elif self.activity:
        #     result = 'Activity: ' + self.activity.title
