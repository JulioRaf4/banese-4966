from django.shortcuts import render
from django.http import HttpRequest, HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import *
import datetime
from pymongo import MongoClient
from django.conf import settings
from django_project.email import envia_emails

from .utils import (
    enviaPrompt,
    enviaPromptPreview,
    enviaPromptSCI,
)


def index(request):
    return render(request, "app4966/home.html")

def chat(request):
    return render(request, "base/chat.html")


def sci_provisionamento(request):
    """Função para lidar com requisições HTTP para a página SCI.

    Essa função trata requisições POST para processar dados do formulário
    e gerar respostas apropriadas usando funções auxiliares. Ela também
    renderiza a página 'sci.html' com o contexto atualizado.
    """
    context = {}

    if request.method == "POST":
        if request.POST.get("entrada", "") == "":
            prompt_value = request.POST.get("prompt", "")
            response = enviaPromptPreview(prompt_value)
            context = {
                "prompt_value": prompt_value,
                "response": response
            }
            chat = Chat_provisionamento(prompt=prompt_value, response=response)
            chat.armazenaReqResponse()

            return render(request, "app4966/sci.html", context)
        
        else:
            prompt_value = request.POST.get("prompt", "")
            response = enviaPromptPreview(prompt_value)
            context = {
                "prompt_value": prompt_value,
                "response": response
            }
            chat = Chat_provisionamento(prompt=prompt_value, response=response)
            chat.armazenaReqResponse()

            return render(request, "app4966/sci.html", context)
    
    return render(request, "app4966/sci.html")


def sci_relatorio(request):
    return render(request, "app4966/sci_relatorio.html")


def sci_historico(request):
    return render(request, "app4966/sci_historico.html")


def chat_historico(request):
    return render(request, "app4966/chat_historico.html")


def teste_api(request):
    if request.method == "POST":
        try:
            prompt = request.POST["prompt"]
            response = "teste provisionamento"
            
            chat = Chat_provisionamento(prompt=prompt, response=response)


            return render(request, "app4966/example.html", {"response": response})
        except Exception as e:
            print(e)

    return render(request, "app4966/example.html")
