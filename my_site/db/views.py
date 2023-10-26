from django.shortcuts import render, redirect
from .models import Articles
from .forms import ArticleForm

# Create your views here.
def db_home(request):
    db = Articles.objects.all()
    return render(request, 'db/db.html', {'db' : db})

def create(request):
    error = ''
    if request.method == 'POST':
        form = ArticleForm(request.post)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = "форма была не верной"

    form = ArticleForm()
    data = {
        'form': form,
        'error': error 
    }
    return render(request, 'db/userAccount.html', data, error)
    
