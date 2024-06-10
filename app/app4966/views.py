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
            messages.error(request, f"Erro ao enviar mensagem para fila.")
    
    return render(request, "app4966/sci.html", context)


def sci_relatorio(request):
    if request.method == "POST":
        try:
            print(request.method)
            messages.success(request, "Mensagem enviada para a fila.")
        except Exception as e:
            messages.error(request, f"Erro ao enviar mensagem para fila.")

    return render(request, "app4966/sci_relatorio.html")


def sci_historico(request):
    return render(request, "app4966/sci_historico.html")


def chat_historico(request):
    return render(request, "app4966/chat_historico.html")


def chat_desenvolvedor(request):
    return render(request, "app4966/chat_desenvolvedor.html")
