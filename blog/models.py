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

 