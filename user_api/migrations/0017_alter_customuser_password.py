# Generated by Django 4.1.7 on 2023-05-21 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_api', '0016_customuser_social_account'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='password',
            field=models.CharField(max_length=20, null=True),
        ),
    ]