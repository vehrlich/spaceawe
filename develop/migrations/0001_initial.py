# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Module',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('info', models.CharField(max_length=255)),
                ('duration', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Mooc',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('info', models.CharField(max_length=255)),
                ('starting_date', models.CharField(max_length=255)),
                ('is_active', models.BooleanField(default=False)),
                ('enroll_url', models.URLField(blank=True)),
                ('introduction', models.TextField()),
                ('what_you_will_learn', models.TextField()),
                ('what_skills_will_you_need', models.TextField()),
                ('duration_of_the_course', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='module',
            name='mooc',
            field=models.ForeignKey(to='develop.Mooc'),
        ),
    ]
