# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


def copy_urls(apps, schema_editor):
    Game = apps.get_model("games", "Game")
    for game in Game.objects.all():
        game.links.create(name='', url=game.url)
        game.save()


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0003_auto_20160126_2201'),
    ]

    operations = [
        migrations.CreateModel(
            name='GameLink',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(max_length=255, blank=True)),
                ('url', models.URLField(verbose_name='URL', max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='gamelink',
            name='game',
            field=models.ForeignKey(related_name='links', to='games.Game'),
        ),
        migrations.RunPython(copy_urls),
        migrations.RemoveField(
            model_name='game',
            name='url',
        ),
    ]
