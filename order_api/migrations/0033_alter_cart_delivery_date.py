# Generated by Django 4.1.7 on 2023-06-02 14:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order_api', '0032_remove_order_item_order_product_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='delivery_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 6, 5, 17, 9, 16, 470985)),
        ),
    ]
