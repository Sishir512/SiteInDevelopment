from django.contrib import admin
from django.urls import path,include,re_path
from . import views

urlpatterns = [
    path('',views.signup,name='SignUp'),
    path('logout/',views.logout , name='LogOut'),
    path('activate/<slug:uidb64>/<slug:token>/',views.activate, name='activate'),
]
