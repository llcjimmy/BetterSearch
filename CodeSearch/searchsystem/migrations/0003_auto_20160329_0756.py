# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-29 07:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('searchsystem', '0002_question_question_languagelabel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='question_title',
            field=models.CharField(max_length=2000),
        ),
    ]
