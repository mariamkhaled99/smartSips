# Generated by Django 4.1.7 on 2023-05-27 14:44

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order_api', '0026_alter_cart_delivery_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='order_item',
        ),
        migrations.AlterField(
            model_name='cart',
            name='delivery_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 5, 30, 17, 44, 28, 667965)),
        ),
    ]