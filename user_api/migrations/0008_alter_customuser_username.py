# Generated by Django 4.1.7 on 2023-04-14 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_api', '0007_customuser_groups_customuser_is_superuser_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='username',
            field=models.CharField(max_length=150, null=True),
        ),
    ]