from django.db import models

# Create your models here.
class orders(models.Model):
    customer = models.CharField('ФИО покупателя', max_length=100)
    tarif = models.CharField('Тариф', max_length=100, null=True, blank=True)
    phone = models.CharField('Телефон', max_length=12)
    email = models.EmailField('Email')

    def __str__(self):
        return str(self.price)