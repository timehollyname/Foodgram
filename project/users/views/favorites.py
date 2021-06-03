from django.views.generic import TemplateView


class FavoritesView(TemplateView):
    template_name = 'users/favorites.html'
