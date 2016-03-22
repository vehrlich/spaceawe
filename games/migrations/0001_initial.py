# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import ckeditor.fields
import sorl.thumbnail.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('featured', models.BooleanField(default=False)),
                ('published', models.BooleanField(default=True)),
                ('release_date', models.DateTimeField()),
                ('embargo_date', models.DateTimeField(blank=True, null=True)),
                ('name', models.CharField(help_text='Short (and commonly used) name', unique=True, max_length=255)),
                ('slug', models.SlugField(help_text='The Slug must be unique, and closely match the title for better SEO; it is used as part of the URL.', unique=True, max_length=255)),
                ('teaser', models.CharField(blank=True, max_length=255)),
                ('url', models.URLField(blank=True, max_length=255, null=True)),
                ('difficulty', models.IntegerField(help_text='From 1 to 5.', default=0)),
                ('fun', models.IntegerField(help_text='From 1 to 5.', default=0)),
                ('cover', sorl.thumbnail.fields.ImageField(upload_to='games', blank=True, null=True)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='GameTranslation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language_code', models.CharField(max_length=15, verbose_name='Language', db_index=True)),
                ('description', ckeditor.fields.RichTextField(blank=True, help_text='Text to appear in Game page', null=True)),
                ('master', models.ForeignKey(related_name='translations', null=True, to='games.Game')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='gametranslation',
            unique_together=set([('language_code', 'master')]),
        ),
    ]
