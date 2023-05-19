from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone
from .managers import UserCustomManager


class User(AbstractUser):
    email = models.EmailField(unique=True)
    is_superuser = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    phone_number = models.IntegerField(unique=True)
    is_owner = models.BooleanField(default=False)
    is_advisor = models.BooleanField(default=False)
    name = models.CharField(max_length=40)
    data_join = models.DateTimeField(default=timezone.now)
    code_agency = models.IntegerField(null=True, blank=True, default=0)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserCustomManager()

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'
