from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.
class Category(models.Model):   # 이렇게 했을 때 모델폼 어떻게?
    category = models.CharField(_("category"), max_length=30, unique=True)


class Post(models.Model):
    title = models.CharField(max_length=80)
    content	= models.TextField()
    # category = models.CharField(max_length=20)   # <- ForeignKey
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

