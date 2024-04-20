from django.contrib.auth import get_user_model
from django.db.models.signals import post_delete, post_save
from django.dispatch import receiver
from django.utils import timezone

from .models import License

User = get_user_model()


@receiver(post_save, sender=User)
def create_license(sender, instance, created, **kwargs):
    if created:
        start_date = timezone.now()
        end_date = start_date + timezone.timedelta(days=7)
        License.objects.create(
            user=instance,
            start_date=start_date,
            end_date=end_date
        )


@receiver(post_save, sender=User)
def update_license(sender, instance, **kwargs):
    try:
        license = instance.license
    except License.DoesNotExist:
        return
    if not license.active:
        license.active = True
        license.save()


@receiver([post_save, post_delete], sender=License)
def update_license_status(sender, instance, **kwargs):
    if kwargs.get('raw', False):
        return

    current_time = timezone.now()
    if instance.end_date <= current_time and instance.active:
        License.objects.filter(pk=instance.pk).update(active=False)
        instance.user.has_license = False
        instance.user.save(update_fields=['has_license'])
    elif instance.end_date > current_time and not instance.active:
        License.objects.filter(pk=instance.pk).update(active=True)
        instance.user.has_license = True
        instance.user.save(update_fields=['has_license'])
