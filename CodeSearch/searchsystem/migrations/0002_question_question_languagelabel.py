# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-24 08:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('searchsystem', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='question_languagelabel',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
    ]