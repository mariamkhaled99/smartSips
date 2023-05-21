# Generated by Django 4.1.7 on 2023-05-18 19:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('socialaccount', '0003_extra_data_default_dict'),
        ('user_api', '0015_remove_customuser_social_account'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='social_account',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='usersocial', to='socialaccount.socialaccount'),
        ),
    ]
