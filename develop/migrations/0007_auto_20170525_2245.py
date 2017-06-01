# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import ckeditor.fields
import sorl.thumbnail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('develop', '0006_auto_20170125_0017'),
    ]

    operations = [
        migrations.CreateModel(
            name='AssessmentMetadataOption',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('group', models.CharField(max_length=50, choices=[('type', 'Type'), ('format', 'Format'), ('timing', 'Timing'), ('focus', 'Focus')])),
                ('code', models.CharField(max_length=50)),
                ('position', models.PositiveSmallIntegerField(default=0)),
            ],
            options={
                'ordering': ['group', 'position'],
            },
        ),
        migrations.CreateModel(
            name='AssessmentMetadataOptionTransition',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('language_code', models.CharField(max_length=15, verbose_name='Language', db_index=True)),
                ('title', models.CharField(max_length=255)),
                ('master', models.ForeignKey(related_name='translations', to='develop.AssessmentMetadataOption', null=True)),
            ],
            options={
                'default_permissions': (),
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='AssessmentTool',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('cover', sorl.thumbnail.fields.ImageField(upload_to='develop/assessment-tools/covers', blank=True, null=True)),
                ('assessment_type', models.ForeignKey(to='develop.AssessmentMetadataOption')),
                ('focus', models.ManyToManyField(related_name='focus', to='develop.AssessmentMetadataOption')),
                ('format', models.ManyToManyField(related_name='format', to='develop.AssessmentMetadataOption')),
                ('timing', models.ManyToManyField(related_name='timing', to='develop.AssessmentMetadataOption')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='AssessmentToolTranslation',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('language_code', models.CharField(max_length=15, verbose_name='Language', db_index=True)),
                ('title', models.CharField(max_length=255)),
                ('slug', models.SlugField(max_length=255)),
                ('disclaimer', models.CharField(max_length=255)),
                ('story', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('master', models.ForeignKey(related_name='translations', to='develop.AssessmentTool', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='SupportDocument',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('mooc', models.ForeignKey(to='develop.Mooc')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SupportDocumentTranslation',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('language_code', models.CharField(max_length=15, verbose_name='Language', db_index=True)),
                ('title', models.CharField(max_length=255)),
                ('disclaimer', models.TextField(max_length=255)),
                ('document_file', models.FileField(upload_to='support_document')),
                ('duration', models.CharField(max_length=255)),
                ('master', models.ForeignKey(related_name='translations', to='develop.SupportDocument', null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='SupportMaterial',
        ),
        migrations.AlterUniqueTogether(
            name='assessmentmetadataoption',
            unique_together=set([('group', 'code')]),
        ),
        migrations.AlterUniqueTogether(
            name='supportdocumenttranslation',
            unique_together=set([('language_code', 'master')]),
        ),
        migrations.AlterUniqueTogether(
            name='assessmenttooltranslation',
            unique_together=set([('language_code', 'master'), ('language_code', 'slug')]),
        ),
    ]
