from django.db import models
from django.db.models import TextField
from django.forms import CharField
from datetime import timedelta
from django.utils import timezone


class Author(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField()

    def __str__(self):
        return self.name

class Blog(models.Model):
    title = models.CharField(max_length=150)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey('Author', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.title


    def published_recently(self):
        date_before = timezone.now() - timedelta(days=7)

        return self.published_date >= date_before





