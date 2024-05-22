from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('', view=index, name='index'),
    path('sci', view=sci, name='sci'),
    path('teste_api', view=teste_api, name='teste_api'),
    path('download_json/', download_json, name='download_json'),

]
