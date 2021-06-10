from rest_framework.serializers import ModelSerializer

from recipes.models import Ingredient  # noqa


class IngredientSerializer(ModelSerializer):
    class Meta:
        model = Ingredient
        fields = '__all__'
