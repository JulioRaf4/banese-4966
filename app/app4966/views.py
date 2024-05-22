from django.shortcuts import render
from django.http import HttpRequest, HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Chat
import datetime

from .utils import (
    enviaPrompt,
    enviaPromptPreview,
    armazenaReqResponse
)

def index(request):
    return render(request, "app4966/home.html")


def sci(request):
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
            prompt_value = request.POST.get("prompt", "")
            response = enviaPromptPreview(prompt_value)
            context = {
                "prompt_value": prompt_value,
                "response": response
            }
            return render(request, "app4966/sci.html", context)
    
    return render(request, "app4966/sci.html")


def teste_api(request):
    if request.method == "POST":
        try:
            prompt = request.POST["prompt"]
            # response = enviaPrompt(prompt)
            response = "xulio vacilao"
            armazenaReqResponse(prompt, response)
            
            return render(request, "app4966/example.html", {"response": response})

        except Exception as e:
            print(e)

    return render(request, "app4966/example.html")
