import re
from django.db import models
from datetime import datetime


class BlogPost(models.Model):
    date = models.DateTimeField(default=datetime.now, blank=False)
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, default='')
    author = models.CharField(default="Dan W.", max_length=200)
    content = models.TextField(blank=False)
    tags = models.CharField(max_length=200, default='Blog')
    description = models.TextField(max_length=500, default='A post about ')
    is_published = models.BooleanField()

    def __str__(self):
        return self.title
