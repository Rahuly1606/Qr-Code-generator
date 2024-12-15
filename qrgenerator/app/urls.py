from django.urls import path
from . import views

urlpatterns = [
    path('', views.generate_qr, name='generate_qr'),
]
