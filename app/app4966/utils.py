import os
from openai import OpenAI
from dotenv import load_dotenv

# Carregar as variáveis de ambiente do arquivo .env
load_dotenv()

def enviar_prompt_chatgpt(prompt):

    client = OpenAI(
    # defaults to os.environ.get("OPENAI_API_KEY")
    api_key="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",
    )

    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}]
        )
        # Extrair e retornar a resposta do modelo GPT-3.5
        print(response.choices[0].message.content.strip())

    except Exception as e:
        raise ValueError(f"Erro ao enviar o prompt para o ChatGPT: {str(e)}")
