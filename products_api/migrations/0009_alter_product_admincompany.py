# Generated by Django 4.1.7 on 2023-05-02 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products_api', '0008_alter_product_admincompany'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='admincompany',
            field=models.CharField(max_length=250),
        ),
    ]
