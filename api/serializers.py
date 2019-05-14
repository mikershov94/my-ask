from rest_framework import serializers
from qa.models import Question, Answer

class QuestionSerializer(serializers.ModelSerializer):
	likes = serializers.SlugRelatedField(
		many=True,
		read_only=True,
		slug_field='username',
	)

	author = serializers.SlugRelatedField(
		read_only=True,
		slug_field='username',
	)

	class Meta:
		model = Question
		fields = [
			'id',
			'title',
			'text',
			'added_at',
			'author',
			'rating',
			'likes',
		]