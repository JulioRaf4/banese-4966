import json
from django.shortcuts import render
from django.http import HttpRequest, HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .utils import (
    enviaPrompt,
    enviaPromptPreview,
    enviaPromptSCI
)

def index(request):
    return render(request, "app4966/home.html")


def sci(request):
    context = {}

    if request.method == "POST":
        prompt_value = request.POST.get("prompt", "")
        entrada_value = request.POST.get("entrada", "")

        if not entrada_value:
            context["response"] = enviaPromptPreview(prompt_value)
        else:
            saida_value = request.POST.get("saida", "")
            context["response"] = enviaPromptSCI(prompt_value, entrada_value, saida_value)

        context["prompt_value"] = prompt_value

    return render(request, "app4966/sci.html", context)


def teste_api(request):
    if request.method == "POST":
        try:
            prompt = request.POST["prompt"]
            response = enviaPrompt(prompt)
            return render(request, "app4966/example.html", {"response": response})

        except Exception as e:
            print(e)

    return render(request, "app4966/example.html")


def download_json(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        prompt_value = request.POST.get("prompt", "")
        response_data = enviaPromptPreview(prompt_value)
        
        try:
            response_json = json.loads(response_data)
        except json.JSONDecodeError:
            return HttpResponse("Erro ao decodificar o JSON.", status=400)

        response_json_str = json.dumps(response_json, indent=4)

        response = HttpResponse(response_json_str, content_type='application/json')
        response['Content-Disposition'] = 'attachment; filename="response.json"'
        return response

    return HttpResponse("Método não permitido.", status=405)