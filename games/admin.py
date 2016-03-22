from django.contrib import admin
from django import forms
from parler.admin import TranslatableAdmin, TranslatableModelForm


from .models import Game, GameLink


class GameLinkInlineAdmin(admin.TabularInline):
    model = GameLink
    fields = ('name', 'url', )
    extra = 1


class GameAdminForm(TranslatableModelForm):

    class Meta:
        model = Game
        fields = ('title', 'slug', 'release_date', 'published', 'featured', 'cover', 'teaser', 'story', '_game_type', '_languages', '_platform', 'difficulty', 'fun', 'space', 'earth', 'navigation', 'heritage', )
        widgets = {
            'game_type': forms.CheckboxSelectMultiple,
        }


@admin.register(Game)
class GameAdmin(TranslatableAdmin):
    list_display = ('title', 'all_languages_column', )
    # list_display = ('title', ), 'all_languages_column', )

    fieldsets = (
        (None,
            {'fields': ('title', 'slug', 'teaser', 'cover', ), }),
        ('Space Awareness Category',
            {'fields': (('space', 'earth', 'navigation', 'heritage', ), ), }),
        (None,
            {'fields': (('_game_type', '_languages', '_platform', ),
                        ('difficulty', 'fun', ),), }),
        ('Publishing',
            {'fields': (('release_date', ),
                        ('published', 'featured', ),), }),
        (None,
            {'fields': ('story', ), }),
    )

    # prepopulated_fields = {'slug': ('title', ), }
    def get_prepopulated_fields(self, request, obj=None):
        # can't use `prepopulated_fields = ..` because it breaks the admin validation
        # for translated fields. This is the official django-parler workaround.
        return {
            'slug': ('title',),
        }

    inlines = (
        GameLinkInlineAdmin,
    )
