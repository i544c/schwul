# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-04 16:20
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('anime', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Character',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('intro', models.CharField(max_length=500)),
                ('anime', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='anime.Anime')),
            ],
        ),
    ]
