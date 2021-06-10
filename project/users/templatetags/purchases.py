from django import template

from ..models import Purchases

register = template.Library()


@register.filter
def is_the_recipe_detected_in_purchases(id, request):
    return Purchases(request).exists(id)
