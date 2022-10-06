from django.db import models
from django.utils import timezone


class Application(models.Model):
    name = models.CharField('アプリケーション名', max_length=32)
    action_url = models.URLField('アクションURL')
    explanation = models.CharField('説明',  max_length=256)
    help_url = models.URLField('ヘルプページURL')
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)


class Parameter(models.Model):
    name = models.CharField('名称', max_length=32)
    key_name = models.CharField('キー', max_length=32)
    application = models.ForeignKey(Application, on_delete=models.PROTECT)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)
