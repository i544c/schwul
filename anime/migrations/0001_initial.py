# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-25 19:03
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Anime',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('bc_year', models.IntegerField(default=2017, validators=[django.core.validators.MinValueValidator(1000), django.core.validators.MaxValueValidator(3000)])),
                ('synopsis', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Story',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subtitle', models.CharField(max_length=100)),
                ('bc_date', models.DateField(verbose_name='broadcast date')),
                ('description', models.CharField(max_length=500)),
                ('anime', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='anime.Anime')),
            ],
        ),
    ]
