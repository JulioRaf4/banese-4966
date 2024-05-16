from django.shortcuts import render
from django.http import HttpRequest, HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .utils import enviar_prompt_chatgpt


def index(request):
    return render(request, "app4966/home.html")


def sci(request):
    print(request.POST)
    prompt_value = request.POST.get('prompt', '')
    context = {
        'prompt_value': prompt_value,
    }
    return render(request, "app4966/sci.html", context)


def teste_api(request):
    if request.method == "POST":
        try:
            prompt = request.POST["prompt"]
            response = enviar_prompt_chatgpt(prompt)
            return render(request, "app4966/example.html", {"response": response})

        except Exception as e:
            print(e)

    return render(request, "app4966/example.html")
