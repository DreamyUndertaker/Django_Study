from .models import Articles, Deposites, Persons
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

class PersonsForm(ModelForm):
    class Meta:
        model = Persons
        fields = ['surnamePersons', 'namePersons', 'fatherNamePersons', 'jobTitlePersons', 'salaryPersons']
        widgets = {
            'surnamePersons': TextInput(attrs={
                # 'class': 'abouRequest',
                'placeholder': 'Фамилия работника'
            }),
            'namePersons': TextInput(attrs={
                # 'class': 'aboutRequest',
                'placeholder': 'Имя работника'
            }),
            'fatherNamePersons': TextInput(attrs={
                # 'class': 'abouRequest',
                'placeholder': 'Фамилия работника'
            }),
            'jobTitlePersons': TextInput(attrs={
                # 'class': 'aboutRequest',
                'placeholder': 'Должность работника'
            }),
            'salaryPersons': TextInput(attrs={
                # 'class': 'aboutRequest',
                'placeholder': 'ЗП работника'
            }),

        }
class DepositesForm(ModelForm):
    class Meta:
        model = Deposites
        fields = ['depositeCode', 'depositeName', 'minDepositePeriod', 'minDepositeValue', 'currencyCode', 'interestRate']
        widgets = {
            'depositeCode': TextInput(attrs={
                'placeholder': 'код вклада'
            }),
            'depositeName': TextInput(attrs={
                'placeholder': 'наименование депозита'
            }), 
            'minDepositePeriod': TextInput(attrs={
                'placeholder': 'минимальный срок вклада'
            }),
            'minDepositeValue': TextInput(attrs={
                'placeholder': 'минимальная сумма вклада'
            }),
            'currencyCode': TextInput(attrs={
                'placeholder': 'код валюты'
            }),
            'interestRate': TextInput(attrs={
                'placeholder': 'процентная ставка, годовая'
            })
        }