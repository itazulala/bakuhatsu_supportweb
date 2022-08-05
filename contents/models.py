import re

from django.utils import timezone
from django.db import models
from accounts.models import AccountRole


def check_name(value):
    if not value:
        return '匿名'


class Tag(models.Model):
    name = models.CharField('タグ名', max_length=32)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField('カテゴリー名', max_length=32)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name


class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    file_path = models.CharField(max_length=100, db_index=True)
    draft = models.BooleanField()
    tags = models.ManyToManyField(Tag)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    account_role = models.ForeignKey(AccountRole, default=1, on_delete=models.PROTECT, related_name='contents_role')
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title


class Thread(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    name = models.CharField('ニックネーム', max_length=100, blank=True, null=True, validators=[check_name])
    email = models.EmailField('メールアドレス', max_length=255,  blank=True, null=True)
    message = models.TextField('メッセージ', blank=False)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.article.title

    def save(self, *args, **keywords):
        if not self.name:
            self.name = '匿名'

        super().save(*args, **keywords)


class Comment(models.Model):
    thread = models.ForeignKey(Thread, on_delete=models.CASCADE)
    name = models.CharField('ニックネーム', max_length=100, null=True)
    email = models.EmailField('Eメールアドレス', max_length=255, null=True)
    message = models.TextField('メッセージ')
    admin_flag = models.BooleanField()
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.thread.article.title

