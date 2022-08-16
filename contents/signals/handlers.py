from django.db.models.signals import post_save
from django.dispatch import receiver
from config.settings import EMAIL_HOST, EMAIL_HOST_USER, EMAIL_HOST_PASSWORD, EMAIL_PORT

from contents.models import Thread, Comment
from config.settings import BASE_URL
from email.mime.text import MIMEText
import smtplib, ssl


@receiver(post_save, sender=Thread)
def thread_create_notification(sender, instance, created, **kwargs):
    if created:
        subject = "コメント投稿通知（テスト）"
        message = f"<h3>コメントが投稿されました。</h3><br>" \
                  f"<p>[氏名]<br>{instance.name}</p>" \
                  f"<p>[メールアドレス]<br>{instance.email}</p>" \
                  f"<p>[メッセージ]<br>{instance.message}</p>" \
                  f"<p>[URL]<br><a href='{BASE_URL}/contents/comment/{instance.id}/detail'>{BASE_URL}/contents/comment/{instance.id}/detail'</a><p>"
        # SMTP認証情報
        account = EMAIL_HOST_USER
        password = EMAIL_HOST_PASSWORD

        # MIMEの作成
        msg = MIMEText(message, "html")
        msg["Subject"] = subject
        msg["To"] = EMAIL_HOST_USER
        msg["From"] = EMAIL_HOST_USER

        server = smtplib.SMTP_SSL(EMAIL_HOST, EMAIL_PORT, context=ssl._create_unverified_context())

        server.login(account, password)
        server.send_message(msg)
        server.quit()


@receiver(post_save, sender=Comment)
def comment_create_notification(sender, instance, created, **kwargs):
    if created and not instance.admin_flag:
        print(instance.admin_flag)
        subject = "コメント投稿通知（テスト）"
        message = f"<h3>コメントが投稿されました。</h3><br>" \
                  f"<p>[氏名]<br>{instance.name}</p>" \
                  f"<p>[メールアドレス]<br>{instance.email}</p>" \
                  f"<p>[メッセージ]<br>{instance.message}</p>" \
                  f"<p>[URL]<br><a href='{BASE_URL}/contents/comment/{instance.thread.id}/detail'>{BASE_URL}/contents/comment/{instance.thread.id}/detail'</a><p>"
        # SMTP認証情報
        account = EMAIL_HOST_USER
        password = EMAIL_HOST_PASSWORD

        # MIMEの作成
        msg = MIMEText(message, "html")
        msg["Subject"] = subject
        msg["To"] = EMAIL_HOST_USER
        msg["From"] = EMAIL_HOST_USER

        server = smtplib.SMTP_SSL(EMAIL_HOST, EMAIL_PORT, context=ssl._create_unverified_context())

        server.login(account, password)
        server.send_message(msg)
        server.quit()
