# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-10 03:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20160410_0319'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='token',
            field=models.CharField(max_length=180),
        ),
    ]
