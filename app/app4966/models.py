from django.db import models

class Chat(models.Model):
    prompt = models.CharField(max_length=2000)
    response = models.CharField(max_length=2000)
    timestamp = models.DateField(auto_now_add=True)
