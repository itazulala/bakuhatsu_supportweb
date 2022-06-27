from datetime import datetime

from django.utils import timezone
from django.db import models
from markdownx.models import MarkdownxField
from accounts.models import AccountRole
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
    upload_path = models.FileField(upload_to='faq', validators=[FileExtensionValidator(['md',])])
    uploaded = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return Path(str(self.upload_path)).name


class Article(models.Model):
    question = models.CharField(max_length=100)
    answer = MarkdownxField()
    file_path = models.CharField(max_length=100)
    draft = models.BooleanField(default=False)
    tags = models.ManyToManyField(Tag)
    category_id = models.ForeignKey(Category, on_delete=models.PROTECT)
    account_role_id = models.ForeignKey(AccountRole, default=1, on_delete=models.PROTECT, related_name='faq_role')
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.question



