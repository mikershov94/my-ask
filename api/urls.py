from django.urls import path
from .views import *

urlpatterns = [
	path('last/', LastListView.as_view()),
	path('popular/', PopularListView.as_view()),
	path('last/<pk>', LastDetailView.as_view()),
	path('popular/<pk>', PopularDetailView.as_view()),
]