from django.db.models.signals import post_save
from django.dispatch import receiver
from config.settings import EMAIL_HOST, EMAIL_HOST_USER, EMAIL_HOST_PASSWORD, EMAIL_PORT

from contact.models import Comment
from email.mime.text import MIMEText
import smtplib, ssl


@receiver(post_save, sender=Comment)
def comment_create_notification(sender, instance, created, **kwargs):
    if created:
        subject = "お問い合わせ通知"
        message = f"<h3>お問い合わせがありました。</h3><br>" \
                  f"<p>[氏名]<br>{instance.name}</p>" \
                  f"<p>[タイトル]<br>{instance.title}</p>" \
                  f"<p>[メッセージ]<br>{instance.message}</p>" \
                  f"<p>[メールアドレス]<br>{instance.email}</p>"

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
