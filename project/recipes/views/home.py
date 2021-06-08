from django.conf import settings
from django.views.generic import ListView

from ..models import Recipe


class HomeView(ListView):
    context_object_name = 'recipes'
    template_name = 'recipes/home.html'
    paginate_by = settings.PAGINATION_RECIPES_SIZE

    def get_queryset(self):
        return Recipe.objects.get_by_tags(
            self.request.GET
        ).get_var_is_favorite(self.request.user).select_related(
            'author'
        ).prefetch_related('tags').distinct()
