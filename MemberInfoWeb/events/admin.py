from django.contrib import admin
from django.db.models import Sum

from .models import Event, Member, Model


class EventAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'member',
        'model',
        'event_type',
        'amount',
        'received_at'
    )
    list_filter = (
        'event_type',
        'member',
        'model',
        'received_at'
    )
    search_fields = [
        'member__username',
        'model__name'
    ]
    ordering = (
        'id',
    )


class MemberAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'username',
        'total_spends'
    )
    readonly_fields = (
        'total_spends',
    )
    ordering = (
        'id',
    )

    def total_spends(self, obj):
        events = obj.event_set.all()
        return sum(event.amount for event in events)

    total_spends.short_description = 'Total Spends'


class ModelAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'user',
        'username',
        'total_amount_spent'
    )
    ordering = (
        'id',
    )

    def total_amount_spent(self, obj):
        total_spent = obj.event_set.aggregate(Sum('amount'))['amount__sum']
        return total_spent if total_spent else 0

    total_amount_spent.short_description = 'Total Amount Spent'


admin.site.register(Model, ModelAdmin)
admin.site.register(Member, MemberAdmin)
admin.site.register(Event, EventAdmin)
