from django.shortcuts import render


# Create your views here.
def db_home(request):
    return render(request, 'main/home.html')