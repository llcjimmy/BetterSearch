from django.shortcuts import render, get_object_or_404

from django.http import HttpResponse
from django.http import Http404

from django.db.models import Q
from .models import Question, Answer

def help(selectlanguage):
	switch_dict = {
		"csharp" : "C#",
		"cpp" : "C++",
		"c" : "C",
		"css" : "CSS",
		"html" : "HTML",
		"java" : "Java",
		"js" : "JavaScript",
		"oc" : "Objective-C",
		"php" : "PHP",
		"perl" : "Perl",
		"py" : "Python",
		"ruby" : "Ruby",
		"sql" : "SQL",
	}
	return switch_dict.get(selectlanguage)

# Create your views here.
def index(request):
	return render(request, 'searchsystem/index.html')

def search(request):
	selectlanguage = request.POST['languages']
	searchcontent = request.POST['search_text']
	
	question_list = Question.objects.filter(question_languagelabel=selectlanguage)
	question_list = question_list.filter(Q(question_body__icontains=searchcontent) | Q(question_title__icontains=searchcontent))[:20]

	searchlanguage = help(selectlanguage)
	if len(question_list):
		context = {
			'searchlanguage' : searchlanguage,
			'searchcontent' : searchcontent,
			'question_list' : question_list,
		}
	else:
		context = {
			'searchlanguage' : searchlanguage,
			'searchcontent' : searchcontent,
			'error_message' : "Sorry, can't search any results!",
		}
	
	return render(request, 'searchsystem/results.html', context)

def detail(request, question_id):
	question = get_object_or_404(Question, pk=question_id)
	answer_list = question.answer_set.all()
	context = {
		'question' : question,
		'answer_list' : answer_list,
	}

	return render(request, 'searchsystem/detail.html', context)