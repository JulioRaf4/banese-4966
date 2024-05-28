from django.core.mail import send_mail
from django.conf import settings

def send_custom_email(subject, message, recipient_list, from_email=None):
    """
    Envia um email personalizado.

    Args:
        subject (str): O assunto do email.
        message (str): O corpo da mensagem.
        recipient_list (list): Lista de destinatários.
        from_email (str, optional): Email do remetente. Se não for fornecido, será usado o padrão das configurações.
    """
    if from_email is None:
        from_email = settings.EMAIL_HOST_USER
    
    send_mail(
        subject,
        message,
        from_email,
        recipient_list,
        fail_silently=False,
    )
