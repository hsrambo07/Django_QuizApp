from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from . import views
from rest_framework.routers import DefaultRouter
from rest_framework.schemas import get_schema_view
from rest_framework.documentation import include_docs_urls
from rest_framework_swagger.views import get_swagger_view

from rest_framework_swagger.renderers import SwaggerUIRenderer, OpenAPIRenderer

schema_view = get_schema_view(title='Users API', renderer_classes=[OpenAPIRenderer, SwaggerUIRenderer])
router = DefaultRouter()

urlpatterns = [
    path('', views.QuizView.as_view()),
    path('category/', views.CategoryView.as_view()),
    path('cate/<str:quiz>', views.CategoryViewQuery.as_view()),
    path(r'docs/', include_docs_urls(title='Polls API')),
]

