from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Email

@receiver(post_save, sender=Email)
def add_sending_datetime(sender, instance, created, **kwargs):
    from datetime import timedelta
    sec = timedelta(seconds=instance.seconds)

    if created:
        instance.datetime_must_be_send = instance.datetime_created + sec
        instance.save()
