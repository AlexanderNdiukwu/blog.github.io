from django.urls import path 
from . import views 
from django.conf import settings 
from django.conf.urls.static import static
    
from django.urls import path
from django.contrib.auth import views as auth_views



urlpatterns = [
    path('', views.landingpage ,name='landingpage'),
    path('home/', views.index ,name='home'),
    path('about/', views.about ,name='about'),
    path('profile/', views.profile_pic ,name='profile'),
    path('register/', views.register ,name='register'),
    path('login/', views.login_user ,name='login'),
    path('logout/', views.logout_user ,name='logout'),
    path('blog/', views.blog ,name='create_blog'),
    path('delete/<int:pk>/', views.delete_blog, name='delete'),
    path('edit/<int:pk>/', views.edit_blog, name='edit'),
    # this is the email reset password
      path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset_done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),

 ]+static( settings.MEDIA_URL , document_root = settings.MEDIA_ROOT)

