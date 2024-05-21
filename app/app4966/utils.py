import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key="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")


def enviaPrompt(prompt: str) -> str:
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


def enviaPromptPreview(prompt: str) -> str:
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
        error_message = f"Erro ao enviar o prompt para o ChatGPT: {str(e)}"
        print(error_message) 
        raise ValueError(error_message)


def enviaPromptSCI(prompt: str, entrada: str, saida: str) -> str:
    """Função para enviar prompt e criar Dados
    Envia também para a fila de provisionamento
    """
    try:
        response = client.chat.completions.create(
            temperature=0.6,
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "user",
                    "content": """Crie CINCO (5) json's semelhantes a este, seguindo exatamente os campos presentes nele, 
                    e respeitando os tipos, mas foque em mudar o conteudo dos campos para que que seja os jsons sejam fictions.
                    Me dê apenas os json concatenados, só e somente e o Json como resposta.
                    Json: """
                    + prompt,
                }
            ],
        )
        print(response.choices[0].message.content.strip())
        return response.choices[0].message.content.strip()

    except Exception as e:
        error_message = f"Erro ao enviar o prompt para o ChatGPT: {str(e)}"
        print(error_message) 
        raise ValueError(error_message)