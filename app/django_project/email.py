from django.core.mail import EmailMessage
from django.template.loader import render_to_string

def envia_emails(assunto, mensagem, destinatarios):
    """
    Envia um e-mail com os detalhes fornecidos.

    :param assunto: Assunto do e-mail.
    :param mensagem: Corpo da mensagem em HTML.
    :param destinatarios: Lista de destinatários.
    """
    mail = EmailMessage(
        subject=assunto,
        body=mensagem,
        from_email="baneselabs1@gmail.com",
        to=destinatarios,
    )
    mail.content_subtype = "html"  # Define o conteúdo como HTML
    return mail.send()
