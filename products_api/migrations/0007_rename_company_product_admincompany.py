# Generated by Django 4.1.7 on 2023-04-29 20:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products_api', '0006_product_company'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='company',
            new_name='admincompany',
        ),
    ]
