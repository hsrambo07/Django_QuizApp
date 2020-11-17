from django.db import models
from django.contrib.auth.models import User
from django.conf import settings


class Quiz(models.Model):
    user = models.ForeignKey(User, related_name = 'user_status', on_delete = models.CASCADE)
    quiz = models.TextField()
    score = models.IntegerField(default = 0)
    
    def __str__(self):
        return self.quiz


class Question(models.Model):
    quiz_key = models.ForeignKey(Quiz, related_name = 'quiz_question', on_delete = models.CASCADE)
    question = models.TextField()
    image_url = models.URLField(blank = True)

    def __str__(self):
        return self.question


class Choice(models.Model):
    choice_key = models.OneToOneField(Question, related_name = 'question_choice', on_delete = models.CASCADE)
    answer = models.TextField()
    option_one = models.TextField()
    option_two = models.TextField()
    option_three = models.TextField()

    def __str__(self):
        return self.answer
