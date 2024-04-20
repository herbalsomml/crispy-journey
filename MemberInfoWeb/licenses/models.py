from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class License(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    active = models.BooleanField(default=True)

    def __str__(self):
        return f"License for {self.user.username}"
