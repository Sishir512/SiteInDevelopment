from django.shortcuts import render,redirect
from .models import VideoContent
from django.views.generic import ListView
from django.db.models import Q
from django.views.generic.detail import SingleObjectMixin
# Create your views here.

'''def video(request):
    datas = VideoContent.objects.all()
    return render(request , 'video.html',{'datas':datas})
'''
    
class Video(ListView):
    model = VideoContent
    template_name = 'video_search.html'
    paginate_by = 1

class VideoSearch(ListView):
    model = VideoContent
    template_name = 'video_search.html'


    def get_queryset(self):
        data_list = VideoContent.objects.all()
        query = self.request.GET.get('query')
        print('Query is ' , query)
        if query is not None:
            data_list = VideoContent.objects.filter(
                Q(title__icontains = query)
            )
        return data_list



class VideoCategory(ListView):
    model = VideoContent
    template_name = 'video_search.html'
    
    
    def get_queryset(self):
        query = self.kwargs['slug']
        print('Query is ' , query)
        data_list = VideoContent.objects.filter(category__name=query)
        return data_list
