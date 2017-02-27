from django.contrib import admin
from django import forms
from parler.admin import TranslatableAdmin
from parler.forms import TranslatableModelForm
from sorl.thumbnail.admin import AdminImageMixin


from .models import Article, Highlight


@admin.register(Article)
class ArticleAdmin(AdminImageMixin, TranslatableAdmin):
    # list_display = ('title', 'all_languages_column', 'thumb', )
    list_display = ('title', 'all_languages_column', )

    fieldsets = (
        (None,
            {'fields': ('title', 'slug', 'teaser', 'cover', ), }),
        ('Publishing',
            {'fields': (('release_date', ),
                        ('published', 'featured', ),), }),
        (None,
            {'fields': ('story', ), }),
        ('Event fields',
            {'fields': ('event_organiser', '_event_language', 'event_download_url', 'event_website_url', ), }),
    )

    # prepopulated_fields = {'slug': ('title', ), }
    def get_prepopulated_fields(self, request, obj=None):
        # can't use `prepopulated_fields = ..` because it breaks the admin validation
        # for translated fields. This is the official django-parler workaround.
        return {
            'slug': ('title', ),
        }


@admin.register(Highlight)
class HighlightAdmin(admin.ModelAdmin):
    raw_id_fields = ('news', 'scoop', 'game', 'activity', 'career', 'interview')
