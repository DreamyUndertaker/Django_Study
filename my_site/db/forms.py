from .models import Articles
from django.forms import ModelForm, TextInput

class ArticleForm(ModelForm):
    class Meta:
        model = Articles
        fields = ['title', 'full_text']

        widgets = {
            'title': TextInput(attrs={
                'class': 'nameRequest',
                'placeholder': 'навзание жалобы'
            }),
            'full_text': TextInput(attrs={
                'class': 'aboutRequest',
                'placeholder': 'описание жалобы'
            }),
        }