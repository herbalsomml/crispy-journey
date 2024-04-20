from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Member(models.Model):
    username = models.CharField(max_length=30)

    @property
    def total_spends(self):
        events = Event.objects.filet(member=self)
        return sum(event.amount for event in events)


class Model(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=None)
    username = models.CharField(max_length=30, blank=False)


class Event(models.Model):
    EVENT_CHOICES = (
        ('fanclubJoin', 'Fan Club Join'),
        ('follow', 'Follow'),
        ('mediaPurchase', 'Media Purchase'),
        ('tip', 'Tip'),
        ('unfollow', 'Unfollow'),
        ('userEnter', 'User Enter'),
        ('userLeave', 'User Leave')
    )
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    model = models.ForeignKey(Model, on_delete=models.CASCADE)
    amount = models.IntegerField()
    event_type = models.CharField(max_length=20, choices=EVENT_CHOICES)
    received_at = models.DateTimeField()

    def __str__(self):
        return (f"{self.member.username} - "
                f"{self.model.username} - "
                f"{self.event_type} - "
                f"{self.amount} - "
                f"{self.received_at}")
