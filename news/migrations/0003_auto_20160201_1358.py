# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('institutions', '0001_initial'),
        ('news', '0002_highlights'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'ordering': ['-release_date'], 'verbose_name': 'news item'},
        ),
        migrations.AddField(
            model_name='articletranslation',
            name='event_download_url',
            field=models.URLField(max_length=255, help_text='Link to downloadable file, e.g. event programme', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='articletranslation',
            name='event_organiser',
            field=models.ForeignKey(to='institutions.Institution', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='articletranslation',
            name='event_website_url',
            field=models.URLField(max_length=255, null=True, blank=True),
        ),
    ]
