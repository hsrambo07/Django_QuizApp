from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User


class ChoiceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Choice
        fields = (
            "answer",
            "option_one",
            "option_two",
            "option_three",
        )


class QuestionSerializer(serializers.ModelSerializer):
    
    question_choice = ChoiceSerializer(read_only = True)
    class Meta:
        model = Question
        fields = (
            "question",
            "image_url",
            "question_choice"
        )


class QuizSerializer(serializers.ModelSerializer):
    quiz_question = QuestionSerializer(many = True, read_only = True)
    class Meta:
        model = Quiz
        fields = (
            "quiz",
            "quiz_question"
        )


class UserSerializer(serializers.ModelSerializer):
     user_status = QuizSerializer(many = True, read_only = True)
     class Meta:
         model = User
         fields = (
             'username',
             'user_status'
         )


