from django.views.generic import TemplateView


class RecipesView(TemplateView):
    template_name = 'users/recipes.html'
