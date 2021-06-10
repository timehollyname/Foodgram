from django.conf import settings
from django.views.generic import ListView

from ..models import Recipe


class HomeView(ListView):
    model = Recipe
    context_object_name = 'recipes'
    template_name = 'recipes/index.html'
    paginate_by = settings.PAGINATION_RECIPES_SIZE

    def get_queryset(self):
        return super().get_queryset().get_by_tags(
            self.request.GET
        ).get_var_is_favorite(
            self.request.user
        ).select_related(
            'author'
        ).prefetch_related(
            'tags'
        ).distinct()
