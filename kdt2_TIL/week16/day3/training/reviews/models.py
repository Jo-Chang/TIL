from django.db import models
from django.conf import settings
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill


class Review(models.Model):
    user = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=80)
    content = models.TextField(null=False)
    movie = models.CharField(max_length=80)
    image = ProcessedImageField(blank=True, upload_to='hello'+'/',
                                processors=[ResizeToFill(100,70)],
                                format='JPEG',
                                options={'quality': 90}
                                )


class Comment(models.Model):
    user = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    review = models.ForeignKey(Review, on_delete=models.CASCADE)
    content = models.TextField(null=False)
