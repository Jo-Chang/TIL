from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    followings = models.ManyToManyField(to='self', symmetrical=False, related_name='followers')
