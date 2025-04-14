from django.urls import path
from . import views

urlpatterns = [
    path('', views.mentorados, name='mentorados'),
    path('auth/', views.auth, name="auth_mentorado"),
]
