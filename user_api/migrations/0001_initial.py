# Generated by Django 4.1.7 on 2023-04-11 17:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import user_api.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='email address')),
                ('username', models.CharField(max_length=150, unique=True)),
                ('password', models.CharField(max_length=20)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=False)),
                ('is_normal', models.BooleanField(default=False)),
                ('is_patient', models.BooleanField(default=False)),
                ('is_farmer', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'ordering': ('-username',),
            },
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(default=' Elgalaa ST', max_length=150)),
                ('country', models.CharField(default=' Egypt', max_length=150)),
                ('phone_number', models.CharField(blank=True, max_length=11, null=True, unique=True, validators=[user_api.models.validate_phone_number])),
                ('profile_photo', models.ImageField(default='upload_to/default.png', upload_to='upload_to')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Survey',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_suffer_heart', models.BooleanField(default=False)),
                ('is_suffer_kidney', models.BooleanField(default=False)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='AdminProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(default='45 Potress ST', max_length=150)),
                ('country', models.CharField(default=' Egypt', max_length=150)),
                ('city', models.CharField(default=' Tanta', max_length=150)),
                ('company', models.CharField(default=' SmartSips', max_length=150)),
                ('phone_number', models.CharField(blank=True, max_length=11, null=True, unique=True, validators=[user_api.models.validate_phone_number])),
                ('profile_photo', models.ImageField(default='upload_to/default.png', upload_to='upload_to')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]