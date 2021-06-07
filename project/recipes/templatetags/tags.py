from django import template

register = template.Library()


@register.simple_tag
def is_the_tag_detected_in_get(request, pk):
    return str(pk) in request.GET.getlist('tags')
