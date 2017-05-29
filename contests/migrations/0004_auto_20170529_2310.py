# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import contests.models


class Migration(migrations.Migration):

    dependencies = [
        ('contests', '0003_auto_20170525_2337'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attachment',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('title', models.CharField(max_length=255, blank=True)),
                ('file', models.FileField(upload_to=contests.models.get_file_path_step, blank=True)),
                ('main_visual', models.BooleanField(default=False, help_text='The main visual is used as the cover image.')),
                ('show', models.BooleanField(verbose_name='Show', default=False, help_text='Include in attachment list.')),
                ('position', models.PositiveSmallIntegerField(verbose_name='Position', default=0, help_text='Used to define the order of attachments in the attachment list.')),
            ],
            options={
                'ordering': ['-show', 'position', 'id'],
            },
        ),
        migrations.RemoveField(
            model_name='contest',
            name='cover',
        ),
        migrations.RemoveField(
            model_name='contestsection',
            name='section_image',
        ),
        migrations.AddField(
            model_name='attachment',
            name='hostmodel',
            field=models.ForeignKey(to='contests.Contest'),
        ),
    ]
