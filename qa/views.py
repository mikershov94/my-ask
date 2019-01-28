from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import Paginator
from qa.models import Question

# Create your views here.
def test(request, *args, **kwargs):
	return HttpResponse('Hello, world')

def new_questions(request):
	questions = Question.objects.new()
	limit = request.GET.get('limit', 10)
	page = request.GET.get('page', 1)
	paginator = Paginator(questions, limit)
	paginator.baseurl = '/?page='
	page = paginator.page(page)
	return render(request, 'new.html', {
		questions: page.object_list,
		paginator: paginator,
		page: page,
		})

def popular_questions(request):
	questions = Question.objects.popular()
	limit = request.GET.get('limit', 10)
	page = request.GET.get('page', 1)
	paginator = Paginator(questions, limit)
	paginator.baseurl = '/?page='
	page = paginator.page(page)
	return render(request, 'new.html', {
		questions: page.object_list,
		paginator: paginator,
		page: page,
		})