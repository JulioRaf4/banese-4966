from django.shortcuts import render
from django.http import HttpRequest, HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import *
import datetime
from pymongo import MongoClient
from django.conf import settings
from django_project.email import envia_emails
from .models import ChatProvisionamento


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
        if request.POST.get("entrada", "") == "":
            prompt_value = request.POST.get("prompt", "")
            response = enviaPromptPreview(prompt_value)
            context = {
                "prompt_value": prompt_value,
                "response": response
            }

            return render(request, "app4966/sci.html", context)
        
        else:
            prompt_value = request.POST.get("entrada", "")
            response = enviaPromptSCI(prompt_value)
            context = {
                "prompt_value": prompt_value,
                "response": response
            }
            return render(request, "app4966/sci.html", context)
    
    return render(request, "app4966/sci.html")


def sci_relatorio(request):
    return render(request, "app4966/sci_relatorio.html")


def sci_historico(request):
    # Verificar se as configurações do MongoDB estão definidas corretamente
    try:
        db_settings = settings.DATABASES['default']['CLIENT']
    except KeyError:
        raise KeyError("CLIENT settings not found in DATABASES configuration.")

    # Conectar ao MongoDB
    client = MongoClient(
        host=db_settings['host'],
        port=db_settings['port'],
        username=db_settings['username'],
        password=db_settings['password'],
        authMechanism=db_settings['authMechanism']
    )

    # Selecionar o banco de dados
    db = client['system_db']
    # Selecionar a coleção correta
    collection = db['chats_provisionamento']

    # Buscar os dados na coleção
    historicos = collection.find({}, {'prompt': 1, 'sent': 1})

    # Converter os dados para uma lista
    historicos_list = list(historicos)

    # Renderizar o template com os dados
    return render(request, 'app4966/sci_historico.html', {'historicos': historicos_list})




def chat_historico(request):
    return render(request, "app4966/chat_historico.html")


def chat_desenvolvedor(request):
    return render(request, "app4966/chat_desenvolvedor.html")