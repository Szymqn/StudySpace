from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    age = models.IntegerField()
    category = models.CharField(max_length=30)
    github = models.URLField()

    def __str__(self):
        return self.username
