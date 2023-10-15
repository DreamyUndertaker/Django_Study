
from ast import main
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index)
]