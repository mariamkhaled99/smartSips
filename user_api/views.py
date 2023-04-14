from django.shortcuts import render
from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from allauth.socialaccount.providers.oauth2.client import OAuth2Client
from dj_rest_auth.registration.views import SocialLoginView
from django.urls import reverse
from django.shortcuts import redirect
import urllib.parse
# 
from .models import CustomUser,AdminProfile,UserProfile 
from .serializers import CustomRegisterSerializer,UpdateUserProfileSerializer,UserProfileSerializer,AdminProfileSerializer,SurveySerializer,SetNewPasswordSerializer,UpdateAdminProfileSerializer
from rest_framework.response import Response
from rest_framework import viewsets, status, generics, permissions
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework import serializers
from rest_framework.permissions import IsAdminUser,AllowAny,IsAuthenticated,BasePermission

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
    return redirect(f'http://127.0.0.1:8000/home/{params}')

def google_callback_logout(request):
    request.session.flush()
    return redirect(f'http://127.0.0.1:8000/login/')

# class update admin custom permissions
class AdminProfileUpdate(BasePermission):
    message="editing admin profile isrestricted to admin only"


# for custom get list of sign up

class CustomUserViewSet(generics.ListAPIView):
    queryset=CustomUser.objects.all()
    serializer_class=CustomRegisterSerializer
    # 


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
  

class AdminProfileList(generics.ListCreateAPIView):
    queryset=AdminProfile.objects.all()
    serializer_class=AdminProfileSerializer



class UpdateUserProfileList(generics.ListAPIView):
    queryset=UserProfile.objects.all()
    serializer_class=UserProfileSerializer
    
   