from django import template

register = template.Library()


@register.simple_tag
def change_page(request, page):
    req = request.GET.copy()
    req['page'] = page
    req = req.urlencode()

    return f'?{req}'


@register.simple_tag
def change_tag(request, pk):
    pk = str(pk)
    req = request.GET.copy()
    tags = req.getlist('tags')

    if pk in tags:
        tags.remove(pk)
    else:
        tags.append(pk)

    if 'page' in req:
        req.pop('page')

    req.setlist('tags', tags)
    req = req.urlencode()

    return f'?{req}'
