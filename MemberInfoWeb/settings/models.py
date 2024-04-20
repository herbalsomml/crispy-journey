import requests
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from events.models import Model

User = get_user_model()


class UserSettings(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    chaturbate_username = models.CharField(max_length=30)
    chaturbate_token = models.CharField(max_length=24)
    minimal_spends_for_notifications = models.IntegerField(default=100)
    minimal_spends_on_model_for_notifications = models.IntegerField(default=0)
    time_between_entering_for_notifications = models.IntegerField(default=5)

    def clean(self):
        if self.chaturbate_token and self.chaturbate_username:
            url = (f"https://eventsapi.chaturbate.com/event"
                   f"s/{self.chaturbate_username}/{self.chaturbate_token}/"
                   f"?timeout=0")
            if Model.objects.filter(
                username=self.chaturbate_username
            ).exists():
                model = Model.objects.get(
                    username=self.chaturbate_username
                )
                if model.user != self.user:
                    raise ValidationError("Другой пользователь уже "
                                          "работает с этим "
                                          "аккаунтов Chaturbate")

            if Model.objects.filter(
                user=self.user
            ).exists():
                existing_model = Model.objects.get(
                    user=self.user,
                )
                print(existing_model.username)
                if ((existing_model.username != self.chaturbate_username)
                        and (existing_model.username != '')):
                    raise ValidationError("Нельзя привязать другой"
                                          "аккаунт Chaturbate")

            try:
                response = requests.get(url)
                if response.status_code == 401:
                    raise ValidationError(f"Неверные учетные данные"
                                          f" Chaturbate:\n{url}")
                elif response.status_code != 200:
                    raise ValidationError("Не удалось подключиться"
                                          " к Chaturbate API")
            except requests.RequestException:
                raise ValidationError("Не удалось подключиться"
                                      " к Chaturbate API")
        elif self.chaturbate_token or self.chaturbate_username:
            raise ValidationError("Необходимо заполнить оба"
                                  " поля chaturbate_token "
                                  "и chaturbate_username")

    @receiver(post_save, sender=User)
    def create_user_settings(sender, instance, created, **kwargs):
        if created:
            UserSettings.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_settings(sender, instance, **kwargs):
        instance.usersettings.save()

    def save(self, *args, **kwargs):
        self.clean()
        if Model.objects.filter(user=self.user).exists():
            Model.objects.filter(user=self.user).update(
                username=self.chaturbate_username
            )

        super().save(*args, **kwargs)


@receiver(post_save, sender=UserSettings)
def create_model_for_user(sender, instance, created, **kwargs):
    if created and instance.user_id is not None:
        Model.objects.create(
            user=instance.user,
            username=instance.chaturbate_username
        )
