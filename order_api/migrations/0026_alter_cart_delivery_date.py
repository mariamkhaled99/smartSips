# Generated by Django 4.1.7 on 2023-05-21 19:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order_api', '0025_alter_cart_delivery_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='delivery_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 5, 24, 22, 15, 16, 365173)),
        ),
    ]
