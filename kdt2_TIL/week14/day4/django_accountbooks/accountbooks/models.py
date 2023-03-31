from django.db import models


# Create your models here.
class AccountBook(models.Model):
    note = models.CharField(max_length=80, default='미정')
    description = models.TextField(null=True)
    category = models.CharField(max_length=20, default='미정')
    amount = models.IntegerField(default=0)
    date = models.DateField()   # 사용할 날짜
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Order(models.Model):
    '''
    True -> ASC
    False -> DESC
    '''
    id_order = models.BooleanField(default=True)
    note_order = models.BooleanField(default=True)
    category_order = models.BooleanField(default=True)
    amount_order = models.BooleanField(default=True)
    date_order = models.BooleanField(default=True)