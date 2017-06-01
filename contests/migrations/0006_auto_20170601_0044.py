# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contests', '0005_auto_20170601_0032'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='attachment',
            options={'ordering': ['id']},
        ),
        migrations.RemoveField(
            model_name='attachment',
            name='position',
        ),
        migrations.RemoveField(
            model_name='attachment',
            name='show',
        ),
    ]
