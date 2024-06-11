from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('', view=index, name='index'),
    path('sci_provisionamento', view=sci_provisionamento, name='sci_provisionamento'),
    path('sci_relatorio', view=sci_relatorio, name='sci_relatorio'),
    path('sci_historico', view=sci_historico, name='sci_historico'),
    path('chat_historico', view=chat_historico, name='chat_historico'),
    path('chat', view=chat_desenvolvedor, name='chat_desenvolvedor'),
    path('historico/edit/<int:pk>/', SciEditView.as_view(), name='sci_edit'),
    path('historico/delete/<int:pk>/', sci_delete.as_view(), name='sci_delete'),

    ]
