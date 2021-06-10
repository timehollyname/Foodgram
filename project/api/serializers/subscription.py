from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator
from users.models import Subscription  # type: ignore


class SubscriptionSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault())

    class Meta:
        model = Subscription
        exclude = ('id', 'created_at',)

        validators = (
            UniqueTogetherValidator(
                queryset=Subscription.objects.all(),
                fields=('user', 'author'),
                message='Вы уже подписаны на данного автора.'
            ),
        )

    def validate_author(self, author):
        if self.context['request'].user.id == author.id:
            message = 'Вы не можете подписываться на самого себя.'
            raise serializers.ValidationError(message)
        return author
