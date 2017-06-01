# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('careers', '0004_auto_20170525_2245'),
        ('news', '0007_auto_20160215_2018'),
    ]

    operations = [
        migrations.AddField(
            model_name='highlight',
            name='career',
            field=models.ForeignKey(blank=True, to='careers.Career', null=True),
        ),
        migrations.AddField(
            model_name='highlight',
            name='interview',
            field=models.ForeignKey(blank=True, to='careers.Interview', null=True),
        ),
    ]
