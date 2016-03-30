#coding=utf-8
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Question(models.Model):
	question_title = models.CharField(max_length=2000)
	question_body = models.TextField()
	question_languagelabel = models.CharField(max_length=200)
	question_tags = models.CharField(max_length=200)
	question_score = models.IntegerField(default=0)
	question_viewcount = models.IntegerField(default=0)

	def __str__(self):
		return self.question_title

class Answer(models.Model):
	question = models.ForeignKey(Question, on_delete=models.CASCADE)
	answer_body = models.TextField()
	answer_score = models.IntegerField(default=0)
	answer_viewcount = models.IntegerField(default=0)

	def __str__(self):
		return "answer"