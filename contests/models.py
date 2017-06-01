import os

from django.db import models
from parler.models import TranslatableModel, TranslatedFieldsModel
from parler.managers import TranslatableManager, TranslatableQuerySet
from ckeditor.fields import RichTextField
from django_ext.models import PublishingModel, PublishingManager


def get_file_path_step(instance, filename):
    return os.path.join('contests/attach', str(instance.hostmodel.id), filename)


class ContestQuerySet(TranslatableQuerySet):
    pass


class ContestManager(PublishingManager, TranslatableManager):
    queryset_class = ContestQuerySet


class Contest(TranslatableModel, PublishingModel):

    objects = ContestManager()

    @property
    def main_visual(self):
        result = None
        images = self.attachment_set.filter(main_visual=True)
        if images:
            result = images[0].file
        return result


class ContestTranslation(TranslatedFieldsModel):
    master = models.ForeignKey(Contest, related_name='translations', null=True)
    title = models.CharField(blank=False, max_length=255, help_text='Short (and commonly used) name', )
    slug = models.SlugField(blank=False, max_length=255, help_text='The Slug must be unique, and closely match the title for better SEO; it is used as part of the URL.', )
    teaser = models.TextField(max_length=255, blank=True, )

    class Meta:
        unique_together = (
            ('language_code', 'master'),
            ('language_code', 'title'),
            ('language_code', 'slug'),
        )


class ContestSection(TranslatableModel):
    contest = models.ForeignKey(Contest, related_name='contest_sections', blank=False, null=True)
    position = models.PositiveSmallIntegerField(default=0, verbose_name='Position',
                                                help_text='Used to define the order of section.')

    class Meta:
        ordering = ['position', 'id']


class ContestSectionTranslation(TranslatedFieldsModel):
    master = models.ForeignKey(ContestSection, related_name='translations', null=True)
    title = models.CharField(blank=False, max_length=255, help_text='Short (and commonly used) name', )
    slug = models.SlugField(blank=False, max_length=255, help_text='The Slug must be unique, and closely match the title for better SEO; it is used as part of the URL.', )
    content = RichTextField(blank=True, null=True, config_name='smartpages')

    class Meta:
        unique_together = (
            ('language_code', 'master'),
            ('language_code', 'title'),
            ('language_code', 'slug'),
        )


class Attachment(models.Model):
    title = models.CharField(max_length=255, blank=True)
    file = models.FileField(blank=True, upload_to=get_file_path_step)
    main_visual = models.BooleanField(default=False, help_text='The main visual is used as the cover image.')
    hostmodel = models.ForeignKey(Contest)


    class Meta:
        ordering = ['id']