from django.shortcuts import render
from django.views.generic import ListView , DetailView
from .models import BlogField
# Create your views here.


class BlogList(ListView):
    model = BlogField
    template_name = 'blog_list.html'
    
class BlogDetail(DetailView):
    model = BlogField
    template_name = 'blog.html'