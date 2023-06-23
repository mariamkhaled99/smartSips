
from django.contrib import admin
from django.urls import path,include
# from user_api.adapter import CustomSocialAccountAdapter
from user_api.views import login,GoogleLogin,home,google_callback,google_callback_logout
from allauth.socialaccount.providers.google.views import OAuth2LoginView
from dj_rest_auth.registration.views import ( SocialAccountListView, SocialAccountDisconnectView)
from drf_spectacular.views import SpectacularAPIView,SpectacularSwaggerView
from rest_framework.routers import DefaultRouter
from django.conf import settings
from django.conf.urls.static import static
from user_api.views import ImageUploadViewSet
from dj_rest_auth.views import PasswordResetView, PasswordResetConfirmView

from . import views


router=DefaultRouter()
# router.register('user_register',UserViewSet,basename='user_register')
router.register(r'imageupload', ImageUploadViewSet)
urlpatterns = [
    path('imageupload/<int:pk>/', include(router.urls)),
    path('admin/', admin.site.urls),
    # """ apps routes"""
    path('user_api/', include('user_api.urls')),
    path('chat_api/', include('chat_api.urls')),
    path('ml_api/', include('ml_api.urls')),
    path('iot_api/', include('iot_api.urls')),
    path('products_api/', include('products_api.urls')),
    path('order_api/', include('order_api.urls')),
    path('accounts/', include('allauth.urls')),
    # """ render templates at user_api routes"""
    path('login/',login,name="login"),
    path('home/',home,name="home"),
    # """default login and register and logout"""
    # path('dj-rest-auth/', include('dj_rest_auth.urls')),
    # path('dj-rest-auth/registration/', include('dj_rest_auth.registration.urls')),
    
    # """ social auth routes"""
    path('google/connect/', GoogleLogin.as_view(), name='google_connect'),
    path('accounts/google/login/', OAuth2LoginView, name='google_login'),
    path('accounts/google/login/callback/', google_callback, name='google_callback'),
    path('socialaccounts/',SocialAccountListView.as_view(), name='social_account_list'),
    path('google/logout/', google_callback_logout, name='google_callback_logout'),
    path('socialaccounts/<int:pk>/disconnect/',SocialAccountDisconnectView.as_view(),name='social_account_disconnect'),
    
    # """ swagger endpoints """
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('', SpectacularSwaggerView.as_view(url_name='schema')),
 
    path('password/reset/', PasswordResetView.as_view(), name='password_reset'),
    path('password/reset/confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('publish', views.publish_message, name='publish'),
    
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
# urlpatterns +=router.urls
urlpatterns +=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
    







 
  
