from django.db import models
from django.conf import settings


class Article(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    like_users = models.ManyToManyField(to=settings.AUTH_USER_MODEL, related_name='like_articles')
    emote_users = models.ManyToManyField(to=settings.AUTH_USER_MODEL, related_name='emote_articles', through='Emote')
    title = models.CharField(max_length=80)
    content = models.TextField(null=False)


class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    like_users = models.ManyToManyField(to=settings.AUTH_USER_MODEL, related_name='like_comments')
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    content = models.TextField(null=False)


class Emote(models.Model):
    article = models.ForeignKey(to=Article, on_delete=models.CASCADE)
    user = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    emotion = models.CharField(max_length=10)