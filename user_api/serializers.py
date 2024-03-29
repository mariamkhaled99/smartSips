from .models import CustomUser,Survey
from rest_framework import  serializers
from rest_framework.exceptions import AuthenticationFailed
from django.contrib.auth import authenticate
from django.db import transaction
from rest_framework import serializers
from dj_rest_auth.registration.serializers import RegisterSerializer
from dj_rest_auth.serializers import LoginSerializer
from django.utils import timezone
from rest_framework.response import Response
from rest_framework import serializers

# AdminProfile,UserProfile,
# ---------------------------------sign up -------------------------------------------------------------------------------
# class UserSerializer(serializers.ModelSerializer):  
#     class Meta:
#         model = CustomUser
#         fields = ['id','username','email','password', 'is_normal','is_patient','is_farmer','created_at' ]
        
#     def create(self, val_data):
        
#         user=CustomUser(
#             username=val_data['username'],
#             email=val_data['email'],
#             is_normal=val_data['is_normal'],
#             is_patient=val_data['is_patient'],
#             is_farmer=val_data['is_farmer'],  
            
#         )
#         user.set_password(val_data['password'])
#         user.save()
        
#         return user

class CustomRegisterSerializer(RegisterSerializer):
    # id=serializers.PrimaryKeyRelatedField()
    email = serializers.EmailField()
    username = serializers.CharField(max_length=150)
    password= serializers.CharField(max_length=20)
    created_at = serializers.DateTimeField(default=timezone.now)
    is_normal = serializers.BooleanField(default=False)
    is_patient = serializers.BooleanField(default=False)
    is_farmer = serializers.BooleanField(default=False)

    # Define transaction.atomic to rollback the save operation in case of error
    @transaction.atomic
    def save(self, request):
        user = super().save(request)
        user.id=self.data.get('id')
        user.email = self.data.get('email')
        user.username = self.data.get('username')
        user.is_normal = self.data.get('is_normal')
        user.is_patient = self.data.get('is_patient')
        user.is_farmer = self.data.get('is_farmer')
        user.password = self.data.get('password')
        user.set_password(user.password)
        user.save()
        return user
    
    


class LoginSerializers(LoginSerializer):
    is_superuser = serializers.BooleanField()
    username = None
    class  Meta:
        model = CustomUser
        fields = ['username','id','email','is_superuser' ]
       
    

    def authenticate(self, **options):
        return authenticate(self.context["request"], **options)

    def validate(self, data):
        id = data.get('id')
        email = data.get('email')
        password = data.get('password')
        is_superuser=data.get('is_superuser')

        if email and password:
            user = authenticate(request=self.context.get('request'),
                                email=email, password=password)
            if not user:
                msg = 'Unable to log in with provided credentials.'
                raise serializers.ValidationError(msg, code='authorization')
        else:
            msg = 'Must include "email" and "password".'
            raise serializers.ValidationError(msg, code='authorization')

        data['user'] = user
        return data
    

            

class ImageUploadSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = CustomUser
        fields= (
            'id',
            'profile_photo'
        )

    
    
class UserProfileSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        min_length=8, max_length=68)
    email=serializers.EmailField()
    username= serializers.CharField(
        max_length=80)
    id=serializers.PrimaryKeyRelatedField(read_only=True)
   
    class Meta:
       model = CustomUser
       fields = ['id','phone_number','address','created_at','username','password','email','country' ]
    
    # def create(self, val_data):
    #     return get_user_model().objects.create_user(**val_data)
    def update(self,instance,val_data):
        '''update profile for User'''
        password=val_data.pop('password',None)
        user=super().update(instance,val_data)
        if password :
            user.set_password(password)
            user.save()
        return user
    
    # serializers.ModelSerializer
class AdminProfileSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        min_length=8, max_length=68, write_only=True)
    email=serializers.EmailField()
    username= serializers.CharField(
        max_length=80, write_only=True)
    created_at=serializers.DateTimeField(read_only=True)
    class Meta:
       model = CustomUser
       fields = ['phone_number','address','country','created_at','city','company','username','password','email' ]
    
    
    def update(self,instance,val_data):
        '''update profile for Admin'''
        password=val_data.pop('password',None)
        user=super().update(instance,val_data)
        if password :
            user.set_password(password)
            user.save()
        return user


