from django.shortcuts import render, redirect, get_object_or_404
from rest_framework import generics
from .serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from . import serializers
from rest_framework import status
from django.db.models.query import QuerySet
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework.permissions import  IsAuthenticated
from .models import *
from django.contrib.auth.models import User
from django.utils import timezone


from rest_framework import status, viewsets
from rest_framework.filters import OrderingFilter
from rest_framework.response import Response



class QuizView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
    
#using query filter
class CategoryView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer
    model = Quiz

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        if 'quiz' in self.request.GET:
            return queryset.filter(quiz__iexact=self.request.GET['quiz'])
        return queryset

#with slashes
class CategoryViewQuery(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer
    model = Quiz

    def get_queryset(self):
        queryset1 = Quiz.objects.filter(quiz = self.kwargs['quiz'])
        return queryset1

'''
class ChoiceViews(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [SessionAuthentication]
    queryset = Choice.objects.all()
    serializer_class = ChoiceSerializer
    lookup_field = 'id'

    def get_queryset(self):
        print(self.request.user.id)
        query = Choice.objects.all().values()
        print(query)
        return (query)
        


class MatchViewSet(viewsets.ModelViewSet):
    """
    retrieve:
    Return the given match.    list:
    Return a list of all the existing matches.    create:
    Create a new match instance.
    """
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer # for list view
    def get_serializer_class(self):
        
        return super().get_serializer_class()


    def get_queryset(self):
        """
        Optionally restricts the returned queries by filtering against
        a `sport` and `name` query parameter in the URL.
        """
        queryset = Quiz.objects.all()
        quiz = self.request.query_params.get('quiz', None)
        if quiz is not None:
            sport = sport.title()
            queryset = queryset.filter(quiz__name=quiz)
        return queryset


class UserViewSet(viewsets.ModelViewSet):
    queryset = Choice.objects.all()
    serializer_class =ChoiceSerializer
'''