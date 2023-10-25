from django.shortcuts import render
from .models import Articles

# Create your views here.
def db_home(request):
    db = Articles.objects.all()
    return render(request, 'db/db.html', {'db' : db})
    
