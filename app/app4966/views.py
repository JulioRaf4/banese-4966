from django.shortcuts import render
from django.http import HttpRequest, HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.edit import DeleteView , UpdateView
from django.urls import reverse_lazy
from django.contrib import messages
from django_project.email import envia_emails
from django_project.middleware import *
from .models import *
import datetime
import json
from django.conf import settings
from django_project.email import envia_emails
from .utils.open_ai import *
from .utils.salvar_models import *
from django.core.paginator import Paginator


# @login_required
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
            response = request.POST.get("prompt", "")
            #asyncio.run(send_messages(response))
            messages.success(request, "Mensagem enviada para a fila.")
        except Exception as e:
            messages.error(request, f"Erro ao enviar mensagem para fila.")

    return render(request, "app4966/sci_relatorio.html")


def sci_historico(request):
    historicos = Chat_provisionamento.objects.all().order_by('-sent')
    paginator = Paginator(historicos, 8)  # Mostra 8 itens por página
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, "app4966/sci_historico.html", {'page_obj': page_obj})


def historico_view(request):
    historicos = sci_historico.objects.all()
    paginator = Paginator(historicos, 8)  # Mostra 8 itens por página

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'template.html', {'page_obj': page_obj})

class sci_delete(SuccessMessageMixin, DeleteView):
    model = Chat_provisionamento
    success_url = reverse_lazy('sci_historico')  # Redireciona para a lista de históricos após a exclusão
    template_name = 'app4966/chat_confirm_delete.html'  # Template para a confirmação de exclusão


class sci_update(SuccessMessageMixin, UpdateView):
    model = Chat_provisionamento
    fields = ['descricao']  # Apenas o campo 'prompt' será editável
    template_name = 'app4966/chat_edit_form.html'
    success_url = reverse_lazy('sci_historico')
    success_message = "Registro atualizado com sucesso!"

    
def chat_historico(request):
    return render(request, "app4966/chat_historico.html")


def chat_desenvolvedor(request):
    return render(request, "app4966/chat_desenvolvedor.html")
