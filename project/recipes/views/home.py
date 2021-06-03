from django.views.generic import ListView

from ..models import Recipe


class HomeView(ListView):
    queryset = Recipe.objects.select_related(
        'author'
    ).prefetch_related(
        'tags'
    ).prefetch_related(
        'recipe_ingredients'
    ).prefetch_related(
        'recipe_ingredients__ingredient'
    ).all()

    context_object_name = 'recipes'
    template_name = 'recipes/home.html'
    paginate_by = 9
