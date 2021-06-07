from recipes.models import Tag  # type: ignore


def tags(request):
    return {'tags': Tag.objects.all()}
