from django.db import models

# Create your models here.
class Articles(models.Model):
    title = models.CharField('название', max_length=50)
    full_text = models.TextField('содержание')
    category = models.Field.choices = [
        ('зеленый'),
        ('синий')
    ]
    def __str__(self):
        return f'Заявка: {self.title}'
    
    class Meta:
        verbose_name = 'заявка'
        verbose_name_plural = 'заявок'