# Generated by Django 4.1.7 on 2023-04-13 20:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_api', '0003_customuser_is_suffer_heart_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='username',
            field=models.CharField(max_length=150),
        ),
    ]