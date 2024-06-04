from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class Conversa(models.Model):
    sent = models.DateTimeField(auto_now_add=True, null=False)
    prompt = models.CharField(max_length=10000, null=False)
    response = models.CharField(max_length=100000, null=False)

    class Meta:
        ordering = ["sent"]

    def __str__(self):
        return f"Conversa at {self.sent} - {self.prompt[:50]}"

    def get_absolute_url(self):
        return reverse('conversa_detail', args=[str(self.id)])


class PreviewProvisionamento(models.Model):
    sent = models.DateTimeField(auto_now_add=True, null=False)
    prompt = models.CharField(max_length=10000, null=False)
    chat_model = models.CharField(max_length=30, null=False)
    response = models.CharField(max_length=100000, null=False)

    class Meta:
        ordering = ["sent"]

    def __str__(self):
        return f"Preview at {self.sent} - {self.prompt[:50]}"

    def get_absolute_url(self):
        return reverse('preview_provisionamento_detail', args=[str(self.id)])


class ChatDesenvolvedor(models.Model):
    descricao = models.CharField(max_length=100, null=False)
    created_at = models.DateTimeField(auto_now_add=True, null=False)
    updated_at = models.DateTimeField(auto_now=True, null=False)
    chat_model = models.CharField(max_length=30, null=False)
    user = models.OneToOneField(
        User, related_name="chat_desenvolvedor", on_delete=models.CASCADE, null=True
    )
    conversa = models.ForeignKey(Conversa, on_delete=models.CASCADE, null=True)

    class Meta:
        ordering = ["created_at"]

    def __str__(self):
        return f"Chat Desenvolvedor: {self.descricao}"

    def get_absolute_url(self):
        return reverse('chat_desenvolvedor_detail', args=[str(self.id)])


class ChatProvisionamento(models.Model):
    user = models.OneToOneField(
        User, related_name="chat_provisionamento", on_delete=models.CASCADE, null=True
    )
    sent = models.DateTimeField(auto_now_add=True, null=False)
    sistema = models.CharField(max_length=100, null=False)
    prompt = models.CharField(max_length=10000, null=False)
    chat_model = models.CharField(max_length=30, null=False)
    response = models.CharField(max_length=100000, null=False)
    preview = models.ForeignKey(
        PreviewProvisionamento, on_delete=models.CASCADE, null=True
    )

    class Meta:
        ordering = ["sent"]

    def __str__(self):
        return f"Chat Provisionamento: {self.sistema} at {self.sent}"

    def get_absolute_url(self):
        return reverse('chat_provisionamento_detail', args=[str(self.id)])


class ChatRelatorio(models.Model):
    sistema = models.CharField(max_length=100, null=False)
    sent = models.DateTimeField(auto_now_add=True, null=False)
    user = models.OneToOneField(
        User, related_name="chat_relatorio", on_delete=models.CASCADE, null=True
    )
    contrato = models.CharField(max_length=1000, null=False)

    class Meta:
        ordering = ["sent"]

    def __str__(self):
        return f"Chat Relatorio: {self.sistema} at {self.sent}"

    def get_absolute_url(self):
        return reverse('chat_relatorio_detail', args=[str(self.id)])
