# Generated by Django 4.1.7 on 2023-05-13 00:34

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products_api', '0012_remove_product_qnt'),
        ('order_api', '0004_alter_order_unique_together_alter_cart_delivery_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='delivery_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 5, 16, 3, 34, 0, 755533)),
        ),
        migrations.AlterField(
            model_name='order',
            name='item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='products_api.product'),
        ),
    ]
