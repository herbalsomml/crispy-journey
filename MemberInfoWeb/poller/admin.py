from django.contrib import admin

from .models import PollerProcess


class PollerProccessAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'user',
        'pid'
    )
    search_fields = (
        'user__username',
    )
    ordering = (
        'id',
    )


admin.site.register(PollerProcess, PollerProccessAdmin)
