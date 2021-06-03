from django.contrib import admin

from ..models import Favorite


@admin.register(Favorite)
class FavoriteAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'recipe', 'created_at',)
    list_filter = ('created_at',)

    search_fields = (
        'user__username',
        'user__first_name',
        'user__last_name',
        'recipe__name',
    )
