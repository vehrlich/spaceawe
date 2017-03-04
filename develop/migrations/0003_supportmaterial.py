# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('develop', '0002_mooc_position'),
    ]

    operations = [
        migrations.CreateModel(
            name='SupportMaterial',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('title', models.CharField(max_length=255)),
                ('slug', models.SlugField(max_length=255)),
                ('disclaimer', models.CharField(max_length=255)),
                ('cover', models.ImageField(upload_to='support_document', blank=True, null=True)),
                ('file', models.FileField(upload_to='support_document')),
                ('mooc', models.ForeignKey(to='develop.Mooc')),
            ],
        ),
    ]
