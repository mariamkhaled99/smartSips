# Generated by Django 4.1.7 on 2023-05-13 00:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order_api', '0005_alter_cart_delivery_date_alter_order_item'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='cart',
        ),
        migrations.DeleteModel(
            name='Cart',
        ),
    ]