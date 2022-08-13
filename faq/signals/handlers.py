from django.conf import settings
from django.core.mail import send_mail
from django.db.models.signals import post_save
from django.dispatch import receiver
from config.settings import BASE_URL
from faq.models import Request


@receiver(post_save, sender=Request)
def comment_create_notification(sender, instance, created, **kwargs):
    if created:
        subject = "質問リクエスト通知"
        message = f"質問リクエストが投稿されました。\n\n" \
                  f"氏名：{instance.name}\n\n" \
                  f"タイトル：{instance.title}\n\n" \
                  f"メッセージ：\n{instance.message}\n\n"
        from_email = settings.DEFAULT_FROM_EMAIL
        recipient_list = [settings.EMAIL_HOST_USER]
        send_mail(subject, message, from_email, recipient_list)
