# Generated by Django 3.1.4 on 2021-01-12 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_auto_20210112_1925'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='expense',
            field=models.IntegerField(default=0, verbose_name='Произведено процессоров (тыс.шт)'),
        ),
        migrations.AlterField(
            model_name='report',
            name='profit',
            field=models.IntegerField(default=0, verbose_name='Продано процессоров (тыс.шт)'),
        ),
    ]