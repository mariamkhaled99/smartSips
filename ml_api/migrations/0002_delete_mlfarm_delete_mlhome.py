# Generated by Django 4.1.7 on 2023-06-21 20:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ml_api', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='MlFarm',
        ),
        migrations.DeleteModel(
            name='MlHome',
        ),
    ]
