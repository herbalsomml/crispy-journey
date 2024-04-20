from django.contrib import admin

from .models import UserSettings


class UserSettingsAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'user',
        'chaturbate_username',
        'minimal_spends_for_notifications',
        'minimal_spends_on_model_for_notifications',
        'time_between_entering_for_notifications'
    )
    search_fields = (
        'user__username',
        'chaturbate_username',
        'user__email',
        'chaturbate_token'
    )
    ordering = (
        "id",
    )


admin.site.register(UserSettings, UserSettingsAdmin)
