import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "CodeSearch.settings")

import django

if django.VERSION >= (1, 7):
	django.setup()

import xml.sax
from searchsystem.models import Question, Answer

IDdict = dict()
dataBaseIDdict = dict()

def init():
	f = open("/Users/jimmy/homework//SearchSystemDataPrepare/QuestionsID.txt", 'r')
	f2 = open("/Users/jimmy/homework//SearchSystemDataPrepare/QuestionsLanguageType.txt", 'r')
	while (True):
		line = f.readline()
		line2 = f2.readline()
		if (not line) and (not line2):
			break
		line = line.strip()
		line2 = line2.strip()
		IDdict[line] = line2

def help(selectlanguage):
	switch_dict = {
		"c#" : "csharp",
		"c++" : "cpp",
		"c" : "c",
		"css" : "css",
		"html" : "html",
		"java" : "java",
		"javascript" : "js",
		"objective-c" : "oc",
		"php" : "php",
		"perl" : "perl",
		"python" : "py",
		"ruby" : "ruby",
		"sql" : "sql",
	}
	return switch_dict.get(selectlanguage)


class SOQHandler(xml.sax.ContentHandler):
	def __init__(self):
		self.type = 0
		self.id = ""
		self.score = ""
		self.viewcount = ""
		self.body = ""
		self.title = ""
		self.tags = ""

	def startElement(self, tag, attributes):
		if tag == "row":
			#print "row"
			if attributes["PostTypeId"] == "1":
				self.id = attributes["Id"]
				if IDdict.has_key(self.id):
					print "Question: " + self.id
					self.type = 1
					self.score = attributes["Score"]
					self.viewcount = attributes["ViewCount"]
					self.body = attributes["Body"]
					self.title = attributes["Title"]
					self.tags = attributes["Tags"]



	def endElement(self, tag):
		if self.type == 1:
			scoretemp = 0
			if self.score != "":
				try:
					scoretemp = int(self.score)
				except (ValueError):
					scoretemp = 0
			vctemp = 0
			if self.viewcount != "":
				try:
					vctemp = int(self.viewcount)
				except (ValueError):
					vctemp = 0
			q = Question(question_title=self.title, question_body=self.body,question_languagelabel=help(IDdict[self.id]),question_tags=self.tags,question_score=scoretemp,question_viewcount=vctemp)
			q.save()
			dataBaseIDdict[self.id] = q.id

		self.type = 0
		self.id = ""
		self.score = ""
		self.viewcount = ""
		self.body = ""
		self.title = ""
		self.tags = ""

	def characters(self, content):
		pass

class SOAHandler(xml.sax.ContentHandler):
	def __init__(self):
		self.type = 0
		self.id = ""
		self.score = ""
		self.viewcount = ""
		self.body = ""
		self.title = ""
		self.tags = ""

	def startElement(self, tag, attributes):
		if tag == "row":
			#print "row"
			if attributes["PostTypeId"] == "2":
				self.id = attributes["ParentId"]
				if IDdict.has_key(self.id):
					print "Question: " + self.id + " Answer: " + attributes["Id"]
					self.type = 2
					self.score = attributes["Score"]
					self.viewcount = attributes["ViewCount"]
					self.body = attributes["Body"]



	def endElement(self, tag):
		if self.type == 2:
			q = Question.objects.get(pk=dataBaseIDdict[self.id])
			scoretemp = 0
			if self.score != "":
				try:
					scoretemp = int(self.score)
				except (ValueError):
					scoretemp = 0
			vctemp = 0
			if self.viewcount != "":
				try:
					vctemp = int(self.viewcount)
				except (ValueError):
					vctemp = 0
			c = q.answer_set.create(answer_body=self.body,answer_score=scoretemp,answer_viewcount=vctemp)

		self.type = 0
		self.id = ""
		self.score = ""
		self.viewcount = ""
		self.body = ""
		self.title = ""
		self.tags = ""

	def characters(self, content):
		pass

if __name__ == "__main__":
	init()

	parserQ = xml.sax.make_parser()
	parserQ.setFeature(xml.sax.handler.feature_namespaces, 0)

	QHandler = SOQHandler()
	parserQ.setContentHandler(QHandler)

	parserQ.parse("/Users/jimmy/StackOverflow/raw-data/posts.xml")
	print('Question Done!')

	parserA = xml.sax.make_parser()
	parserA.setFeature(xml.sax.handler.feature_namespaces, 0)

	AHandler = SOAHandler()
	parserA.setContentHandler(AHandler)

	parserA.parse("/Users/jimmy/StackOverflow/raw-data/posts.xml")
	print('Answer Done!')