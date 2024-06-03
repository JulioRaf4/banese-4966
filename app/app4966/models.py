from django.db import models
from django.utils import timezone
from django.http import JsonResponse
from django.contrib.auth.models import User


class Conversa(models.Model):
    sent = models.DateTimeField(auto_now_add=True, null=False)
    prompt = models.CharField(max_length=10000, null=False)
    response = models.CharField(max_length=100000, null=False)

    class Meta:
        ordering = ["sent"]

    def __str__(self) -> str:
        return self.prompt


class Preview_provisionamento(models.Model): ...


class Chat_desenvolvedor(models.Model):
    descricao = models.CharField(max_length=100, null=False)
    created_at = models.DateTimeField(auto_now_add=True, null=False)
    updated_at = models.DateTimeField(auto_now=True, null=False)
    chat_model = models.CharField(max_length=30, null=False)
    user = models.OneToOneField(
        User, related_name="profile", on_delete=models.CASCADE, null=True
    )
    conversa = models.ForeignKey(Conversa, on_delete=models.CASCADE, null=True)

    def __str__(self) -> str:
        return self.descricao


class Chat_provisionamento(models.Model):
    user = models.OneToOneField(
        User, related_name="profile", on_delete=models.CASCADE, null=True
    )
    sent = models.DateTimeField(auto_now_add=True, null=False)
    sistema = models.CharField(max_length=100, null=False)
    prompt = models.CharField(max_length=10000, null=False)
    chat_model = models.CharField(max_length=30, null=False)
    response = models.CharField(max_length=100000, null=False)
    preview = models.ForeignKey(Preview_provisionamento, on_delete=models.CASCADE, null=True)


class Chat_relatorio(models.Model):
    sistema = models.CharField(max_length=100, null=False)
    sent = models.DateTimeField(auto_now_add=True, null=False)
    user = models.OneToOneField(
        User, related_name="profile", on_delete=models.CASCADE, null=True
    )
    contrato = models.CharField(max_length=1000, null=False)
