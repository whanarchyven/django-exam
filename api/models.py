from django.db import models
from simple_history.models import HistoricalRecords
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

def validate_lvl(value):
    if value <= 0:
        raise ValidationError(
            _('%(value)s Уровень не должен быть отрицательным'),
            params={'value': value},
)   


class Partners(models.Model):
    organization = models.CharField(verbose_name='Название', max_length=25)
    addres_p = models.TextField(verbose_name='Адрес ресторана')
    price = models.FloatField(verbose_name='Средний чек')
    employer = models.TimeField(verbose_name='Работает до')

    history = HistoricalRecords()

    def __str__(self):
        return self.organization

    class Meta:
        verbose_name = 'Ресторан'
        verbose_name_plural = 'Рестораны'
        
class Client(models.Model):
    name = models.CharField(verbose_name='Имя', max_length=25)
    address = models.CharField(verbose_name='Адрес', max_length=250)
    amount = models.IntegerField(verbose_name='Количество заказов')
    money_spend = models.FloatField(verbose_name='Денег потрачено')
    favorite_partner = models.ManyToManyField(Partners,verbose_name='Любимый ресторан')
    level = models.IntegerField(verbose_name='Уровень клиента', validators=[validate_lvl])
    

    history = HistoricalRecords()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'


class Order(models.Model):
    client = models.ManyToManyField(Client,verbose_name='Заказчик')
    partner = models.ManyToManyField(Partners,verbose_name='Ресторан')
    food = models.TextField(verbose_name='Меню заказа')
    price = models.FloatField(verbose_name='Чек')

    history = HistoricalRecords()

    # def __str__(self):
    #     return self.price

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'