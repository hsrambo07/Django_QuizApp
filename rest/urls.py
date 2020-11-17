from django.contrib import admin
from django.urls import path, include
from .serializers import *
from .token import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/quiz/',include('quiz.urls')),
    path('auth/token', ObtainAuthToken.as_view())
]
