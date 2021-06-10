from django import template

register = template.Library()


@register.filter
def is_the_tag_detected_in_get(id, request):
    return str(id) in request.GET.getlist('tags')
