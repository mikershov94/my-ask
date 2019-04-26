from rest_framework import viewsets
from rest_framework.response import Response
from .serializers import *
from qa.models import Question
from django.shortcuts import get_object_or_404

# Create your views here.
class QuestionViewSet(viewsets.ReadOnlyModelViewSet):
	queryset = Question.objects.all()
	
	def list(self, request):
		queryset = Question.objects.new()
		serializer = QuestionSerializer(queryset, many=True)
		return Response(serializer.data)


	def retrieve(self, request, pk):
		queryset = Question.objects.all()
		question = get_object_or_404(queryset, pk=pk)
		serializer = QuestionSerializer(question)
		return Response(serializer.data)

class PopularViewSet(viewsets.ReadOnlyModelViewSet):
	queryset = Question.objects.all()
	
	def list(self, request):
		queryset = Question.objects.popular()
		serializer = QuestionSerializer(queryset, many=True)
		return Response(serializer.data)


	def retrieve(self, request, pk):
		queryset = Question.objects.all()
		question = get_object_or_404(queryset, pk=pk)
		serializer = QuestionSerializer(question)
		return Response(serializer.data)