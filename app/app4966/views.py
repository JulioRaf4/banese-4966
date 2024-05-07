from django.shortcuts import render
from django.http import HttpRequest, HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

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
            resposta = enviar_prompt_chatgpt(prompt)
            print(resposta)
            return render(request, 'app4966/example.html', {'resposta': resposta})

        except Exception as e:
            print(e)

    return render(request, 'app4966/example.html')
