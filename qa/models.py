from django.db import models
from django.contrib.auth.models import User
from django.contrib.sessions.models import Session

# Create your models here.
class QuestionManager(models.Manager):
	def new(self):
		return self.order_by('-added_at')

	def popular(self):
		return self.order_by('-rating')

class Question(models.Model):
	objects = QuestionManager()
	title = models.CharField(max_length=50)
	text = models.TextField()
	added_at = models.DateTimeField(auto_now_add=True)
	rating = models.IntegerField(default=0)
	author = models.ForeignKey(User, default=1, on_delete=models.DO_NOTHING)
	likes = models.ManyToManyField(User, related_name='likes_set')

	def __unicode__(self):
		return self.title

class Answer(models.Model):
	text = models.TextField()
	added_at = models.DateTimeField(auto_now_add=True)
	question = models.ForeignKey(Question, on_delete=models.DO_NOTHING)
	author = models.ForeignKey(User, default=1, on_delete=models.DO_NOTHING)

	def __unicode__(self):
		return self.title

class Session(Session):
	user = models.ForeignKey(User, on_delete=models.DO_NOTHING)

