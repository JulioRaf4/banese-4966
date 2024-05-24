from django.db import models
from django.utils import timezone

class Chat(models.Model):
    prompt = models.CharField(max_length=2000)
    response = models.CharField(max_length=2000)
    timestamp = models.DateField(auto_now_add=True)

class Chat_dev(models.Model):
    user_id = models.AutoField(primary_key=True)
    created_at = models.DateField(default=timezone.now)
    updated_at = models.DateField(auto_now=True)
    model_chat = models.CharField(max_length=250)
    conversation = models.JSONField()
    prompt = models.CharField(max_length=2000)
    sended_at = models.DateTimeField(auto_now_add=True)
    response = models.CharField(max_length=2000)
    receive_time = models.DateTimeField(auto_now=True)

    def add_to_conversation(self, prompt_text, response_text):
        """
        Adiciona um novo prompt e response ao campo de conversa com 
        autoincremento para cada item.
        """
        if not self.conversation:
            self.conversation = []
        
        item_id = len(self.conversation) + 1
        self.conversation.append({
            'id': item_id,
            'prompt': prompt_text,
            'response': response_text,
            'sended_at': self.sended_at,
            'receive_time': self.receive_time,
        })
        self.save()

class Chat_provisionamento(models.Model):
    user_id = models.CharField(max_length=100)
    sended_at = models.DateTimeField(default=timezone.now)
    prompt = models.CharField(max_length=2000)
    preview = models.CharField(max_length=500)
    response = models.CharField(max_length=2000)