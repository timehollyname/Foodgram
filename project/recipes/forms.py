from django.forms import CheckboxSelectMultiple, ModelForm

from .fields import ListWithoutValidationField
from .models import Recipe, RecipeIngredient
from .utils import generate_recipe_ingredient


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
            'image',
        )

        labels = {
            'name': 'Название рецепта',
            'description': 'Описание',
            'cooking_time': 'Время приготовления',
            'tags': 'Теги',
            'image': 'Загрузить фото',
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

    def save(self, author, is_edit):
        ingredients = self.cleaned_data.pop('ingredients')
        ingredients = generate_recipe_ingredient(ingredients)

        instance = super().save(commit=False)
        instance.author = author
        instance.save()

        if is_edit:
            instance.ingredients.clear()

        instance.recipe_ingredients.set(ingredients, bulk=False)

        return instance
