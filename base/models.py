from django.db import models
from django.conf import settings


class Project(models.Model):
    name = models.CharField(max_length=30)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    source_code = models.URLField()

    def __str__(self):
        return self.name


class Topic(models.Model):
    name = models.CharField(max_length=30)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    content = models.TextField()

    def __str__(self):
        return self.name
