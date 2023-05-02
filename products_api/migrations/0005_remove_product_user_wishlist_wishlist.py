# Generated by Django 4.1.7 on 2023-04-28 18:03

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('products_api', '0004_remove_product_user_product_user_wishlist'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='user_wishlist',
        ),
        migrations.CreateModel(
            name='Wishlist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.ManyToManyField(blank=True, related_name='user', to='products_api.product')),
                ('user_wishlist', models.ManyToManyField(blank=True, related_name='user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]