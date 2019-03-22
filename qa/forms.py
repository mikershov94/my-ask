from django import forms
from qa.models import Question, Answer
from django.contrib.auth.models import User

def is_ask(cleaned_data):
	text = cleaned_data['text']
	if len(text) > 0:
		return True
	else:
		return False

def is_answer(cleaned_data):
	text = cleaned_data['text']
	if len(text) > 0:
		return True
	else:
		return False

def is_signup(cleaned_data):
	login = cleaned_data['username']
	password = cleaned_data['password']
	if len(login) > 0 or len(password) > 0:
		return True
	else:
		return False

def is_login(cleaned_data):
	login = cleaned_data['login']
	password = cleaned_data['password']
	if len(login) > 0 or len(password) > 0:
		return True
	else:
		return False

class AskForm(forms.ModelForm):
	class Meta:
		model = Question
		fields = ('title', 'text',)

	def save(self):
		self.cleaned_data['author'] = self._user
		return Question.objects.create(**self.cleaned_data)

class AnswerForm(forms.ModelForm):
	class Meta:
		model = Answer
		fields = ('text',)
	question = forms.IntegerField()

	def save(self):
		self.cleaned_data['author'] = self._user
		return Question.objects.create(**self.cleaned_data)

class SignupForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ('username', 'email', 'password',)

class LoginForm(forms.Form):
	login = forms.CharField(max_length=255)
	password = forms.CharField()

	
