from django.db import models
from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class Review(models.Model):
    title = models.CharField('제목', max_length=20)
    content = models.TextField('내용')
    movie = models.CharField('영화', max_length=20)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    score = models.PositiveIntegerField('평점', default=3, validators=[MinValueValidator(0), MaxValueValidator(5)])

class Comment(models.Model):
    review = models.ForeignKey(to=Review, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.CharField(max_length=50)