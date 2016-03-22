# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models

from parler.utils.context import switch_language


def copy_en_fields(apps, schema_editor):
    Game = apps.get_model("games", "Game")
    GameTranslation = apps.get_model("games", "GameTranslation")
    for game in Game.objects.all():
        game_t = GameTranslation.objects.get(master=game, language_code='en')
        game_t.slug = game.slug
        game_t.title = game.title
        game_t.teaser = game.teaser
        game_t.save()


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0005_auto_20160204_0713'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='game',
            options={'ordering': ['release_date']},
        ),


        migrations.AddField(
            model_name='gametranslation',
            name='slug',
            field=models.SlugField(max_length=255, blank=True, help_text='The Slug must be unique, and closely match the title for better SEO; it is used as part of the URL.'),
        ),
        migrations.AddField(
            model_name='gametranslation',
            name='title',
            field=models.CharField(max_length=255, blank=True, help_text='Short (and commonly used) name'),
        ),
        migrations.AddField(
            model_name='gametranslation',
            name='teaser',
            field=models.CharField(max_length=255, blank=True),
        ),

        migrations.RunPython(copy_en_fields),




    ]
