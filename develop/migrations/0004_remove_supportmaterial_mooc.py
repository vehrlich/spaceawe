# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('develop', '0003_supportmaterial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='supportmaterial',
            name='mooc',
        ),
    ]
