from rest_framework import viewsets
from rest_framework import generics
from rest_framework.response import Response
from .serializers import *
from qa.models import Question
from django.shortcuts import get_object_or_404


# Create your views here.
class LastListView(generics.ListAPIView):
	queryset = Question.objects.new()
	serializer_class = QuestionSerializer

class PopularListView(generics.ListAPIView):
	queryset = Question.objects.popular()
	serializer_class = QuestionSerializer

class LastDetailView(generics.RetrieveAPIView):
	queryset = Question.objects.new()
	serializer_class = QuestionSerializer

class PopularDetailView(generics.RetrieveAPIView):
	queryset = Question.objects.popular()
	serializer_class = QuestionSerializer