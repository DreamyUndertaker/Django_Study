from django.urls import path
from . import views

urlpatterns = [
    path('', views.db_home, 'main/home.html', name = 'db_home')
]