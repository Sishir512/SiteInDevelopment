from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.

STATUS = (
    (0,"Draft"),
    (1,"Publish")
)

class PublishingUser(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name

class BlogField(models.Model):
    
    title = models.CharField(max_length=200 , unique=True)
    slug = models.SlugField(max_length=200 , unique=True)
    author = models.ForeignKey(PublishingUser, on_delete= models.CASCADE , related_name='blog_posts')
    #manytomany = models.ManyToManyField(PublishingUser)
    #onetomany12 = models.OneToOneField(PublishingUser , on_delete=models.CASCADE,primary_key=True,default=1)
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title