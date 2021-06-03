from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator
from users.models import Subscription  # type: ignore

from .author import AuthorListRetrieveSerializer
from .recipe import SubscriptionRecipeSerializer


class SubscriptionListRetrieveSerializer(serializers.ModelSerializer):
    author = AuthorListRetrieveSerializer()
    recipes = serializers.SerializerMethodField()
    recipes_count = serializers.IntegerField()
    recipes_count_remains = serializers.SerializerMethodField()

    class Meta:
        model = Subscription
        exclude = ('user', 'created_at',)

    def get_recipes(self, obj):
        recipes = obj.author.recipes.all()[:3]
        return SubscriptionRecipeSerializer(recipes, many=True).data

    def get_recipes_count_remains(self, obj):
        return (obj.recipes_count - 3) if obj.recipes_count > 3 else 0


class SubscriptionCreateDestroySerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault())

    class Meta:
        model = Subscription
        exclude = ('created_at',)

        validators = (
            UniqueTogetherValidator(
                queryset=Subscription.objects.all(),
                fields=('user', 'author'),
                message='Вы уже подписаны на данного автора.'
            ),
        )

    def validate_author(self, author):
        if self.context['request'].user.id == author.id:
            raise serializers.ValidationError((
                'Вы не можете подписываться на самого себя.'
            ))
        return author
