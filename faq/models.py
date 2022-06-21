from django.db import models
# from mdeditor.fields import MDTextField
from markdownx.models import MarkdownxField


class Article(models.Model):
    title = models.CharField(max_length=100)
    content = MarkdownxField()

    def __str__(self):
        return self.title
