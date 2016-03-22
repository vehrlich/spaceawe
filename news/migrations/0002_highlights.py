# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spacescoops', '0006_auto_20160126_2201'),
        ('activities', '0007_auto_20160126_2201'),
        ('games', '0003_auto_20160126_2201'),
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Highlight',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('activity', models.ForeignKey(blank=True, null=True, to='activities.Activity')),
                ('game', models.ForeignKey(blank=True, null=True, to='games.Game')),
                ('news', models.ForeignKey(blank=True, null=True, to='news.Article')),
                ('scoop', models.ForeignKey(blank=True, null=True, to='spacescoops.Article')),
            ],
        ),
    ]
