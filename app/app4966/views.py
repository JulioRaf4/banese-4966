from django.shortcuts import render
from django.http import HttpRequest
# Create your views here.


def index(request):
    print("########################################")
    return render(request, 'base/base.html')

def chat(request):
    print("########################################")
    return render(request, 'base/chat.html')