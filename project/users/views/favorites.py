from django.conf import settings
from django.views.generic import ListView
from recipes.models import Recipe  # type: ignore


class FavoritesView(ListView):
    context_object_name = 'recipes'
    template_name = 'users/favorites.html'
    paginate_by = settings.PAGINATION_RECIPES_SIZE

    def get_queryset(self):
        objects = Recipe.objects.filter(
            favorites__user__id=self.request.user.id
        )

        if 'tags' in self.request.GET:
            objects = objects.get_by_tags(
                self.request.GET.getlist('tags')
            )

        return objects.select_related(
            'author'
        ).prefetch_related(
            'tags'
        ).distinct()
