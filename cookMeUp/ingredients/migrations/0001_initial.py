# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-21 06:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='com_ingredients',
            fields=[
                ('name_of_ingredient', models.CharField(db_column='minoringredients', max_length=50, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='dish',
            fields=[
                ('name_of_dish', models.CharField(max_length=50, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='maj_ingredients',
            fields=[
                ('name_of_ingredient', models.CharField(choices=[('veg', 'Vegetable'), ('fruit', 'Fruit')], db_column='majoringredients', max_length=50, primary_key=True, serialize=False)),
            ],
        ),
        migrations.AddField(
            model_name='dish',
            name='ingredient1',
            field=models.ManyToManyField(to='ingredients.maj_ingredients'),
        ),
        migrations.AddField(
            model_name='dish',
            name='ingredient2',
            field=models.ManyToManyField(to='ingredients.com_ingredients'),
        ),
    ]
