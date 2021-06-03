from django.contrib import admin

from ..models import Ingredient


@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'dimension',)
    search_fields = ('name',)
