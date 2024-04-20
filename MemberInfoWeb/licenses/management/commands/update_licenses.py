from django.core.management.base import BaseCommand
from django.utils import timezone

from licenses.models import License


class Command(BaseCommand):
    help = 'Updates the status of licenses'

    def handle(self, *args, **kwargs):
        current_time = timezone.now()
        expired_licenses = License.objects.filter(
            end_date__lte=current_time,
            active=True
        )
        for license in expired_licenses:
            license.active = False
            license.user.has_license = False
            license.user.save(update_fields=['has_license'])
            license.save(update_fields=['active'])

        active_licenses = License.objects.filter(
            end_date__gt=current_time,
            active=False
        )
        for license in active_licenses:
            license.active = True
            license.user.has_license = True
            license.user.save(update_fields=['has_license'])
            license.save(update_fields=['active'])

        self.stdout.write(self.style.SUCCESS('Licenses updated successfully'))
