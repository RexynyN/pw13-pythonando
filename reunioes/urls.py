from django.urls import path
from . import views

urlpatterns = [
    path('', views.reunioes, name='reunioes'),
]
