from django.urls import path,include
from .views import SurveyList,CustomLoginViewSet,SetNewPasswordUpdate,UserProfileUpdate,CustomUserViewSet,AdminProfileList,AdminProfileUpdate,UpdateUserProfileList

app_name='user_api'

urlpatterns = [
 
    # #show all product
    path('signup/',CustomUserViewSet.as_view(),name='signup'),
    # for register 
    path('auth/registration/', include('dj_rest_auth.registration.urls')),
    # for most of end point included in auth 
    path('auth/', include('dj_rest_auth.urls')),
    
  
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
    # path('<int:pk>/adminprofile/updatetest',AdminProfileList.as_view(),name='adminprofileupdate'),
    
    
    
    
    
    ]
   