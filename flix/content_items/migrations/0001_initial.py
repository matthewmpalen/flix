# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Episode',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('title', models.CharField(max_length=30)),
                ('description', models.CharField(max_length=200)),
                ('season', models.PositiveSmallIntegerField(default=1)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=30)),
                ('description', models.CharField(max_length=200)),
                ('us_release_date', models.DateField(verbose_name='US Release Date')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('mpaa_rating', models.CharField(verbose_name='MPAA Rating', choices=[('g', 'G'), ('pg', 'PG'), ('pg-13', 'PG-13'), ('r', 'R'), ('nc-17', 'NC-17'), ('nr', 'NR')], max_length=5)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'people',
            },
        ),
        migrations.CreateModel(
            name='Series',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=30)),
                ('description', models.CharField(max_length=200)),
                ('us_release_date', models.DateField(verbose_name='US Release Date')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('us_tv_parental_rating', models.CharField(verbose_name='Parental Rating', choices=[('tv-g', 'TV-G'), ('tv-y', 'TV-Y'), ('tv-y7', 'TV-Y7'), ('tv-pg', 'TV-PG'), ('tv-14', 'TV-14'), ('tv-ma', 'TV-MA')], max_length=5)),
            ],
            options={
                'verbose_name_plural': 'series',
            },
        ),
        migrations.AddField(
            model_name='movie',
            name='director',
            field=models.ForeignKey(to='content_items.Person'),
        ),
        migrations.AddField(
            model_name='episode',
            name='director',
            field=models.ForeignKey(to='content_items.Person'),
        ),
        migrations.AddField(
            model_name='episode',
            name='series',
            field=models.ForeignKey(to='content_items.Series'),
        ),
        migrations.AlterUniqueTogether(
            name='movie',
            unique_together=set([('name', 'us_release_date')]),
        ),
        migrations.AlterUniqueTogether(
            name='episode',
            unique_together=set([('series', 'title')]),
        ),
    ]
