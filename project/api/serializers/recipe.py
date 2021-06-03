from recipes.models import Recipe, RecipeIngredient  # type: ignore
from rest_framework.serializers import ModelSerializer

from .author import AuthorListRetrieveSerializer
from .ingredient import IngredientSerializer
from .tag import TagSerializer


class RecipeIngredientSerializer(ModelSerializer):
    ingredient = IngredientSerializer()

    class Meta:
        model = RecipeIngredient
        exclude = ('recipe',)


class RecipeSerializer(ModelSerializer):
    author = AuthorListRetrieveSerializer()

    ingredients = RecipeIngredientSerializer(
        source='recipe_ingredients', many=True)
    tags = TagSerializer(
        many=True)

    class Meta:
        model = Recipe
        fields = '__all__'


class SubscriptionRecipeSerializer(ModelSerializer):
    ingredients = RecipeIngredientSerializer(
        source='recipe_ingredients', many=True)
    tags = TagSerializer(
        many=True)

    class Meta:
        model = Recipe
        exclude = ('author',)
