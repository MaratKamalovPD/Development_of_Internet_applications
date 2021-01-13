from django.db import models

# Create your models here.
from django.db import models


class Processor(models.Model):
    name = models.CharField(max_length=20, verbose_name='Наименование')


    class Meta:
        verbose_name = 'Процессор'
        verbose_name_plural = 'Процессоры'

class Report(models.Model):
    processor_id = models.ForeignKey(Processor, on_delete=models.CASCADE, verbose_name='ID Процессора')
    year = models.IntegerField(default=0, verbose_name='Год')
    profit = models.IntegerField(default=0, verbose_name='Продано процессоров (тыс.шт)')
    expense = models.IntegerField(default=0, verbose_name='Произведено процессоров (тыс.шт)')


    class Meta:
        verbose_name = 'Отчет'
        verbose_name_plural = 'Отчеты'