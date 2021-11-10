from rest_framework import serializers
from .models import Quiz,Category,Question



class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields=['name','detail']

class QuizSerializer(serializers.ModelSerializer):
    class Meta:
        model=Quiz
        fields='__all__'

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model=Question
        fields='__all__'