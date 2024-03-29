# Generated by Django 4.1.7 on 2023-05-13 11:27

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order_api', '0011_alter_order_unique_together_cart_order_item_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='delivery_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 5, 16, 14, 27, 0, 226462)),
        ),
        migrations.AlterField(
            model_name='cart',
            name='order_item',
            field=models.ManyToManyField(blank=True, related_name='items', to='order_api.order'),
        ),
    ]
