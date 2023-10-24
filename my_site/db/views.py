from django.shortcuts import render


# Create your views here.
def db(request):
    return render(request, 'main/db.html')