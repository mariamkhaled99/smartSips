# Generated by Django 4.1.7 on 2023-04-09 12:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('description', models.TextField(null=True)),
                ('published', models.DateTimeField(default=django.utils.timezone.now)),
                ('price', models.IntegerField()),
                ('sales', models.IntegerField(default=0)),
                ('stock', models.IntegerField(default=30)),
                ('image', models.ImageField(default='products/default.jpg', upload_to='upload_to')),
                ('category', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='products_api.category')),
                ('user', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-published',),
            },
        ),
    ]
