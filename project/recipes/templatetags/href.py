from django import template

register = template.Library()


@register.simple_tag
def change_page(request, page):
    req = request.GET.copy()
    req['page'] = page
    req = req.urlencode()

    return f'?{req}'


@register.simple_tag
def change_tag(request, id):
    id = str(id)
    req = request.GET.copy()
    tags = req.getlist('tags')

    if id in tags:
        tags = list(set(tags))
        tags.remove(id)
    else:
        tags.append(id)

    if 'page' in req:
        req.pop('page')

    req.setlist('tags', tags)
    req = req.urlencode()

    return f'?{req}'
