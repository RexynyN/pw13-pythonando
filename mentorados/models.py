from datetime import timedelta
import secrets
from django.db import models
from django.contrib.auth.models import User 

# To create the database table for the Navigators model, run:
# py manage.py makemigrations

class Navigators(models.Model):
    nome = models.CharField(max_length=255) 
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome

# Create your models here.
class Mentorados(models.Model):
    estagio_choices = (
        ("E1", "10-100K"),
        ("E2", "100-1MM"),
    )

    nome = models.CharField(max_length=255)
    estagio = models.CharField(max_length=2, choices=estagio_choices)
    foto = models.ImageField(upload_to='fotos', null=True, blank=True)

    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)
    token = models.CharField(max_length=16, null=True, blank=True)

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    navigators = models.ForeignKey(Navigators, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.nome
    
    def save(self, *args, **kwargs):
        if not self.token: 
            self.token = self.gerar_token_unico()
        super().save(*args, **kwargs)

    def gerar_token_unico(self):
        while True:
            token = secrets.token_urlsafe(8)  
            if not Mentorados.objects.filter(token=token).exists():
                return token


class DisponibilidadeHorarios(models.Model):
    data_inicial = models.DateTimeField(null=True, blank=True)
    mentor = models.ForeignKey(User, on_delete=models.CASCADE)
    agendado = models.BooleanField(default=False)

    @property
    def data_final(self):
        return self.data_inicial + timedelta(minutes=50)
    
class Reuniao(models.Model):
    tag_choices = (
        ('G', 'Gestão'),
        ('M', 'Marketing'),
        ('RH', 'Gestão de pessoas'),
        ('I', 'Impostos')
    )

    data = models.ForeignKey(DisponibilidadeHorarios, on_delete=models.CASCADE)
    mentorado = models.ForeignKey(Mentorados, on_delete=models.CASCADE)
    tag = models.CharField(max_length=2, choices=tag_choices)
    descricao = models.TextField()








