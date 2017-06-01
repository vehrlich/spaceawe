# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import careers.models
import ckeditor.fields
import sorl.thumbnail.fields
import select_multiple_field.models


class Migration(migrations.Migration):

    dependencies = [
        ('activities', '0014_languageattachment_languageattachmenttranslation'),
        ('careers', '0003_interviewquestion_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='TeachingMaterial',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('featured', models.BooleanField(default=False)),
                ('published', models.BooleanField(default=True)),
                ('release_date', models.DateTimeField()),
                ('embargo_date', models.DateTimeField(blank=True, null=True)),
                ('space', models.BooleanField(default=False)),
                ('earth', models.BooleanField(default=False)),
                ('navigation', models.BooleanField(default=False)),
                ('heritage', models.BooleanField(default=False)),
                ('cover', sorl.thumbnail.fields.ImageField(upload_to='careers/teaching-materials/covers', blank=True, null=True)),
                ('learning', models.CharField(max_length=2, verbose_name='type of learning activity', choices=[('g', 'Game'), ('l', 'Lesson plan')])),
                ('_languages', select_multiple_field.models.SelectMultipleField(db_column='languages', max_length=9999, choices=[('af', 'Afrikaans'), ('ar', 'Arabic'), ('ast', 'Asturian'), ('az', 'Azerbaijani'), ('bg', 'Bulgarian'), ('be', 'Belarusian'), ('bn', 'Bengali'), ('br', 'Breton'), ('bs', 'Bosnian'), ('ca', 'Catalan'), ('cs', 'Czech'), ('cy', 'Welsh'), ('da', 'Danish'), ('de', 'German'), ('el', 'Greek'), ('en', 'English'), ('en-au', 'Australian English'), ('en-gb', 'British English'), ('eo', 'Esperanto'), ('es', 'Spanish'), ('es-ar', 'Argentinian Spanish'), ('es-mx', 'Mexican Spanish'), ('es-ni', 'Nicaraguan Spanish'), ('es-ve', 'Venezuelan Spanish'), ('et', 'Estonian'), ('eu', 'Basque'), ('fa', 'Persian'), ('fi', 'Finnish'), ('fr', 'French'), ('fy', 'Frisian'), ('ga', 'Irish'), ('gl', 'Galician'), ('he', 'Hebrew'), ('hi', 'Hindi'), ('hr', 'Croatian'), ('hu', 'Hungarian'), ('ia', 'Interlingua'), ('id', 'Indonesian'), ('io', 'Ido'), ('is', 'Icelandic'), ('it', 'Italian'), ('ja', 'Japanese'), ('ka', 'Georgian'), ('kk', 'Kazakh'), ('km', 'Khmer'), ('kn', 'Kannada'), ('ko', 'Korean'), ('lb', 'Luxembourgish'), ('lt', 'Lithuanian'), ('lv', 'Latvian'), ('mk', 'Macedonian'), ('ml', 'Malayalam'), ('mn', 'Mongolian'), ('mr', 'Marathi'), ('my', 'Burmese'), ('nb', 'Norwegian Bokmal'), ('ne', 'Nepali'), ('nl', 'Dutch'), ('nn', 'Norwegian Nynorsk'), ('os', 'Ossetic'), ('pa', 'Punjabi'), ('pl', 'Polish'), ('pt', 'Portuguese'), ('pt-br', 'Brazilian Portuguese'), ('ro', 'Romanian'), ('ru', 'Russian'), ('sk', 'Slovak'), ('sl', 'Slovenian'), ('sq', 'Albanian'), ('sr', 'Serbian'), ('sr-latn', 'Serbian Latin'), ('sv', 'Swedish'), ('sw', 'Swahili'), ('ta', 'Tamil'), ('te', 'Telugu'), ('th', 'Thai'), ('tr', 'Turkish'), ('tt', 'Tatar'), ('udm', 'Udmurt'), ('uk', 'Ukrainian'), ('ur', 'Urdu'), ('vi', 'Vietnamese'), ('zh-cn', 'Simplified Chinese'), ('zh-hans', 'Simplified Chinese'), ('zh-hant', 'Traditional Chinese'), ('zh-tw', 'Traditional Chinese')])),
                ('age', models.ManyToManyField(related_name='_teachingmaterial_age_+', to='activities.MetadataOption')),
            ],
            options={
                'ordering': ['release_date'],
            },
        ),
        migrations.CreateModel(
            name='TeachingMaterialAttachment',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('title', models.CharField(max_length=255, blank=True)),
                ('show', models.BooleanField(default=False, verbose_name='Show', help_text='Include in attachment list.')),
                ('position', models.PositiveSmallIntegerField(default=0, verbose_name='Position', help_text='Used to define the order of attachments in the attachment list.')),
                ('file', models.FileField(upload_to=careers.models.get_file_path_step, blank=True, null=True)),
                ('hostmodel', models.ForeignKey(to='careers.TeachingMaterial', related_name='attachments')),
            ],
            options={
                'ordering': ['position', 'id'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TeachingMaterialTranslation',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('language_code', models.CharField(max_length=15, verbose_name='Language', db_index=True)),
                ('title', models.CharField(max_length=255, blank=True)),
                ('slug', models.SlugField(max_length=255, blank=True)),
                ('story', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('language', models.CharField(max_length=255, blank=True)),
                ('master', models.ForeignKey(related_name='translations', to='careers.TeachingMaterial', null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='careertranslation',
            name='interview',
        ),
        migrations.AddField(
            model_name='interview',
            name='career',
            field=models.ManyToManyField(to='careers.Career'),
        ),
        migrations.AlterUniqueTogether(
            name='teachingmaterialtranslation',
            unique_together=set([('language_code', 'title'), ('language_code', 'master'), ('language_code', 'slug')]),
        ),
    ]
