from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone
from .managers import UserCustomManager


class User(AbstractUser):
    username = models.CharField(max_length=30, unique=True)
    is_superuser = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_owner = models.BooleanField(default=False)
    is_advisor = models.BooleanField(default=False)
    data_join = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    objects = UserCustomManager()

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'
