from django.contrib import admin
from parler.admin import TranslatableAdmin,TranslatableTabularInline
from parler.forms import TranslatableModelForm
from develop.models import Mooc, Module, SupportDocument, AssessmentMetadataOption, AssessmentTool


class ModuleInline(admin.TabularInline):
    model = Module
    extra = 0


class SupportDocumentInline(TranslatableTabularInline):
    model = SupportDocument
    fields = ('title', 'disclaimer', 'duration', 'document_file')
    extra = 0


class MoocAdmin(admin.ModelAdmin):

    inlines = [
        ModuleInline,
        SupportDocumentInline,
    ]


class ModuleAdmin(admin.ModelAdmin):
    pass

class SupportDocumentAdminForm(TranslatableModelForm):
    class Meta:
        model = SupportDocument
        fields = ('mooc', 'title', 'disclaimer', 'duration', 'document_file')


@admin.register(SupportDocument)
class SupportDocumentAdmin(TranslatableAdmin):
    list_display = ('title', 'all_languages_column')
    form = SupportDocumentAdminForm


class AssessmentMetadataOptionAdminForm(TranslatableModelForm):
    class Meta:
        model = AssessmentMetadataOption
        fields = ('title', 'code', 'group', 'position',)


@admin.register(AssessmentMetadataOption)
class AssessmentMetadataOptionAdmin(TranslatableAdmin):
    # model = AssessmentMetadataOption
    list_display = ('code', 'title', 'all_languages_column', 'group', 'position', )
    list_filter = ('group',)
    form = AssessmentMetadataOptionAdminForm


class AssessmentToolForm(TranslatableModelForm):
    class Meta:
        model = AssessmentTool
        fields = ('title', 'slug', 'cover', 'disclaimer', 'story', 'assessment_type', 'format', 'timing', 'focus',)


@admin.register(AssessmentTool)
class AssessmentToolAdmin(TranslatableAdmin):
    form = AssessmentToolForm

    def get_prepopulated_fields(self, request, obj=None):
        return {
            'slug': ('title',),
        }


admin.site.register(Mooc, MoocAdmin)
admin.site.register(Module, ModuleAdmin)
# admin.site.register(DidacticCourse, DidacticCourseAdmin)
# admin.site.register(DidacticCourseDisclaimer, DidacticCourseDisclaimerAdmin)


