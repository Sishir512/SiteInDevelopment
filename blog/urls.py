from django.contrib import admin
from django.urls import path
from .views import BlogList , BlogDetail

urlpatterns = [
    path('', BlogList.as_view() , name = 'BlogList'),
    path('<slug:slug>' , BlogDetail.as_view() , name = 'BlogDetail')
]
