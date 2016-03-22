# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='game',
            options={'ordering': ['title']},
        ),
        migrations.RenameField(
            model_name='game',
            old_name='name',
            new_name='title',
        ),
        migrations.RenameField(
            model_name='gametranslation',
            old_name='description',
            new_name='story',
        ),
        migrations.AlterField(
            model_name='game',
            name='difficulty',
            field=models.IntegerField(verbose_name='difficulty level', help_text='From 1 to 5.', default=0),
        ),
        migrations.AlterField(
            model_name='game',
            name='fun',
            field=models.IntegerField(verbose_name='fun level', help_text='From 1 to 5.', default=0),
        ),
    ]
