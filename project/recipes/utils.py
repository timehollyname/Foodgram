from .models import RecipeIngredient


def generate_recipe_ingredient(ingredients):
    return [RecipeIngredient(**ingredient) for ingredient in ingredients]
