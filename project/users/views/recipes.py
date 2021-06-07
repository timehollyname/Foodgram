from django.conf import settings
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from django.views.generic import ListView

User = get_user_model()


class RecipesView(ListView):
    context_object_name = 'recipes'
    template_name = 'users/recipes.html'
    paginate_by = settings.PAGINATION_RECIPES_SIZE
    author = None

    def dispatch(self, request, *args, **kwargs):
        username = self.kwargs.get('username', None)

        if request.user.is_authenticated and request.user.username == username:
            self.author = request.user
        else:
            self.author = get_object_or_404(User, username=username)

        return super().dispatch(request, *args, **kwargs)

    def get_queryset(self):
        objects = self.author.recipes

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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['author'] = self.author
        return context
