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

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    navigators = models.ForeignKey(Navigators, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.nome
    











