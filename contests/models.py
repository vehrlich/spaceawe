import os

from django.db import models
from parler.models import TranslatableModel, TranslatedFieldsModel
from ckeditor.fields import RichTextField
from django_ext.models import PublishingModel


def get_file_path_step(instance, filename):
    return os.path.join('contests/attach', str(instance.hostmodel.id), filename)


class Contest(TranslatableModel, PublishingModel):

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
    show = models.BooleanField(default=False, verbose_name='Show', help_text='Include in attachment list.')
    position = models.PositiveSmallIntegerField(default=0, verbose_name='Position', help_text='Used to define the order of attachments in the attachment list.')
    hostmodel = models.ForeignKey(Contest)

    def display_name(self):
        if self.title:
            return self.title
        else:
            return os.path.basename(self.file.name)

    def __str__(self):
        return self.display_name()

    class Meta:
        ordering = ['-show', 'position', 'id']