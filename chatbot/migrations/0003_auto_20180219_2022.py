# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-02-19 14:52
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chatbot', '0002_auto_20180219_2021'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='UserDetail',
            new_name='train',
        ),
    ]
