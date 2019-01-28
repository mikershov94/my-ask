from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.core.paginator import Paginator
from qa.models import Question

# Create your views here.
def test(request, *args, **kwargs):
	return HttpResponse('Hello, world')

def new_questions(request):
	questions = Question.objects.new()			#выбираем объекты класса Question из БД.
	limit = request.GET.get('limit', 10)		#в переменную limit пишем значение из GET-запроса из параметра limit/
													#если GET-параметр пуст - то записываем 10
	page = request.GET.get('page', 1)			#в переменную page пишем значение из GET-параметра page
													#если GET-параметр пуст - то записываем 1
	paginator = Paginator(questions, limit)		#создаем объект класса Paginator
										#объект принимает в качестве аргументов список объектов Question и число объектов на странице
	paginator.baseurl = '/?page='
	page = paginator.page(page)			#создаем объект page c помощью метода объекта Paginator, который принимает в качестве аргумента число страниц
	return render(request, 'new.html', {
		questions: page.object_list,	#передаем список объектов Question как свойство объекта page (страница)
		paginator: paginator,			#передаем объект Paginator
		page: page,						#передаем сам объект page
		})

def popular_questions(request):
	questions = Question.objects.popular()
	limit = request.GET.get('limit', 10)
	page = request.GET.get('page', 1)
	paginator = Paginator(questions, limit)
	paginator.baseurl = 'popular/?page='
	page = paginator.page(page)
	return render(request, 'new.html', {
		questions: page.object_list,
		paginator: paginator,
		page: page,
		})

def question_details(request, pk):
	question = get_object_or_404(Question, pk=pk)
	return render(request, 'details.html', {
		question: question,
		})
