from django.shortcuts import render
from django.http import HttpRequest, HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Chat
import datetime
from pymongo import MongoClient
from pymongo.server_api import ServerApi
from django.conf import settings

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

# def teste_api(request):
#     if request.method == "POST":
#         try:
#             prompt = request.POST["prompt"]
#             # response = enviaPrompt(prompt)
#             response = "xulio vacilao"
            
#             # Armazenar no banco de dados
#             chat_entry = Chat(prompt=prompt, response=response)
#             chat_entry.save()
            
#             return render(request, "app4966/example.html", {"response": response})

#         except Exception as e:
#             print(e)

#     return render(request, "app4966/example.html")

def teste_api(request):
    if request.method == "POST":
        try:
            prompt = request.POST["prompt"]
            response = "xulio vacilao"
            
            # Conecte ao MongoDB
            client = MongoClient(settings.MONGODB_URI)
            db = client[settings.MONGODB_DATABASE]
            collection = db[settings.MONGODB_COLLECTION]

            # Insira os dados na coleção
            collection.insert_one({
                "prompt": prompt,
                "response": response,
                "timestamp": datetime.datetime.now()
            })

            return render(request, "app4966/example.html", {"response": response})

        except Exception as e:
            print(e)

    return render(request, "app4966/example.html")