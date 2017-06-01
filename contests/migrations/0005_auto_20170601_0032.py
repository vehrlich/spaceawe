# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contests', '0004_auto_20170529_2310'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contestsection',
            options={'ordering': ['position', 'id']},
        ),
        migrations.AddField(
            model_name='contestsection',
            name='position',
            field=models.PositiveSmallIntegerField(help_text='Used to define the order of section.', verbose_name='Position', default=0),
        ),
    ]
