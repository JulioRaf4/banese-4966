from app4966.models import Preview_provisionamento, Chat_provisionamento


def salvar_preview_provisionamento(prompt, response):
    """Função para salvar dados de PreviewProvisionamento no banco de dados."""
    Preview_provisionamento.objects.create(
        prompt=prompt,
        chat_model='gpt-3.5-turbo',  # Substitua por qualquer valor necessário
        response=response
    )

def salvar_chat_provisionamento(user, sistema, prompt, response, qtde_json):
    """Função para salvar dados de ChatProvisionamento no banco de dados."""
    Chat_provisionamento.objects.create(
        user=user,
        sistema=sistema,
        prompt=prompt,
        chat_model='gpt-3.5-turbo',  # Substitua por qualquer valor necessário
        response=response,
        quantidade_json = qtde_json
    )
