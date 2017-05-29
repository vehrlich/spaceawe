# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('contests', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contestsectiontranslation',
            name='content',
            field=ckeditor.fields.RichTextField(null=True, blank=True),
        ),
    ]
