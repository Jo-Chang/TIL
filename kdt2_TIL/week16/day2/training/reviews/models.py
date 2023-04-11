from django.db import models
from imagekit.models import ProcessedImageField 

# Create your models here.
class Review(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField()
    movie = models.CharField(max_length=20)
    image = models.ImageField(blank=True, upload_to='image/')
    
    
class Comment(models.Model):
    review = models.ForeignKey(to=Review, on_delete=models.CASCADE)
    content = models.CharField(max_length=50)