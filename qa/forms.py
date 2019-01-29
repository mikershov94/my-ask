from django import forms
from qa.models import Question, Answer

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

class AskForm(forms.ModelForm):
	class Meta:
		model = Question
		fields = ['title', 'text']

class AnswerForm(forms.ModelForm):
	class Meta:
		model = Answer
		fields = ['text']
