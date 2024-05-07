from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('', view=index, name='index'),
    path('chat', view=chat, name='chat'),
    path('teste_api', view=teste_api, name='teste_api'),
]
