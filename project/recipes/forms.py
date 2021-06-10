from django.forms import CheckboxSelectMultiple, ModelForm
from django.utils.translation import gettext_lazy as _

from .fields import ListWithoutValidationField
from .models import Recipe, RecipeIngredient


class RecipeIngredientForm(ModelForm):
    class Meta:
        model = RecipeIngredient
        fields = ('ingredient', 'quantity')


class RecipeForm(ModelForm):
    ingredients = ListWithoutValidationField(required=True)

    class Meta:
        model = Recipe

        fields = (
            'name',
            'description',
            'cooking_time',
            'tags',
            'ingredients',
        )

        labels = {
            'name': _('Название рецепта'),
            'description': _('Описание'),
            'cooking_time': _('Время приготовления'),
            'tags': _('Теги'),
        }

        widgets = {'tags': CheckboxSelectMultiple()}

    def clean_ingredients(self):
        ingredients = []

        for ingredient in self.cleaned_data.get('ingredients'):
            ingredient, quantity = ingredient.split(' && ')
            quantity = quantity.replace(',', '.')

            params = {'ingredient': ingredient, 'quantity': quantity}
            form = RecipeIngredientForm(params)

            if form.is_valid():
                ingredients.append(form.clean())
            else:
                raise list(form.errors.as_data().values())[0][0]

        return ingredients
