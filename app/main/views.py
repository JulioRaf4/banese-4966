from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse


## GENERIC VIEWS ##

def index(request):
    return render(request, 'main/home.html')
