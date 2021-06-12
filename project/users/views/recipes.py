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
        username = self.kwargs.get('username')
        self.author = get_object_or_404(User, username=username)
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['author'] = self.author

        if self.request.user.is_authenticated:
            if self.request.user.id != self.author.id:
                exists = self.request.user.subscriptions
                exists = exists.filter(author__id=self.author.id).exists()
                context['is_subscribed'] = exists

        return context

    def get_queryset(self):
        return self.author.recipes.get_by_tags(
            self.request.GET
        ).get_var_is_favorite(
            self.request.user
        ).select_related(
            'author'
        ).prefetch_related(
            'tags'
        ).distinct()
