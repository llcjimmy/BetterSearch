# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-22 13:20
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer_body', models.TextField()),
                ('answer_score', models.IntegerField(default=0)),
                ('answer_viewcount', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_title', models.CharField(max_length=200)),
                ('question_body', models.TextField()),
                ('question_tags', models.CharField(max_length=200)),
                ('question_score', models.IntegerField(default=0)),
                ('question_viewcount', models.IntegerField(default=0)),
            ],
        ),
        migrations.AddField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='searchsystem.Question'),
        ),
    ]
