from django.contrib.auth import get_user_model
from django.db import models
from django.utils import timezone

User = get_user_model()


class PollerProcess(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
    )
    pid = models.PositiveIntegerField(
        null=True,
        blank=True,
    )
    updated_at = models.DateTimeField(
        default=timezone.now,
    )
    active = models.BooleanField(
        default=False,
    )
