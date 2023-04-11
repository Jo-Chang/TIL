from django.db import models

# Create your models here.
class Review(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField()
    movie = models.CharField(max_length=20)
    
    
class Comment(models.Model):
    review = models.ForeignKey(to=Review, on_delete=models.CASCADE)
    content = models.CharField(max_length=50)