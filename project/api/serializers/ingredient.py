from recipes.models import Ingredient  # type: ignore
from rest_framework.serializers import ModelSerializer


class IngredientSerializer(ModelSerializer):
    class Meta:
        model = Ingredient
        fields = '__all__'
