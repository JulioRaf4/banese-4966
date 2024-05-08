from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
# Create your views here.


def index(request):
    print("########################################")
    return render(request, 'base/base.html')

def chat(request):
    print("########################################")
    return render(request, 'base/chat.html')

def home(request):
    return render(request, 'app4966/home.html')