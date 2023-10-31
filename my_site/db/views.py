from django.shortcuts import render, redirect
from requests import post
from .models import Articles, Persons, Deposites, ExchangeRates, Clients, DepositsRegistration
from .forms import ArticleForm, PersonsForm

# Create your views here.
def db_home(request):
    db = Articles.objects.all()
    db1 = Persons.objects.all()
    db2 = Deposites.objects.all()
    db3 = ExchangeRates.objects.all()
    db4 = Clients.objects.all()
    db5 = DepositsRegistration.objects.all()
    return render(request, 'db/db.html', {'db' : db, 'Persosns': db1, 'Deposites' : db2, 'ExchangeRates': db3, 'Clients': db4, 'DepositsRegistration': db5})

def create(request):
    error = ''
    if request.method == 'POST':
        formArticle = ArticleForm(request.post)
        formPersons = PersonsForm(request, post)
        if formArticle.is_valid():
            formArticle.save()
            formPersons.save()
            return redirect('')
        else:
            error = "форма была не верной"
    formPersons = PersonsForm()
    formArticle = ArticleForm()
    data = {
        'formArticle': formArticle,
        'formPersons': formPersons,
        'error': error 
    }
    return render(request, 'db/userAccount.html', data)
    
