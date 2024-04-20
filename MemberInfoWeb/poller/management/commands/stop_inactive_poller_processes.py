import os

from django.core.management.base import BaseCommand
from django.utils import timezone

from poller.models import PollerProcess


class Command(BaseCommand):
    help = 'Stop inactive processes'

    def handle(self, *args, **kwargs):
        threshold_time = timezone.now() - timezone.timedelta(minutes=10)
        inactive_processes = PollerProcess.objects.filter(
            active=True,
            updated_at__lt=threshold_time
        )
        if inactive_processes:
            for process in inactive_processes:
                try:
                    os.kill(process.pid, 9)
                except ProcessLookupError:
                    self.stdout.write(
                        self.style.WARNING(
                            f"Process {process.pid} was not"
                            f" found in the system"
                        )
                    )
                process.active = False
                process.pid = None
                self.stdout.write(
                    self.style.WARNING(
                        f"Process {process.pid} was stopped"
                        f" because it was inactive"
                    )
                )
                process.save()
            self.stdout.write(
                self.style.SUCCESS('All inactive processes were stopped')
            )
        else:
            self.stdout.write(
                self.style.SUCCESS('No inactive processes found')
            )
