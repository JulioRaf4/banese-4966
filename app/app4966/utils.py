import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

def enviar_prompt_chatgpt(prompt):
    api_key = os.environ.get("OPENAI_API_KEY")
    
    if api_key is None:
        raise ValueError("API Key não encontrada. Verifique seu arquivo .env e a variável OPENAI_API_KEY.")

    client = OpenAI(api_key=api_key)

    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", 
                "content": "Crie um json semelhante a este, seguindo exatamente os campos presentes nele, e respeitando os tipos, mas mude o conteudo dos campos para dados ficticios: "+prompt}
                ]
        )
        return(response.choices[0].message.content.strip())

    except Exception as e:
        raise ValueError(f"Erro ao enviar o prompt para o ChatGPT: {str(e)}")
