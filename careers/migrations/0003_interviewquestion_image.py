# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import sorl.thumbnail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('careers', '0002_auto_20160616_0746'),
    ]

    operations = [
        migrations.AddField(
            model_name='interviewquestion',
            name='image',
            field=sorl.thumbnail.fields.ImageField(blank=True, null=True, upload_to='interviews'),
        ),
    ]
