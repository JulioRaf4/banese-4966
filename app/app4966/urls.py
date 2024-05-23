from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('', view=index, name='index'),
    path('sci_provisionamento', view=sci_provisionamento, name='sci_provisionamento'),
    path('sci_relatorio', view=sci_relatorio, name='sci_relatorio'),
    path('sci_historico', view=sci_historico, name='sci_historico'),
    path('chat_historico', view=chat_historico, name='chat_historico'),

    path('teste_api', view=teste_api, name='teste_api'),
]
