# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-02-19 15:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chatbot', '0003_auto_20180219_2022'),
    ]

    operations = [
        migrations.AddField(
            model_name='train',
            name='class_bag',
            field=models.CharField(max_length=100000, null=True),
        ),
    ]
