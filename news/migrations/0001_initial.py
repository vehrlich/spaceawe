# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import sorl.thumbnail.fields
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('featured', models.BooleanField(default=False)),
                ('published', models.BooleanField(default=True)),
                ('release_date', models.DateTimeField()),
                ('embargo_date', models.DateTimeField(blank=True, null=True)),
                ('cover', sorl.thumbnail.fields.ImageField(blank=True, null=True, upload_to='news')),
            ],
            options={
                'ordering': ['-release_date'],
            },
        ),
        migrations.CreateModel(
            name='ArticleTranslation',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('language_code', models.CharField(verbose_name='Language', max_length=15, db_index=True)),
                ('title', models.CharField(help_text='Short (and commonly used) name', max_length=255, unique=True)),
                ('slug', models.SlugField(help_text='The Slug must be unique, and closely match the title for better SEO; it is used as part of the URL.', max_length=255, unique=True)),
                ('teaser', models.CharField(blank=True, max_length=255)),
                ('story', ckeditor.fields.RichTextField(help_text='Text to appear in Article page', blank=True, null=True)),
                ('master', models.ForeignKey(to='news.Article', related_name='translations', null=True)),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='articletranslation',
            unique_together=set([('language_code', 'slug'), ('language_code', 'master')]),
        ),
    ]
