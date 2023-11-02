# Generated by Django 4.2.5 on 2023-11-02 23:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0002_clients_deposites_depositsregistration_exchangerates_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='clients',
            options={'verbose_name': 'Клиенты банка', 'verbose_name_plural': 'Клиентов банка'},
        ),
        migrations.AlterModelOptions(
            name='deposites',
            options={'verbose_name': 'Виды вкладов', 'verbose_name_plural': 'Виды вкладов'},
        ),
        migrations.AlterModelOptions(
            name='depositsregistration',
            options={'verbose_name': 'Регистрация вкладов', 'verbose_name_plural': 'Регистрация вкладов'},
        ),
        migrations.AlterModelOptions(
            name='exchangerates',
            options={'verbose_name': 'Обменный курс', 'verbose_name_plural': 'Обменный курс'},
        ),
        migrations.AlterModelOptions(
            name='persons',
            options={'verbose_name': 'Сотрудники банка', 'verbose_name_plural': 'Сострудников банка'},
        ),
        migrations.AlterField(
            model_name='persons',
            name='salaryPersons',
            field=models.PositiveBigIntegerField(verbose_name='Оклад'),
        ),
    ]
