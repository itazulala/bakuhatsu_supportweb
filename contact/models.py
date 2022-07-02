from django.db import models
from django.utils import timezone


class Comment(models.Model):
    name = models.CharField('氏名', max_length=100)
    email = models.EmailField('メールアドレス', max_length=255)
    title = models.CharField('件名', max_length=100)
    message = models.TextField('メッセージ')
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name

