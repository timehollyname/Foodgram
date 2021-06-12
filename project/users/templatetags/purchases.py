from django import template

from ..models import Purchase

register = template.Library()


@register.filter
def is_the_recipe_detected_in_purchases(id, request):
    return Purchase(request).exists(id)