class SurveySerializer(serializers.ModelSerializer):  
    is_suffer_heart=serializers.BooleanField(default=False)
    is_suffer_kidney=serializers.BooleanField(default=False)
    class Meta:
        model = Survey
        fields = ['is_suffer_heart', 'is_suffer_kidney' ]
        def create(self,validated_data):
            
            
            return Survey.objects.create(**validated_data)
        
     
from dj_rest_auth.serializers import PasswordChangeSerializer

# class CustomPasswordChangeSerializer(PasswordChangeSerializer):
#     # Override methods here
#     pass


from django.core.exceptions import ObjectDoesNotExist


class CustomPasswordChangeSerializer(PasswordChangeSerializer):
    new_password2= serializers.CharField(
        min_length=8, max_length=68, write_only=True)
    new_password1= serializers.CharField(
        min_length=8, max_length=68, write_only=True)
    password = serializers.CharField(
        min_length=8, max_length=68, write_only=True)
    id=serializers.PrimaryKeyRelatedField(queryset=CustomUser.objects.all())

    class Meta:
        model = CustomUser
        fields = ['id','password']
        
  
        
    def validate(self, data):
        print(data)
        password = data.get('password')
        user_id = data.get('id')
        

        if isinstance(user_id, CustomUser):
            user_id = user_id.pk
        
        print(user_id)
        
        if user_id is None:
            raise serializers.ValidationError('The user ID is missing')
        try:
            user = CustomUser.objects.get(id=user_id)
        except ObjectDoesNotExist:
            raise serializers.ValidationError('The user does not exist')
        user.set_password(password)
        user.save()
        return data
    
    
    def save(self, **kwargs):
        # get the validated data from the serializer
        validated_data = dict(
                list(self.validated_data.items()) +
                list(kwargs.items())
            )

            # update the model instance with the validated data
        instance = self.instance

        for attr, value in validated_data.items():
                setattr(instance, attr, value)

        if instance is None:
            pass
        else:
            instance.save()

        return instance


class ResetPasswordEmailRequestSerializer(serializers.Serializer):
    email = serializers.EmailField(min_length=2)

    class Meta:
        model = CustomUser
        fields = ["email"]
    

        

 
        
class UpdateAdminProfileSerializer(serializers.ModelSerializer):
    adminProfile = AdminProfileSerializer()
    class Meta:
        model = CustomUser
        fields = ['id','username','password','email' ]

    def update(self, instance, validated_data):
        # We try to get profile data
        profile_data = validated_data.pop('adminProfile', None)
        # If we have one
        if profile_data is not None:
            # We set fields, 
            # if you provide profile
            instance.adminProfile.address = profile_data['address']
            instance.adminProfile.country = profile_data['country']
            instance.adminProfile.city = profile_data['city']
            instance.adminProfile.company = profile_data['company']
            instance.adminProfile.phone_number = profile_data['phone_number']
            instance.adminProfile.profile_photo= profile_data['profile_photo']
            # And save profile
            instance.adminProfile.save()
        # Rest will be handled by DRF
        return super().update(instance, validated_data)
    
    
    
class UpdateUserProfileSerializer(serializers.ModelSerializer):
    userProfile = UserProfileSerializer()
    
    class Meta:
        model = CustomUser
        fields = ['id','username','password','email' ]

    def update(self, instance, validated_data):
        # We try to get profile data
        profile_data = validated_data.pop('userProfile', None)
        # If we have one
        if profile_data is not None:
            # We set address, assuming that you always set address
            # if you provide profile
            instance.userProfile.address = profile_data['address']
            instance.userProfile.country = profile_data['country']
            instance.userProfile.phone_number = profile_data['phone_number']
            instance.userProfile.profile_photo = profile_data['profile_photo']
            # And save profile
            instance.userProfile.save()
        # Rest will be handled by DRF
        return super().update(instance, validated_data)
    
    

