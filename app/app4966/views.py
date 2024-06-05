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


def sci_provisionamento(request):
    """Função para lidar com requisições HTTP para a página SCI.

    Essa função trata requisições POST para processar dados do formulário
    e gerar respostas apropriadas usando funções auxiliares. Ela também
    renderiza a página 'sci.html' com o contexto atualizado.
    """
    context = {}

    if request.method == "POST":
        qtde_json = int(request.POST.get("quantidade-json", ""))
        print(request.POST)

        if not qtde_json:
            context['error'] = "Por favor, selecione uma quantidade válida de JSONs."
            return render(request, "app4966/sci.html", context)
        
        if request.POST.get("entrada", "") == "":
            prompt_value = request.POST.get("prompt", "")
            response = enviaPromptPreview(prompt_value, qtde_json)
            print(prompt_value)
            # response = "criou"
            context = {
                "prompt_value": prompt_value,
                "response": response,
                "quantidade_json": qtde_json
            }

            return render(request, "app4966/sci.html", context)
        
        else:
            prompt_value = request.POST.get("entrada", "")
            response = enviaPromptSCI(prompt_value, qtde_json)
            context = {
                "prompt_value": prompt_value,
                "response": response,
                "quantidade_json": qtde_json
            }
            return render(request, "app4966/sci.html", context)
    
    return render(request, "app4966/sci.html")


def sci_relatorio(request):
    return render(request, "app4966/sci_relatorio.html")


def sci_historico(request):
    return render(request, "app4966/sci_historico.html")


def chat_historico(request):
    return render(request, "app4966/chat_historico.html")


def chat_desenvolvedor(request):
    return render(request, "app4966/chat_desenvolvedor.html")