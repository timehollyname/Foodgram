from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from django.views.generic import ListView

User = get_user_model()


class RecipesView(ListView):
    context_object_name = 'recipes'
    template_name = 'users/recipes.html'
    paginate_by = 9
    author = None

    def dispatch(self, request, *args, **kwargs):
        username = self.kwargs.get('username', None)

        if request.user.username == username:
            self.author = request.user
        else:
            self.author = get_object_or_404(User, username=username)

        return super().dispatch(request, *args, **kwargs)

    def get_queryset(self):
        return self.author.recipes.select_related(
            'author'
        ).prefetch_related(
            'tags'
        ).prefetch_related(
            'recipe_ingredients'
        ).prefetch_related(
            'recipe_ingredients__ingredient'
        ).all()

    def get_context_data(self, **kwargs):
        response = super().get_context_data(**kwargs)
        response['author'] = self.author
        return response
