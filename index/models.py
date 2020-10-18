from django.db import models

# Create your models here.

# Create your models here.
class homedata(models.Model):
    title = models.TextField()
    description=models.TextField()
    img=models.ImageField(upload_to='pics')
    
class homeurl(models.Model):
    title=models.CharField(max_length=100,default='')
    url=models.URLField(max_length=200)
    img=models.ImageField(upload_to='pics')        