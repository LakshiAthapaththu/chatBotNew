# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-03-10 03:21
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('chatbot', '0008_auto_20180223_2127'),
    ]

    operations = [
        migrations.AddField(
            model_name='classes',
            name='layer_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='chatbot.Layers'),
            preserve_default=False,
        ),
    ]
