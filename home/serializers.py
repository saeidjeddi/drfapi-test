from rest_framework import serializers
from .models import Question, Answer


class PersonsSerialize(serializers.Serializer):
    name = serializers.CharField(max_length=35)
    age = serializers.IntegerField()
    email = serializers.EmailField()


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = '__all__'
