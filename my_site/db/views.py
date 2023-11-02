from django.shortcuts import render, redirect
from .models import Articles, Persons, Deposites, ExchangeRates, Clients, DepositsRegistration
from .forms import ArticleForm, DepositesForm, PersonsForm

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
        formArticle = ArticleForm(request.POST)
        formPersons = PersonsForm(request.POST)
        formDeposites = DepositesForm(request.POST)
        if formArticle.is_valid():
            formArticle.save()
            formPersons.save()
            formDeposites.save()
            return redirect('')
        else:
            error = "форма была не верной"
    formPersons = PersonsForm()
    formArticle = ArticleForm()
    formDeposites = DepositesForm()
    data = {
        'formArticle': formArticle,
        'formPersons': formPersons,
        'fomrDeposites': formDeposites,
        'error': error 
    }
    return render(request, 'db/userAccount.html', data)
    
