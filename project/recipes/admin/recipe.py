from django.contrib import admin

from ..models import Recipe, RecipeIngredient


class RecipeIngredientInline(admin.TabularInline):
    model = RecipeIngredient
    min_num = 1


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ('id', 'author', 'name', 'cooking_time', 'created_at',)
    search_fields = ('name', 'description',)
    list_filter = ('created_at',)
    inlines = (RecipeIngredientInline,)
