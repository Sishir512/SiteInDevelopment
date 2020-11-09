from django.db import models
from django.utils import timezone
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=30)
    def __str__(self):
        return self.name

class VideoContent(models.Model): 

    CurrentDateTime = models.DateTimeField(default=timezone.now)   
    title = models.CharField(max_length=40)
    img = models.ImageField(upload_to = 'pics')
    url = models.URLField(max_length=200)
    category = models.ManyToManyField(Category)

    class Meta:
        ordering = ["-CurrentDateTime"]
    
    def __str__(self):
        return self.title