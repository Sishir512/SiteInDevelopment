from django.db import models
from django.utils import timezone
# Create your models here.

class VideoContent(models.Model): 
    CurrentDateTime = models.DateTimeField(default=timezone.now)   
    title = models.CharField(max_length=40)
    img = models.ImageField(upload_to = 'pics')
    url = models.URLField(max_length=200)

    class Meta:
        ordering = ["-CurrentDateTime"]