from django.shortcuts import render
from django.http import HttpRequest, HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django_project.email import envia_emails
from django_project.middleware import *
from .models import *
import datetime
import json
from django.conf import settings
from django.contrib import messages

from .utils.open_ai import *
from .utils.salvar_models import *


@login_required
def index(request):
    return render(request, "app4966/home.html")


# @login_required(redirect_field_name="index")
def sci_provisionamento(request):
    """Função para lidar com requisições HTTP para a página SCI.

    Essa função trata requisições POST para processar dados do formulário
    e gerar respostas apropriadas usando funções auxiliares. Ela também
    renderiza a página 'sci.html' com o contexto atualizado.
    """
    context = {}
    
    if request.method == "POST":
        try:
            entrada = request.POST.get("entrada", "")
            prompt_value = request.POST.get("prompt", "") if not entrada else entrada
            qtde_json = request.POST.get("quantidade-json", "")

            if entrada:
                if not qtde_json:
                    context["error"] = (
                        "Por favor, selecione uma quantidade válida de JSONs."
                    )
                else:
                    response = enviaPromptSCI(prompt_value, qtde_json)
                    asyncio.run(send_messages(response))
                    context = {
                        "prompt_value": prompt_value,
                        "response": response,
                        "quantidade_json": qtde_json,
                    }
                    salvar_chat_provisionamento(
                        request.user, "SCI", prompt_value, response, qtde_json
                    )
            else:
                response = enviaPromptPreview(prompt_value)

                context = {"prompt_value": prompt_value, "response": response}
                salvar_preview_provisionamento(prompt_value, response)
            messages.success(request, "Prompt enviado.")
        except Exception as e:
            error_str = str(e)
            json_start = error_str.find("{")
            json_end = error_str.rfind("}") + 1
            json_str = error_str[json_start:json_end]

            json_str = json_str.replace("'", '"').replace("None", "null")

            try:
                error_dict = json.loads(json_str)
                message = error_dict['error']['message']
                messages.error(request, f"Erro. Prompt não enviado. {repr(message)}")
            except json.JSONDecodeError as jde:
                print("Erro. Prompt não enviado. Erro ao decodificar JSON. String JSON original:", json_str)
            
        
    return render(request, "app4966/sci.html", context)


def sci_relatorio(request):
    if request.method == "POST":
        try:
            messages.success(request, "Prompt enviado.")
        except Exception as e:
            error_str = str(e)
            json_start = error_str.find("{")
            json_end = error_str.rfind("}") + 1
            json_str = error_str[json_start:json_end]

            json_str = json_str.replace("'", '"').replace("None", "null")

            try:
                error_dict = json.loads(json_str)
                message = error_dict['error']['message']
                messages.error(request, f"Erro. Prompt não enviado. {repr(message)}")
            except json.JSONDecodeError as jde:
                print("Erro. Prompt não enviado. Erro ao decodificar JSON. String JSON original:", json_str)

    return render(request, "app4966/sci_relatorio.html")


def sci_historico(request):
    return render(request, "app4966/sci_historico.html")


def chat_historico(request):
    return render(request, "app4966/chat_historico.html")


def chat_desenvolvedor(request):
    return render(request, "app4966/chat_desenvolvedor.html")
