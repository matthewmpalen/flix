# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0001_initial'),
        ('content_items', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='tags',
            field=models.ManyToManyField(related_name='movie', to='common.Tag'),
        ),
        migrations.AddField(
            model_name='series',
            name='tags',
            field=models.ManyToManyField(related_name='series', to='common.Tag'),
        ),
    ]
