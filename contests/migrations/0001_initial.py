# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import sorl.thumbnail.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contest',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('featured', models.BooleanField(default=False)),
                ('published', models.BooleanField(default=True)),
                ('release_date', models.DateTimeField()),
                ('embargo_date', models.DateTimeField(null=True, blank=True)),
                ('cover', sorl.thumbnail.fields.ImageField(null=True, blank=True, upload_to='contests')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ContestSection',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('section_image', sorl.thumbnail.fields.ImageField(null=True, blank=True, upload_to='contest_section')),
                ('contest', models.ForeignKey(null=True, to='contests.Contest', related_name='contest_sections')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ContestSectionTranslation',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('language_code', models.CharField(max_length=15, db_index=True, verbose_name='Language')),
                ('title', models.CharField(max_length=255, help_text='Short (and commonly used) name')),
                ('slug', models.SlugField(max_length=255, help_text='The Slug must be unique, and closely match the title for better SEO; it is used as part of the URL.')),
                ('content', models.CharField(max_length=255, blank=True)),
                ('master', models.ForeignKey(null=True, to='contests.ContestSection', related_name='translations')),
            ],
        ),
        migrations.CreateModel(
            name='ContestTranslation',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('language_code', models.CharField(max_length=15, db_index=True, verbose_name='Language')),
                ('title', models.CharField(max_length=255, help_text='Short (and commonly used) name')),
                ('slug', models.SlugField(max_length=255, help_text='The Slug must be unique, and closely match the title for better SEO; it is used as part of the URL.')),
                ('teaser', models.CharField(max_length=255, blank=True)),
                ('master', models.ForeignKey(null=True, to='contests.Contest', related_name='translations')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='contesttranslation',
            unique_together=set([('language_code', 'title'), ('language_code', 'master'), ('language_code', 'slug')]),
        ),
        migrations.AlterUniqueTogether(
            name='contestsectiontranslation',
            unique_together=set([('language_code', 'title'), ('language_code', 'master'), ('language_code', 'slug')]),
        ),
    ]
