from django.db import models
from django.contrib.auth import get_user_model
from ckeditor_uploader.fields import  RichTextUploadingField
# Create your models here.



class PublishingUser(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name

class BlogField(models.Model):
    display_image = models.ImageField(upload_to = 'pics' , null=True)
    title = models.CharField(max_length=200 , unique=True)
    slug = models.SlugField(max_length=200 , unique=True)
    author = models.ForeignKey(PublishingUser, on_delete= models.CASCADE , related_name='blog_posts')
    updated_on = models.DateTimeField(auto_now=True)
    description = models.TextField(null=True)
    content = RichTextUploadingField()
    created_on = models.DateTimeField(auto_now_add=True)
    time_to_read = models.IntegerField(default=2)
    

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title
    
    @property
    def datepublished(self):
        return self.created_on.strftime('%d %B %Y')   # %B = full month name , %d = Day , %Y = Year

    @property
    def number_of_comments(self):
        return BlogComment.objects.filter(CommentPost=self).count()

class BlogComment(models.Model):
    CommentPost = models.ForeignKey(BlogField , related_name='comments' , on_delete=models.CASCADE)
    author = models.ForeignKey(get_user_model() , on_delete=models.CASCADE)
    content = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)
    parent = models.ForeignKey('self' , null=True , blank=True , on_delete=models.CASCADE)

    class Meta:
        ordering=['-date_posted']

    def __str__(self):
        return str(self.author) + ' comment on ' + self.CommentPost.title[:30]
    
    @property
    def children(self):
        return BlogComment.objects.filter(parent=self)

    @property
    def is_parent(self):
        if self.parent is None:
            return True
        return False
    
    

 