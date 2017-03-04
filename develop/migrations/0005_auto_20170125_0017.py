# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('develop', '0004_remove_supportmaterial_mooc'),
    ]

    operations = [
        migrations.RenameField(
            model_name='supportmaterial',
            old_name='file',
            new_name='document',
        ),
    ]
