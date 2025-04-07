from django.shortcuts import render
from django.http import HttpResponse


# Create your models here.
def cadastro(request):
    return render(request, 'cadastro.html')