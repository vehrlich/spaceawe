# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0006_new_translated_fields'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='game',
            name='slug',
        ),
        migrations.RemoveField(
            model_name='game',
            name='teaser',
        ),
        migrations.RemoveField(
            model_name='game',
            name='title',
        ),
        migrations.AlterField(
            model_name='gametranslation',
            name='slug',
            field=models.SlugField(max_length=255, help_text='The Slug must be unique, and closely match the title for better SEO; it is used as part of the URL.'),
        ),
        migrations.AlterField(
            model_name='gametranslation',
            name='title',
            field=models.CharField(max_length=255, help_text='Short (and commonly used) name'),
        ),
        migrations.AlterUniqueTogether(
            name='gametranslation',
            unique_together=set([('language_code', 'slug'), ('language_code', 'title'), ('language_code', 'master')]),
        ),
    ]
