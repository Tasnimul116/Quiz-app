from django.contrib import admin
from django.urls import path
from .views import *


urlpatterns = [
    path('', home , name='home'),
    path('<id>', quiz , name='quiz'),
    path('api/<id>', api_question , name='api_question')
]
