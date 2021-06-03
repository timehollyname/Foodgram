from django.views.generic import TemplateView


class RecipeView(TemplateView):
    template_name = 'recipes/recipe/get.html'


class RecipeEditView(TemplateView):
    template_name = 'recipes/recipe/edit.html'


class RecipeCreateView(TemplateView):
    template_name = 'recipes/recipe/create.html'
