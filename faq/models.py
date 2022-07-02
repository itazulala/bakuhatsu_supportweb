from django.db.models import Q
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
    question = models.CharField(max_length=100)
    answer = models.TextField()
    file_path = models.CharField(max_length=100)
    draft = models.BooleanField(default=False)
    tags = models.ManyToManyField(Tag)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    account_role = models.ForeignKey(AccountRole, default=1, on_delete=models.PROTECT, related_name='faq_role')
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.question

    def get_queryset(self):
        q_word = self.request.GET.get('keyword')

        if q_word:
            object_list = Article.objects.filter(
                Q(question__icontains=q_word) | Q(answer__icontains=q_word) | Q(tags__icontains=q_word)
            )
        else:
            object_list = Article.objects.all()
        return object_list


class Request(models.Model):
    name = models.CharField('氏名', max_length=100)
    title = models.CharField('タイトル', max_length=100)
    message = models.TextField('メッセージ', blank=False)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.question
