from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.conf import settings

from .models import Wallet

@receiver(post_save, sender=User)
def create_wallet(sender, instance, created, **kwargs):
    if created:
        wallet = Wallet.objects.create(user=instance)
        send_wallet_notification_email(wallet)


def send_wallet_notification_email(wallet):
    subject = 'Wallet ID Assigned'
    full_name = f'{wallet.user.first_name} {wallet.user.last_name}'
    message = f'Hello {full_name},\n\nYour wallet ID has been assigned: {wallet.wallet_id}'
    from_email = settings.DEFAULT_FROM_EMAIL
    to_email = wallet.user.email
    send_mail(subject, message, from_email, [to_email])
