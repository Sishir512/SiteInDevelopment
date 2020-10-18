from django.shortcuts import render
from .models import VideoContent

# Create your views here.

def video(request):
    datas = VideoContent.objects.all()
    return render(request , 'video.html',{'datas':datas})