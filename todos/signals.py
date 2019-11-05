from django.db.models.signals import post_save
from django.core.mail import send_mail
from django.contrib.auth.models import User
from django.conf import settings
from .models import Todo
from django.dispatch import receiver


@receiver(post_save, sender=Todo)
def notify_todo_creation(sender, instance, **kwargs):
    if instance:
        subject = '[Alert] Unknown activity detected!'
        message = 'This mail is sent using Django Signals whenever psychic activity is detected on our radar.'
        email_from = settings.EMAIL_HOST_USER
        recipient_list = ['dde@narola.email',]
        send_mail(subject, message, email_from, recipient_list)
