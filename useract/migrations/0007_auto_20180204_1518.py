# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-02-04 09:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('useract', '0006_auto_20180202_2240'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdetail',
            name='email',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
