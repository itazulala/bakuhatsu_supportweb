from django.utils import timezone
from django.db import models
from markdownx.models import MarkdownxField
from django.core.validators import FileExtensionValidator
from pathlib import Path


class Tag(models.Model):
    name = models.CharField(max_length=32)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=32)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name


class MarkdownFile(models.Model):
    upload_path = models.FileField(upload_to='contents', validators=[FileExtensionValidator(['md',])])
    uploaded = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return Path(str(self.upload_path)).name


class Article(models.Model):
    title = models.CharField(max_length=100)
    content = MarkdownxField()
    draft = models.BooleanField()
    tags = models.ManyToManyField(Tag)
    category_id = models.ForeignKey(Category, on_delete=models.PROTECT)
    markdown_file_id = models.OneToOneField(MarkdownFile, on_delete=models.PROTECT)
    good_count = models.IntegerField(default=0)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title



