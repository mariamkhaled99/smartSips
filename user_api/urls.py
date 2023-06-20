from django.urls import path,include
from .views import CustomPasswordChangeView,UserProfileOne,DeleteUserProfileList,LoginList,SurveyList,CustomLoginViewSet,UserProfileUpdate,CustomUserViewSet,AdminProfileList,AdminProfileUpdate,UpdateUserProfileList
# from dj_rest_auth.views import PasswordResetView, PasswordResetConfirmView


    # ...
   
# ,SetNewPasswordUpdate,CreateUserProfileList

app_name='user_api'

urlpatterns = [
    # path('password/reset/', PasswordResetView.as_view(), name='password_reset'),
    # path('password/reset/confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    # #show all product
    path('signup/',CustomUserViewSet.as_view(),name='signup'),
    # for register 
    path('auth/registration/', include('dj_rest_auth.registration.urls')),
    # for most of end point included in auth 
    path('auth/', include('dj_rest_auth.urls')),
    path('<int:pk>/userprofile/get',UserProfileOne.as_view(),name='userprofile_get'),
  
    #  edit admin profile
    path('<int:pk>/userprofile/update',UserProfileUpdate.as_view(),name='userprofile'),
    #  edit user profile
    path('<int:pk>/adminprofile/update',AdminProfileUpdate.as_view(),name='adminprofile'),
    # fill survey for user 
    path('<int:pk>/fillsurvey',SurveyList.as_view(),name='fill_survey'),
    # retrive admin data
    path('adminprofile/list',AdminProfileList.as_view(),name='adminprofilelist'),
    # retrive user data
    path('userprofile/list',UpdateUserProfileList.as_view(),name='userprofilelist'),
    path('customlogin/',CustomLoginViewSet.as_view(),name='customlogin'),
    path('loginlist/',LoginList.as_view(),name='loginlist'),
    path('userprofile/delete/<int:pk>',DeleteUserProfileList.as_view(),name='userprofiledelete'),
    path('password/change/<int:id>', CustomPasswordChangeView.as_view(), name='rest_password_change'),
    # path('reset/password/<int:pk>',ReSetNewPasswordUpdate.as_view(),name='reset-password'),
    # path('<int:pk>/adminprofile/updatetest',AdminProfileList.as_view(),name='adminprofileupdate'),
    
    
    
    
    
    ]
   