# Generated by Django 4.1.7 on 2023-05-12 21:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products_api', '0010_remove_wishlist_user_wishlist_wishlist_user_wishlist'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='qnt',
            field=models.IntegerField(default=1),
        ),
    ]
