# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('develop', '0005_auto_20170125_0017'),
    ]

    operations = [
        migrations.RenameField(
            model_name='supportmaterial',
            old_name='document',
            new_name='document_file',
        ),
    ]
