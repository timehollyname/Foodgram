from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, UpdateView

from ..forms import RecipeForm
from ..models import Recipe, RecipeIngredient


def generate_recipe_ingredient(ingredients):
    return [RecipeIngredient(**ingredient) for ingredient in ingredients]


class RecipeView(DetailView):
    model = Recipe
    context_object_name = 'recipe'
    template_name = 'recipes/detail.html'
    http_method_names = ('get',)

    def get_queryset(self):
        return super().get_queryset().get_var_is_favorite(
            self.request.user
        ).get_var_is_subscribed(
            self.request.user
        ).select_related(
            'author'
        ).prefetch_related(
            'tags',
            'recipe_ingredients',
            'recipe_ingredients__ingredient'
        )


class RecipeEditView(LoginRequiredMixin, UpdateView):
    model = Recipe
    form_class = RecipeForm
    context_object_name = 'recipe'
    template_name = 'recipes/edit.html'

    def get_queryset(self):
        return super().get_queryset().select_related(
            'author'
        ).prefetch_related(
            'recipe_ingredients',
            'recipe_ingredients__ingredient'
        )

    def get(self, request, *args, **kwargs):
        response = super().get(request, *args, **kwargs)

        if self.request.user.id != self.object.author.id:
            return redirect(self.object.get_absolute_url())

        return response # noqa

    def form_valid(self, form):
        ingredients = form.cleaned_data.pop('ingredients')
        ingredients = generate_recipe_ingredient(ingredients)

        self.object = form.save(commit=False)
        self.object.author = self.request.user
        self.object.save()
        self.object.ingredients.clear()
        self.object.recipe_ingredients.set(ingredients, bulk=False)

        return super().form_valid(form)


class RecipeCreateView(LoginRequiredMixin, CreateView):
    model = Recipe
    form_class = RecipeForm
    template_name = 'recipes/create.html'

    def form_valid(self, form):
        ingredients = form.cleaned_data.pop('ingredients')
        ingredients = generate_recipe_ingredient(ingredients)

        self.object = form.save(commit=False)
        self.object.author = self.request.user
        self.object.save()
        self.object.recipe_ingredients.set(ingredients, bulk=False)

        return super().form_valid(form)


class RecipeDestroyView(LoginRequiredMixin, DeleteView):
    model = Recipe
    form_class = RecipeForm
    template_name = 'recipes/create.html'
    http_method_names = ('get',)
    success_url = reverse_lazy('recipes:home')

    def get(self, request, *args, **kwargs):
        super().get(request, *args, **kwargs)

        if self.request.user.id != self.object.author.id:
            return redirect(self.object.get_absolute_url())

        return super().delete(request, *args, **kwargs)
