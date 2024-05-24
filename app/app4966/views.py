import json
from django.shortcuts import render
from django.http import HttpRequest, HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Chat
import datetime
from pymongo import MongoClient
from django.conf import settings

from .utils import (
    enviaPrompt,
    enviaPromptPreview,
    enviaPromptSCI,
    armazenaTabelaChats
)

def index(request):
    return render(request, "app4966/home.html")


def sci_provisionamento(request):
    """Função para lidar com requisições HTTP para a página SCI.

    Essa função trata requisições POST para processar dados do formulário
    e gerar respostas apropriadas usando funções auxiliares. Ela também
    renderiza a página 'sci.html' com o contexto atualizado.
    """
    context = {}

    if request.method == "POST":
        print(request.POST)
        prompt_value = request.POST.get("prompt", "")
        entrada_value = request.POST.get("entrada", "")

        if not entrada_value:
            context["response"] = enviaPromptPreview(prompt_value)
        else:
            saida_value = request.POST.get("saida", "")
            context["response"] = enviaPromptSCI(
                entrada_value, entrada_value, saida_value
            )

        context["prompt_value"] = prompt_value

    return render(request, "app4966/sci.html", context)


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
            response = "teste quinta"
            
            armazenaTabelaChats(prompt=prompt, response=response)

            return render(request, "app4966/example.html", {"response": response})

        except Exception as e:
            print(e)

    return render(request, "app4966/example.html")