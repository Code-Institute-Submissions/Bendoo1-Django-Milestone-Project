# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-04-29 13:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0007_auto_20200429_1352'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='rating',
            field=models.CharField(max_length=1),
        ),
    ]