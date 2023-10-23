from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'main/home.html')

def registration(request):
    return render(request, 'main/registration.html')

def signin(request):
    return render(request, 'main/signin.html')

def userAccount(request):
    return render(request, 'main/userAccount.html')