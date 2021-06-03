from django.contrib import admin

from ..models import Tag


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'color', 'background',)
    search_fields = ('name',)
