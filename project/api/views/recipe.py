from django_filters.rest_framework import DjangoFilterBackend
from recipes.models import Recipe  # type: ignore
from rest_framework.viewsets import ReadOnlyModelViewSet

from ..serializers import RecipeSerializer


class RecipeViewSet(ReadOnlyModelViewSet):
    queryset = Recipe.objects.select_related(
        'author'
    ).prefetch_related(
        'tags'
    ).prefetch_related(
        'recipe_ingredients'
    ).prefetch_related(
        'recipe_ingredients__ingredient'
    ).all()

    serializer_class = RecipeSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('tags',)
