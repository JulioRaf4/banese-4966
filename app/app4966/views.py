from django.shortcuts import render
from django.http import HttpRequest, HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

from .utils import (
    enviar_prompt_chatgpt
)

def index(request):
    print("########################################")
    return render(request, 'base/sidebar.html')

def chat(request):
    print("########################################")
    return render(request, 'base/chat.html')

def teste_api(request):
    if request.method == 'POST':
        try:
            prompt = request.POST['prompt']
            response = enviar_prompt_chatgpt(prompt)
            return render(request, 'app4966/example.html', {'response': response})

        except Exception as e:
            print(e)

    return render(request, 'app4966/example.html')

def home(request):
    return render(request, 'base/dados.html')
    # return render(request, 'app4966/home.html')
