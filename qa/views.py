from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.core.paginator import Paginator
from qa.models import Question
#import pudb

# Create your views here.
def test(request, *args, **kwargs):
	return HttpResponse('Hello, world')

def paginate(request, queryset):
	try:
		limit = int(request.GET.get('limit', 10))	#в переменную limit пишем значение из GET-запроса из параметра limit/
													#если GET-параметр пуст - то записываем 10
	except ValueError:		#при ощибке пишем 10
		limit = 10
	if limit > 100:		#ограничение объектов на странице до 100
		limit = 10
	paginator = Paginator(queryset, limit)	#создаем объект класса Paginator
										#объект принимает в качестве аргументов список объектов Question и число объектов на странице
	return paginator

def last_page(request, paginator):
	try:
		numpage = int(request.GET.get('page', 1)) #в переменную numpage пишем количество страниц из GET-параметра
												#если параметр пуст - записываем в переменную 1
	except ValueError:
		raise Http404			#в случае ошибки возвращаем HTTP-ответ 404
	try:
		page = paginator.page(numpage)	#создаем объект page c помощью метода объекта Paginator, который принимает в качестве аргумента число страниц
	except EmptyPage:		#если страница не существует, создаем последнюю страницу (номер последней страницы берем из свойства num_pages объекта Paginator)
		page = paginator.page(paginator.num_pages)
	return page

def new_questions(request):
	questions = Question.objects.new()			#выбираем объекты класса Question из БД.
	paginator = paginate(request, questions)	#создаем объект Paginator с помощью функции
	paginator.baseurl = '/?page='
	page = last_page(request, paginator)		#создаем объект page с помощью функции		
	#pudb.set_trace()
	return render(request, 'new.html', {
		'questions': page.object_list,	#передаем список объектов Question как свойство объекта page (страница)
		'paginator': paginator,			#передаем объект Paginator
		'page': page,						#передаем сам объект page
		})

def popular_questions(request):
	questions = Question.objects.popular()
	paginator = paginate(request, questions)	#создаем объект Paginator с помощью функции
	paginator.baseurl = '/popular/?page='
	page = last_page(request, paginator)		#создаем объект page с помощью функции	
	return render(request, 'popular.html', {
		'questions': page.object_list,
		'paginator': paginator,
		'page': page,
		})

def question_details(request, id):
	question = get_object_or_404(Question, id=id)
	return render(request, 'details.html', {
		'question': question,
		})
