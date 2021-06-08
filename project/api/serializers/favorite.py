from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator
from users.models import Favorite  # type: ignore


class FavoriteSerializer(serializers.ModelSerializer):
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
