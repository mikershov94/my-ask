from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.core.paginator import Paginator
from django.urls import reverse
from qa.models import Question
from qa.forms import AskForm, AnswerForm, SignupForm, LoginForm
from qa.helper import do_login
import pudb

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

def question_add(request):
	if request.method == 'POST':	#если метод запроса POST
		form = AskForm(request.POST)	#создаем объект AskForm с содержимым в POST параметре запроса (класс определен в forms.py)
		form._user = request.user
		if form.is_valid():			#проверка валидности формы - к объекту AskForm применяем метод is_valid() - 
			pudb.set_trace()
			question = form.save()	#если форма валидна - сохраняем содержимое формы в БД как объект Question
			return HttpResponseRedirect(reverse(question_details, args=[question.id]))
				#после сохрнения делаем редирект на страницу нового вопроса
	else:		#если метод запроса GET
		form = AskForm()	#создаем пустой объект класса AskForm
	return render(request, 'ask.html',{
		'form': form,
		})

def answer_add(request, question_id):
	question = Question.objects.get(id=question_id)	#получаем из БД объект Question с заданным id
	if request.method == 'POST':	#если метод запроса POST
		form = AnswerForm(request.POST)	#создаем объект AnswerForm с содержимым в POST параметре запроса (класс определен в forms.py)
		form._user = request.user
		if form.is_valid():		#проверка валидности формы - к объекту AnswerForm применяем метод is_valid()
			answer = form.save()	#если форма валидна - сохраняем содержимое формы в БД как объект Answer
			url = question.get_url()	#получаем URL объекта Question
			return HttpResponseRedirect(url)	#после сохранения объекта Answer делаем редирект на полученный URL
	else:		#если метод запроса GET
		form = AnswerForm()		#создаем пустой объект класса AskForm
	return render(request, 'question_details.html', {
		'form': form,
		})

def user_add(request):
	if request.method == 'POST':
		form = SignupForm(request.POST)
		if form.is_valid():
			login = request.POST.get('username')
			password = request.POST.get('password')
			user = form.save()
			url = request.POST.get('continue', '/')
			sessid = do_login(login, password)
			if sessid:
				response = HttpResponseRedirect(url)
				response.set_cookie('sessid', sessid)
				return response
	else:
		form = SignupForm()
	return render(request, 'signup.html', {
		'form': form,
		})

def login(request):
	error = ''
	if request.method == 'POST':
		login = request.POST.get('login')
		password = request.POST.get('password')
		url = request.POST.get('continue', '/')
		sessid = do_login(login, password)
		if sessid:
			response = HttpResponseRedirect(url)
			response.set_cookie('sessid', sessid)
			return response
		else:
			error = 'Bad login or password'
	else:
		form = LoginForm()
	return render(request, 'login.html', {
		'form': form,
		})