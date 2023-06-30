# from django.db.models.signals import post_save
# from django.dispatch import receiver
# from django.core.mail import send_mail
# from django.conf import settings
# from .models import User


# def send_account_creation_email(sender, instance, created, **kwargs):
#     if created:
#         subject = "OnePay Account Created"
#         message = f"Dear {instance.first_name},\n\nYour OnePay account has been created successfully!\n\nAccount Number: {instance.wallet_id}\n\n Quickly complete the KYC section so you can enjoy the full benefits of OnePay. Thank you for joining OnePay!"
#         send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [instance.email])


# def connect_signals(sender, **kwargs):
#     User = sender.get_model('User')
#     post_save.connect(send_account_creation_email, sender=User)
