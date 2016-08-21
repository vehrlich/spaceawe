# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('develop', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='mooc',
            name='position',
            field=models.IntegerField(default=True),
        ),
    ]
