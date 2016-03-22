# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0002_auto_20160125_0639'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='earth',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='game',
            name='heritage',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='game',
            name='navigation',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='game',
            name='space',
            field=models.BooleanField(default=False),
        ),
    ]
