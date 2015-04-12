# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FoodItem',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=128, blank=True)),
                ('net_carbs', models.IntegerField()),
                ('fat', models.IntegerField()),
                ('protein', models.IntegerField()),
                ('calories', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='FoodItemMeal',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('quantity', models.IntegerField()),
                ('food_item', models.ForeignKey(to='meals.FoodItem')),
            ],
        ),
        migrations.CreateModel(
            name='Meal',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=128, blank=True)),
                ('date_ate', models.DateTimeField(auto_now_add=True)),
                ('food_items', models.ManyToManyField(to='meals.FoodItem', through='meals.FoodItemMeal')),
            ],
        ),
        migrations.AddField(
            model_name='fooditemmeal',
            name='meal',
            field=models.ForeignKey(to='meals.Meal'),
        ),
    ]
