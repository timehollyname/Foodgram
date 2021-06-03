from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator
from users.models import Favorite  # type: ignore

from .recipe import RecipeSerializer


class FavoriteListRetrieveSerializer(serializers.ModelSerializer):
    recipe = RecipeSerializer()

    class Meta:
        model = Favorite
        exclude = ('user', 'created_at',)


class FavoriteCreateDestroySerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault())

    class Meta:
        model = Favorite
        exclude = ('created_at',)

        validators = (
            UniqueTogetherValidator(
                queryset=Favorite.objects.all(),
                fields=('user', 'recipe'),
                message=(
                    'Данный рецепт уже находиться в списке избранных.'
                )
            ),
        )
