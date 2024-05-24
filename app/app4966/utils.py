import os
from openai import OpenAI
from dotenv import load_dotenv
from .models import Chat
from django.http import JsonResponse
from django.conf import settings
import datetime
from pymongo import MongoClient

load_dotenv()

client = OpenAI(api_key="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")


def enviaPrompt(prompt):
    # api_key = os.environ.get("OPENAI_API_KEY")

    # if api_key is None:
    #     raise ValueError("API Key não encontrada. Verifique seu arquivo .env e a variável OPENAI_API_KEY.")
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "user",
                    "content": "Crie um json semelhante a este, seguindo exatamente os campos presentes nele, e respeitando os tipos, mas mude o conteudo dos campos para dados ficticios: "
                    + prompt,
                }
            ],
        )
        return response.choices[0].message.content.strip()

    except Exception as e:
        raise ValueError(f"Erro ao enviar o prompt para o ChatGPT: {str(e)}")


def enviaPromptPreview(prompt):
    """Função para receber preview do modelo do ChatGPT
    antes de realizar a criação dos dados para os testes
    """

    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "user",
                    "content": """Crie um json semelhante a este, seguindo exatamente os campos presentes nele, 
                    e respeitando os tipos, mas foque em mudar o conteudo dos campos para que que seja um Json com dados ficticio.
                    Json: """
                    + prompt,
                }
            ],
        )
        return response.choices[0].message.content.strip()

    except Exception as e:
        raise ValueError(f"Erro ao enviar o prompt para o ChatGPT: {str(e)}")


def enviaPromptSCI(prompt, entrada):
    """Função para enviar prompt e criar Dados
    Envia também para a fila de provisionamento
    """
    ...

def armazenaTabelaChats(prompt, response):
    """Função para armazenar a request e a response no banco de dados"""
    try:
        client = MongoClient(settings.MONGODB_URI)
        db = client[settings.MONGODB_DATABASE]
        collection = db["chats"]

        collection.insert_one({
            "prompt": prompt,
            "response": response,
            "timestamp": datetime.datetime.now()
        })
        print(JsonResponse({'status': 'success', 'message': 'Prompt armazenado com sucesso'}))

    except Exception as e:
        print(e)