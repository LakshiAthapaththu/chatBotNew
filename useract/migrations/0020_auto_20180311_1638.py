# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-03-11 11:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('useract', '0019_inquiry_datetime'),
    ]

    operations = [
        migrations.CreateModel(
            name='abc',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.TimeField(auto_now_add=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='inquiry',
            name='dateTime',
        ),
    ]
