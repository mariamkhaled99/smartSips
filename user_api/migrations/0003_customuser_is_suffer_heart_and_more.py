# Generated by Django 4.1.7 on 2023-04-13 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_api', '0002_alter_customuser_is_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='is_suffer_heart',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='customuser',
            name='is_suffer_kidney',
            field=models.BooleanField(default=False),
        ),
        migrations.DeleteModel(
            name='Survey',
        ),
    ]