from rest_framework import serializers
from qa.models import Question, Answer

class QuestionSerializer(serializers.ModelSerializer):
	class Meta:
		model = Question
		fields = [
			'title',
			'text',
			'added_at',
		]