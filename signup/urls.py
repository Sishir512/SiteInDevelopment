from django.contrib import admin
from django.urls import path,include,re_path
from . import views
from django.contrib.auth import views as password_views
urlpatterns = [
    path('',views.signup,name='signup'),
    path('logout/',views.logout , name='logout'),
    path('activate/<slug:uidb64>/<slug:token>/',views.activate, name='activate'),
    path('change-username' , views.change_username , name='ChangeUsername'),
        
    path('password_reset/done/', password_views.PasswordResetCompleteView.as_view(template_name='password_reset/password_reset_done.html'),name='password_reset_done'),

    path('reset/<uidb64>/<token>/', password_views.PasswordResetConfirmView.as_view(template_name='password_reset/password_reset_confirm.html'), name='password_reset_confirm'),
    path('password_reset/', password_views.PasswordResetView.as_view(template_name='password_reset/password_reset_form.html' , email_template_name = 'password_reset/password_reset_email.html'), name='password_reset'),
    
    path('reset/done/', password_views.PasswordResetCompleteView.as_view(template_name='password_reset/password_reset_complete.html'),name='password_reset_complete'),
]
