from django.contrib import admin

from .models import License


class LicensesAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'user',
        'start_date',
        'end_date',
        'active'
    )
    search_fields = (
        'user__username',
        'user__email'
    )
    ordering = (
        'id',
    )


admin.site.register(License, LicensesAdmin)
