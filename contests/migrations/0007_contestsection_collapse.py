# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contests', '0006_auto_20170601_0044'),
    ]

    operations = [
        migrations.AddField(
            model_name='contestsection',
            name='collapse',
            field=models.BooleanField(default=False, help_text='Collapse this section'),
        ),
    ]
