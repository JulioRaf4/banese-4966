from django.db import models
from django.utils import timezone
from django.http import JsonResponse



class Chat_dev(models.Model):
    user_id = models.AutoField(primary_key=True)
    created_at = models.DateField(default=timezone.now)
    updated_at = models.DateField(auto_now=True)
    model_chat = models.CharField(max_length=250)
    prompt = models.CharField(max_length=2000)
    sent = models.DateTimeField(auto_now_add=True)
    response = models.CharField(max_length=2000)
    receive_time = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "chats_dev"

    def armazenaReqResponse(self):
        """Função para armazenar a request e a response no banco de dados"""
        try:
            self.save(using="mongodb")
            print(JsonResponse({'status': 'success', 'message': 'Prompt armazenado com sucesso'}))

        except Exception as e:
            print(e)

    

class Chat_provisionamento(models.Model):
    user_id = models.CharField(max_length=100)
    sended_at = models.DateTimeField(default=timezone.now)
    prompt = models.CharField(max_length=2000)
    preview = models.CharField(max_length=500)
    response = models.CharField(max_length=2000)

    class Meta:
        db_table = "chats_provisionamento"

    def armazenaReqResponse(self):
        """Função para armazenar a request e a response no banco de dados"""
        try:
            self.save(using="mongodb")
            print(JsonResponse({'status': 'success', 'message': 'Prompt armazenado com sucesso'}))

        except Exception as e:
            print(e)