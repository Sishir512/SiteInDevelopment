from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
   path('', views.Video.as_view() , name = 'Video'),
    path('results/',views.VideoSearch.as_view() , name='search_result') ,
    path('category/<slug>' , views.VideoCategory.as_view() , name = 'video_category'),
]
    