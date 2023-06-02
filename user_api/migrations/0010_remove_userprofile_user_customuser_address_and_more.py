# Generated by Django 4.1.7 on 2023-05-09 19:21

from django.db import migrations, models
import user_api.models


class Migration(migrations.Migration):

    dependencies = [
        ('user_api', '0009_alter_customuser_user_permissions'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='user',
        ),
        migrations.AddField(
            model_name='customuser',
            name='address',
            field=models.CharField(default=' Elgalaa ST', max_length=150),
        ),
        migrations.AddField(
            model_name='customuser',
            name='city',
            field=models.CharField(default=' Tanta', max_length=150),
        ),
        migrations.AddField(
            model_name='customuser',
            name='company',
            field=models.CharField(default=' SmartSips', max_length=150),
        ),
        migrations.AddField(
            model_name='customuser',
            name='country',
            field=models.CharField(default=' Egypt', max_length=150),
        ),
        migrations.AddField(
            model_name='customuser',
            name='phone_number',
            field=models.CharField(blank=True, max_length=11, null=True, unique=True, validators=[user_api.models.validate_phone_number]),
        ),
        migrations.AddField(
            model_name='customuser',
            name='profile_photo',
            field=models.ImageField(default='upload_to/default.png', upload_to='upload_to'),
        ),
        migrations.DeleteModel(
            name='AdminProfile',
        ),
        migrations.DeleteModel(
            name='UserProfile',
        ),
    ]