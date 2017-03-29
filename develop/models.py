from django.db import models
from parler.models import TranslatableModel,TranslatedFieldsModel
from ckeditor.fields import RichTextField
from sorl.thumbnail import ImageField


class Mooc(models.Model):
    info = models.CharField(max_length=255)
    starting_date = models.CharField(max_length=255)
    is_active = models.BooleanField(default=False)
    enroll_url = models.URLField(blank=True)

    position = models.IntegerField(default=True)

    # description
    introduction = models.TextField()
    what_you_will_learn = models.TextField()
    what_skills_will_you_need = models.TextField()
    duration_of_the_course = models.TextField()

    def __str__(self, **kwargs):
        return self.info


class Module(models.Model):
    mooc = models.ForeignKey(Mooc)
    info = models.CharField(max_length=255)
    duration = models.CharField(max_length=255)

    def __str__(self, **kwargs):
        return self.info

    def info_parts(self, **kwargs):
        return self.info.split(': ')


class SupportDocument(TranslatableModel):
    """
    Support material document is represent with title, short disclaimer, download file
    """
    mooc = models.ForeignKey(Mooc)

    def __str__(self):
        return self.title


class SupportDocumentTranslation(TranslatedFieldsModel):
    master = models.ForeignKey(SupportDocument, related_name='translations', null=True)
    title = models.CharField(max_length=255)
    disclaimer = models.TextField(max_length=255)
    document_file = models.FileField(upload_to='support_document')
    duration = models.CharField(max_length=255)

    class Meta:
        unique_together = (
            ('language_code', 'master'),
        )

# same as activity metadata
ASSESSMENT_METADATA = (
    ('type', 'Type',
        {'display': 'assessment_type', }),
    ('format', 'Format',
        {'multiple': True, }),
    ('timing', 'Timing',
        {'multiple': True, }),
    ('focus', 'Focus',
        {'multiple': True,}),
)

METADATA_OPTION_CHOICES = [(x[0], x[1]) for x in ASSESSMENT_METADATA]


class AssessmentMetadataOption(TranslatableModel):
    group = models.CharField(max_length=50, blank=False, choices=METADATA_OPTION_CHOICES)
    code = models.CharField(max_length=50, blank=False)
    position = models.PositiveSmallIntegerField(default=0)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['group', 'position']
        unique_together = (('group', 'code'),)


class AssessmentMetadataOptionTransition(TranslatedFieldsModel):
    master = models.ForeignKey(AssessmentMetadataOption, related_name='translations', null=True)
    title = models.CharField(max_length=255, blank=False)

    def __str__(self):
        return self.title


class AssessmentMetadataOptionsManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().order_by('position')


class AssessmentTool(TranslatableModel):
    cover = ImageField(null=True, blank=True, upload_to='develop/assessment-tools/covers')
    assessment_type = models.ForeignKey(AssessmentMetadataOption, limit_choices_to={'group':'type'})
    format = models.ManyToManyField(AssessmentMetadataOption, limit_choices_to={'group': 'format'},
                                    related_name='format')
    timing = models.ManyToManyField(AssessmentMetadataOption, limit_choices_to={'group': 'timing'},
                                    related_name='timing')
    focus = models.ManyToManyField(AssessmentMetadataOption, limit_choices_to={'group': 'focus'},
                                   related_name='focus')

    def __str__(self):
        return self.title

    def assessment_format(self):
        return [obj.title for obj in self.format.all()]

    def assessment_timing(self):
        return [obj.title for obj in self.timing.all()]

    def assessment_focus(self):
        return [obj.title for obj in self.focus.all()]


class AssessmentToolTranslation(TranslatedFieldsModel):
    master = models.ForeignKey(AssessmentTool, related_name='translations', null=True)
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    disclaimer = models.CharField(max_length=255)
    story = RichTextField(blank=True, null=True, config_name='smartpages')

    class Meta:
        unique_together = (
            ('language_code', 'master'),
            ('language_code', 'slug'),
        )
