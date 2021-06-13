from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, UpdateView

from ..forms import RecipeForm
from ..mixins import AuthorMixin, RecipeFormMixin
from ..models import Recipe


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


class RecipeEditView(
        LoginRequiredMixin,
        AuthorMixin,
        RecipeFormMixin,
        UpdateView):
    model = Recipe
    form_class = RecipeForm
    context_object_name = 'recipe'
    template_name = 'recipes/create_or_edit.html'

    def get_queryset(self):
        return super().get_queryset().select_related(
            'author'
        ).prefetch_related(
            'recipe_ingredients',
            'recipe_ingredients__ingredient'
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_edit'] = True
        return context


class RecipeCreateView(LoginRequiredMixin, RecipeFormMixin, CreateView):
    model = Recipe
    form_class = RecipeForm
    template_name = 'recipes/create_or_edit.html'


class RecipeDestroyView(LoginRequiredMixin, AuthorMixin, DeleteView):
    model = Recipe
    http_method_names = ('get',)
    success_url = reverse_lazy('recipes:home')

    def get(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)
