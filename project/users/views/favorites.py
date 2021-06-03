from django.views.generic import ListView
from recipes.models import Recipe  # type: ignore


class FavoritesView(ListView):
    context_object_name = 'recipes'
    template_name = 'users/favorites.html'
    paginate_by = 9

    def get_queryset(self):
        return Recipe.objects.filter(
            favorites__user__id=self.request.user.id
        ).select_related(
            'author'
        ).prefetch_related(
            'tags'
        ).prefetch_related(
            'recipe_ingredients'
        ).prefetch_related(
            'recipe_ingredients__ingredient'
        )
