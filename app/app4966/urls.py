from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('', view=home, name='home'),
    path('chat', view=chat, name='chat'),
]
