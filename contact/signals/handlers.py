from django.conf import settings
from django.core.mail import send_mail
from django.db.models.signals import post_save
from django.dispatch import receiver

from contact.models import Comment


@receiver(post_save, sender=Comment)
def comment_create_notification(sender, instance, created, **kwargs):

    if created:
        subject = "お問い合わせ通知"
        message = f"{instance.name}\n" \
                  f"{instance.title}\n" \
                  f"{instance.email}\n" \
                  f"{instance.message}\n"
        from_email = settings.DEFAULT_FROM_EMAIL
        recipient_list = [settings.EMAIL_HOST_USER]
        send_mail(subject, message, from_email, recipient_list)
