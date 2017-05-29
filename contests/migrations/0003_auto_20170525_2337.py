# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contests', '0002_auto_20170525_2336'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contesttranslation',
            name='teaser',
            field=models.TextField(blank=True, max_length=255),
        ),
    ]
