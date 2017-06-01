from django.contrib import admin
from django import forms
from parler.admin import TranslatableAdmin, TranslatableModelForm,TranslatableStackedInline


from .models import Contest, ContestSection, Attachment


class ContestSectionInlineAdmin(TranslatableStackedInline ):
    model = ContestSection
    fields = ('title', 'slug', 'position', 'collapse', 'content')
    extra = 1

    def get_prepopulated_fields(self, request, obj=None):
        # can't use `prepopulated_fields = ..` because it breaks the admin validation
        # for translated fields. This is the official django-parler workaround.
        return {
            'slug': ('title',),
        }

    class Meta:
        widgets = {'content': forms.TextInput(attrs={'class': 'vTextField'}),}


class AttachmentInlineFormset(forms.models.BaseInlineFormSet):
    def clean(self):
        if any(self.errors):
            # Don't bother validating the formset unless each form is valid on its own
            return

        # There can be only one "main visual"
        main_visual_count = 0
        for form in self.forms:
            if form.cleaned_data:
                main_visual = form.cleaned_data['main_visual']
                if main_visual:
                    main_visual_count += 1

        if main_visual_count > 1:
            raise forms.ValidationError('There can be only one "main visual".')


class AttachmentInlineForm(admin.TabularInline):
    model = Attachment
    formset = AttachmentInlineFormset
    fields = ('title', 'file', 'main_visual')


class ContestAdminForm(TranslatableModelForm):

    class Meta:
        model = Contest
        fields = ('title', 'slug', 'release_date', 'published', 'featured', 'teaser')


@admin.register(Contest)
class ContestAdmin(TranslatableAdmin):
    list_display = ('title', 'all_languages_column', )
    form = ContestAdminForm

    # prepopulated_fields = {'slug': ('title', ), }
    def get_prepopulated_fields(self, request, obj=None):
        # can't use `prepopulated_fields = ..` because it breaks the admin validation
        # for translated fields. This is the official django-parler workaround.
        return {
            'slug': ('title',),
        }

    inlines = (
        ContestSectionInlineAdmin, AttachmentInlineForm
    )
