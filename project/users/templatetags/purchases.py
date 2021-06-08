from django import template

from ..models import Purchases

register = template.Library()


@register.filter
def is_the_recipe_detected_in_purchases(recipe, request):
    purchases = Purchases(request)
    return purchases.exists(recipe.id)
