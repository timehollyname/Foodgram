from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView

from recipes.models import Recipe  # noqa


class FavoritesView(LoginRequiredMixin, ListView):
    context_object_name = 'recipes'
    template_name = 'users/favorites.html'
    paginate_by = settings.PAGINATION_RECIPES_SIZE

    def get_queryset(self):
        return Recipe.objects.filter(
            favorites__user__id=self.request.user.id
        ).get_by_tags(
            self.request.GET
        ).select_related(
            'author'
        ).prefetch_related(
            'tags'
        ).distinct()
