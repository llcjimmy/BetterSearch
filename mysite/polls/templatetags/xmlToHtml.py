from django import template

import HTMLParser

register = template.Library()

def xmlToH(value):
	htmlpa = HTMLParser.HTMLParser()
	newtitle = htmlpa.unescape(value)
	return newtitle

register.filter('xmlToH', xmlToH)