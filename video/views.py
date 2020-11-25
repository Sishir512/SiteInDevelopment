from django.shortcuts import render,redirect
from .models import VideoContent
from django.views.generic import ListView
from django.db.models import Q
from django.views.generic.detail import SingleObjectMixin
# Create your views here.


class Video(ListView):
    model = VideoContent
    template_name = 'video_search.html'
    paginate_by = 1

class VideoSearch(ListView):
    model = VideoContent
    template_name = 'video_search.html'

    def get(self , request , *args , **kwargs):
        if request.GET.get('query') is None:
            return redirect('/video')
        else:
            return super().get(request , *args , **kwargs)
    def get_queryset(self):
        
        query = self.request.GET.get('query')
        
        if not query:
            return VideoContent.objects.none()
        
        if query is not None:
            return VideoContent.objects.filter(
                Q(title__icontains = query)
            )
        
        



class VideoCategory(ListView):
    model = VideoContent
    template_name = 'video_search.html'
    
    
    def get_queryset(self):
        query = self.kwargs['slug']
        print('Query is ' , query)
        data_list = VideoContent.objects.filter(category__name=query)
        return data_list
