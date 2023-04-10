from django.db import models

# Create your models here.
class Article(models.Model):
    def articles_image_path(instance, filename):
        return f'images/{instance.user.username}/{filename}'
    
    title = models.CharField(max_length=10)
    content = models.TextField()
    # image = models.ImageField(blank=True, upload_to='images/')    # images 폴더 안
    image = models.ImageField(blank=True, upload_to='%Y/%m/%d')     # 년 / 월 / 일 3중 폴더 안
    # image = models.ImageField(blank=True, upload_to=articles_image_path)  # 유저 이름 별 파일 안
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
