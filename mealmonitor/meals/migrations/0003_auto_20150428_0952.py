# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('meals', '0002_auto_20150412_1533'),
    ]

    operations = [
        migrations.AddField(
            model_name='fooditem',
            name='is_foundation_vegatable',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='fooditem',
            name='calories',
            field=models.IntegerField(help_text='per 100g'),
        ),
        migrations.AlterField(
            model_name='fooditem',
            name='fat',
            field=models.FloatField(help_text='per 100g'),
        ),
        migrations.AlterField(
            model_name='fooditem',
            name='net_carbs',
            field=models.FloatField(help_text='per 100g'),
        ),
        migrations.AlterField(
            model_name='fooditem',
            name='protein',
            field=models.FloatField(help_text='per 100g'),
        ),
    ]
