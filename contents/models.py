from django.utils import timezone
from django.db import models
from accounts.models import AccountRole


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
    file_path = models.CharField(max_length=100)
    draft = models.BooleanField()
    tags = models.ManyToManyField(Tag)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    account_role = models.ForeignKey(AccountRole, default=1, on_delete=models.PROTECT, related_name='contents_role')
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title


class Thread(models.Model):
    name = models.CharField('ニックネーム', max_length=100, null=True)
    email = models.EmailField('メールアドレス', max_length=255, null=True)
    title = models.CharField('タイトル', max_length=100)
    message = models.TextField('メッセージ', blank=False)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title


class Comment(models.Model):
    thread = models.ForeignKey(Thread, on_delete=models.CASCADE)
    name = models.CharField('ニックネーム', max_length=100, null=True)
    email = models.EmailField('Eメールアドレス', max_length=255, null=True)
    message = models.TextField('メッセージ')
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.question