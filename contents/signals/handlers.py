from django.conf import settings
from django.core.mail import send_mail
from django.db.models.signals import post_save
from django.dispatch import receiver

from contents.models import Thread, Comment
from config.settings import BASE_URL


@receiver(post_save, sender=Thread)
def thread_create_notification(sender, instance, created, **kwargs):

    if created:
        subject = "コメント投稿通知"
        message = f"コメントが投稿されました。\n\n"\
                  f"氏名：{instance.name}\n\n" \
                  f"メールアドレス：{instance.email}\n\n" \
                  f"メッセージ：\n{instance.message}\n\n" \
                  f"URL：{BASE_URL}/contents/comment/{instance.id}/detail\n"
        from_email = settings.DEFAULT_FROM_EMAIL
        recipient_list = [settings.EMAIL_HOST_USER]
        send_mail(subject, message, from_email, recipient_list)


@receiver(post_save, sender=Comment)
def comment_create_notification(sender, instance, created, **kwargs):
    if created and not instance.admin_flag:
        print(instance.admin_flag)
        subject = "コメント投稿通知"
        message = f"コメントが投稿されました。\n\n"\
                  f"氏名：{instance.name}\n\n" \
                  f"メールアドレス：{instance.email}\n\n" \
                  f"メッセージ：\n{instance.message}\n\n" \
                  f"URL：{BASE_URL}/contents/comment/{instance.id}/detail\n"
        from_email = settings.DEFAULT_FROM_EMAIL
        recipient_list = [settings.EMAIL_HOST_USER]
        send_mail(subject, message, from_email, recipient_list)
