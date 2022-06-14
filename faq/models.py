from django.db import models
from mdeditor.fields import MDTextField


class Article(models.Model):
    title = models.CharField(max_length=100)
    content = MDTextField()

    def __str__(self):
        return self.title
