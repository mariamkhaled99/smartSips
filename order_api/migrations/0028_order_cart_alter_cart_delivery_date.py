# Generated by Django 4.1.7 on 2023-05-27 14:48

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('order_api', '0027_remove_cart_order_item_alter_cart_delivery_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='cart',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='carts', to='order_api.cart'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='cart',
            name='delivery_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 5, 30, 17, 47, 17, 283506)),
        ),
    ]
