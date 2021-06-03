from django.contrib import admin

from ..models import Subscription


@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'author', 'created_at',)
    list_filter = ('created_at',)

    search_fields = (
        'user__username',
        'user__first_name',
        'user__last_name',
        'author__username',
        'author__first_name',
        'author__last_name',
    )
