from django.shortcuts import render
from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from allauth.socialaccount.providers.oauth2.client import OAuth2Client
from dj_rest_auth.registration.views import SocialLoginView
from django.urls import reverse
from django.shortcuts import redirect
import urllib.parse
# UpdateUserProfileSerializer,,AdminProfile,UserProfile 
from .models import CustomUser
from .serializers import LoginSerializers,CustomRegisterSerializer,UserProfileSerializer,AdminProfileSerializer,SurveySerializer,SetNewPasswordSerializer,UpdateAdminProfileSerializer
from rest_framework.response import Response
from rest_framework import viewsets, status, generics, permissions
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework import serializers
from rest_framework.permissions import IsAdminUser,AllowAny,IsAuthenticated,BasePermission
import json
from dj_rest_auth.registration.serializers import (
    SocialAccountSerializer, SocialConnectSerializer, SocialLoginSerializer
)

# Create your views here.

def login(request):
    """login page"""
    return render(request, 'core/login.html')

def home(request):
    """home page"""
    return render(request, 'core/home.html')


 
    
"""url in google cloud api for callback"""
url = "http://127.0.0.1:8000/google/login/callback/"

class GoogleLogin(SocialLoginView): # if you want to use Authorization Code Grant, use this
    adapter_class = GoogleOAuth2Adapter
    client_class = OAuth2Client
    @property
    def callback_url(self):
        return self.request.build_absolute_uri(reverse('google_login'))



def google_callback(request):
    params = urllib.parse.urlencode(request.GET)
    return redirect(f'http://localhost:8000/google/home/{params}')
    # return redirect(f'https://smartsips-production.up.railway.app/home/{params}')

def google_callback_logout(request):
    request.session.flush()
    return redirect(f'http://localhost:8000/google/login/')
    # return redirect(f'https://smartsips-production.up.railway.app/login/')

# class update admin custom permissions
# class AdminProfileUpdate(BasePermission):
#     message="editing admin profile isrestricted to admin only"



from .serializers import ImageUploadSerializer

class ImageUploadViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = ImageUploadSerializer
    permission_classes = [AllowAny]
    lookup_field = 'pk'
    def get_queryset(self):
            
        # current_user = self.request.user.id
        # print(current_user)
        id =self.kwargs.get(self.lookup_field)

        # Here you can do the following thing:
        

        # And use it as you wish in the filtering below:

        return CustomUser.objects.filter(id=id)

# for custom get list of sign up

class CustomUserViewSet(generics.ListAPIView):
    queryset=CustomUser.objects.all()
    serializer_class=CustomRegisterSerializer
  


# for fill survey

class SurveyList(generics.UpdateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = SurveySerializer
    permission_classes = [AllowAny]
    lookup_field = 'pk'

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response({"message": " survey updated successfully"})

        else:
            return Response({"message": "failed", "details": serializer.errors})






    
# #used to update password  table  
class SetNewPasswordUpdate(generics.UpdateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = SetNewPasswordSerializer
    lookup_field = 'pk'
    permission_classes = [AllowAny]

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response({"message": " password updated successfully"})

        else:
            return Response({"message": "failed", "details": serializer.errors})

    
# #used to update some fields inside UserProfile table  
class UserProfileUpdate(generics.UpdateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserProfileSerializer
    lookup_field = 'pk'
    permission_classes = [AllowAny]

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response({"message": "user profile updated successfully"})

        else:
            return Response({"message": "failed", "details": serializer.errors})
        
        
        
# #used to update some fields inside AdminProfile table  
class AdminProfileUpdate(generics.UpdateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = AdminProfileSerializer
    lookup_field = 'pk'
    permission_classes = [AllowAny]
    # permission_classes = [IsAdminUser]

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response({"message": "admin profile updated successfully"})

        else:
            return Response({"message": "failed", "details": serializer.errors})
  

class AdminProfileList(generics.ListAPIView):
    queryset=admins = CustomUser.objects.filter(is_superuser=True)
    serializer_class=AdminProfileSerializer
    permission_classes = [AllowAny]


class UpdateUserProfileList(generics.ListAPIView):
    queryset=admins = CustomUser.objects.filter(is_superuser=False)
    serializer_class=UserProfileSerializer
    permission_classes = [AllowAny]
    

# class CreateUserProfileList(generics.CreateAPIView):
#     queryset=CustomUser.objects.all()
#     serializer_class=UserProfileSerializer
#     permission_classes = [AllowAny]
#     lookup_field = 'pk'
    
class DeleteUserProfileList(generics.DestroyAPIView):
    queryset=CustomUser.objects.all()
    serializer_class=UserProfileSerializer
    permission_classes = [AllowAny]
    lookup_field = 'pk'
    
class CustomLoginViewSet(generics.GenericAPIView):
    queryset = CustomUser.objects.all()
    serializer_class=LoginSerializers
    
    
    # def get_serializer_class(self):
    #     if self.request.user.is_superuser:
            
            
    #         return AdminProfileSerializer
    #     return UserProfileSerializer
    
    def post(self, request):
        serializer = self.serializer_class(data=request.data)

        email = request.data.get('email', '')
        if CustomUser.objects.filter(email=email).exists():
                
                user = CustomUser.objects.get(email=email)
                id = user.id
                is_superuser=user.is_superuser

                return Response({"message": "user login successfully",
            
  "user": {
    "is_superuser": is_superuser,
    "pk":  id,
    "email":  email}})

        else:
            return Response({"message": "failed", "details": serializer.errors})
        


            
          
class LoginList(generics.ListAPIView):
    queryset=CustomUser.objects.all()
    serializer_class=LoginSerializers
    permission_classes = [AllowAny]
    
    
    



class UserProfileOne(generics.ListAPIView):
    # queryset = CustomUser.objects.filter(id=id)
    serializer_class = UserProfileSerializer
    lookup_field = 'pk'
    def get_queryset(self):
            
        # current_user = self.request.user.id
        # print(current_user)
        id =self.kwargs.get(self.lookup_field)

        # Here you can do the following thing:
        

        # And use it as you wish in the filtering below:

        return CustomUser.objects.filter(id=id)