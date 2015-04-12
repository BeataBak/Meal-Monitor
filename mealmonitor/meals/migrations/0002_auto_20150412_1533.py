# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('meals', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fooditem',
            name='fat',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='fooditem',
            name='net_carbs',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='fooditem',
            name='protein',
            field=models.FloatField(),
        ),
    ]
