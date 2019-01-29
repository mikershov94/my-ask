from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.new_questions, name='new_questions'),
	url(r'^popular/$', views.popular_questions, name='popular_questions'),
	url(r'^question/(?P<id>\d+)/$', views.question_details, name='question_details'),
	url(r'^signup/$', views.test, name='test'),
	url(r'^login/$', views.test, name='test'),
	url(r'^ask/$', views.test, name='test'),
]