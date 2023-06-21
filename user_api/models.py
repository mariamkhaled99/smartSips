
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.core.exceptions import ValidationError
import re
from allauth.socialaccount.models import SocialAccount
from django.contrib.auth.models import Permission


class CustomAccountManager(BaseUserManager):
    
    def create_superuser(self, email, username, password,social_account=None,**other_fields):

        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)
        other_fields.setdefault('address', ' Elgalaa ST')
        other_fields.setdefault('country', 'Egypt')
        other_fields.setdefault('phone_number', "+00000000000")
        other_fields.setdefault('profile_photo', 'upload_to/default.png')
        other_fields.setdefault('city', 'Tanta')
        other_fields.setdefault('company', ' SmartSips')
       
   

       

        if other_fields.get('is_staff') is not True:
            raise ValueError(
                'Superuser must be assigned to is_staff=True.')
        if other_fields.get('is_superuser') is not True:
            raise ValueError(
                'Superuser must be assigned to is_superuser=True.')

        return self.create_user(email, username, password,social_account, **other_fields)

    def create_user(self, email, username, password,social_account, **other_fields):
            
             
        if not email:
            raise ValueError(_('You must provide an email address'))

        email = self.normalize_email(email)
        user = self.model(email=email, username=username,password=None,social_account=None,**other_fields)
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_normal', False)
        other_fields.setdefault('is_patient', False)
        other_fields.setdefault('is_farmer', False)
        other_fields.setdefault('is_superuser', False)
        other_fields.setdefault('is_suffer_heart', False)
        other_fields.setdefault('is_suffer_kidney', False)
        other_fields.setdefault('address', ' Elgalaa ST')
        other_fields.setdefault('country', 'Egypt')
        other_fields.setdefault('phone_number', "01000000000")
        other_fields.setdefault('profile_photo', 'upload_to/default.jpg')
        user.set_password(password)
        user.save(using=self._db)
        # Populate the social account data
        social_account = SocialAccount.objects.filter(user=user).first()
        if social_account:
            # Update the user instance with data from the social account
            # user.first_name = social_account.extra_data.get('first_name', '')
            # user.last_name = social_account.extra_data.get('last_name', '')
            user.email = social_account.extra_data.get('email', '')
            user.username = social_account.extra_data.get('username', '')
            user.save()
        return user

def upload_to(instance,filename):
    return 'users_api/{filename}'.format(filename=filename)

def validate_phone_number(value):
    if not re.match(r"^01[0125]{1}", value):
        raise ValidationError("Phone number must start with 010 or 011 or 012 or 015")

    if not re.match(r"^\d{11}$", value):
        raise ValidationError("Phone number must be 11 numbers")

class CustomUser(AbstractBaseUser, PermissionsMixin):
    social_account= models.ForeignKey(SocialAccount, on_delete=models.CASCADE,null=True, blank=True, related_name='usersocial')
    email = models.EmailField(_('email address'), unique=True)
    username = models.CharField(max_length=150,null=True)
    password= models.CharField(max_length=20,null=True)
    created_at = models.DateTimeField(default=timezone.now)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_normal = models.BooleanField(default=False)
    is_patient = models.BooleanField(default=False)
    is_farmer = models.BooleanField(default=False)
    address=models.CharField(max_length=150,default=' Elgalaa ST')
    country=models.CharField(max_length=150,default=' Egypt')
    phone_number=models.CharField(unique=False, null=True, blank=True, max_length=11, validators=[validate_phone_number])
    profile_photo=models.ImageField(upload_to='upload_to', default='upload_to/default.jpg')
    city=models.CharField(max_length=150,default=' Tanta')
    company=models.CharField(max_length=150,default=' SmartSips')
   
    
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name=_('user permissions'),
        blank=True,
        help_text=_('Specific permissions for this user.'),
        related_name="+",
    )
   

    objects = CustomAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    class Meta:
        ordering = ('-username',)
    

    def __str__(self):
        return self.username
    


class Survey(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    is_suffer_heart=models.BooleanField(default=False)
    is_suffer_kidney=models.BooleanField(default=False)
    
    def __str__(self):
        return self.user.username

# admins = CustomUser.objects.filter(is_superuser=True)

    
    
        
        
    
    
# class device(models.Model):
#     user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
# name=
# status=
# location=models.CharField(max_length=150,default='45 Potress ST')
# dashboard
    