from django.shortcuts import render
from django.views.generic import ListView , DetailView
from .models import BlogField , BlogComment
from .forms import CommentForm
# Create your views here.


class BlogList(ListView):
    model = BlogField
    template_name = 'blog_list.html'
    
class BlogDetail(DetailView):
    model = BlogField
    template_name = 'blog.html'

    def get_context_data(self , **kwargs):
        data = super().get_context_data(**kwargs)
        connected_comments = BlogComment.objects.filter(CommentPost=self.get_object())
        data['comments'] = connected_comments
        data['comment_form'] = CommentForm()
        return data
    
    def post(self , request , *args , **kwargs):
        comment_form = CommentForm(self.request.POST)
        if comment_form.is_valid():
            content = comment_form.cleaned_data['content']
        new_comment = BlogComment(content=content , author = self.request.user , CommentPost=self.get_object())
        new_comment.save()
        return self.get(request , *args , **kwargs)
    

