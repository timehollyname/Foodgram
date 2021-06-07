from django.conf import settings
from django.views.generic import ListView

from ..models import Recipe


class HomeView(ListView):
    context_object_name = 'recipes'
    template_name = 'recipes/home.html'
    paginate_by = settings.PAGINATION_RECIPES_SIZE

    def get_queryset(self):
        objects = Recipe.objects

        if 'tags' in self.request.GET:
            objects = objects.get_by_tags(
                self.request.GET.getlist('tags')
            )

        if self.request.user.is_authenticated:
            objects = objects.get_var_is_favorite(
                self.request.user
            )

        return objects.select_related(
            'author'
        ).prefetch_related(
            'tags'
        ).distinct()
