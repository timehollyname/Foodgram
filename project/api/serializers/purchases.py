from rest_framework import serializers

from recipes.models import Recipe  # noqa


class PurchasesSerializer(serializers.Serializer):
    recipes = serializers.ListField(
        child=serializers.IntegerField(), read_only=True)
    recipe = serializers.PrimaryKeyRelatedField(
        queryset=Recipe.objects.all(), write_only=True)
