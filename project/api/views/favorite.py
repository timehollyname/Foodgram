from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import SAFE_METHODS, IsAuthenticated
from users.models import Favorite  # type: ignore

from ..mixins import ListCreateRetrieveDestroyMixin
from ..serializers import (FavoriteCreateDestroySerializer,
                           FavoriteListRetrieveSerializer)


class FavoriteViewSet(ListCreateRetrieveDestroyMixin):
    permission_classes = (IsAuthenticated,)
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('recipe__tags',)

    safe_serializer_class = FavoriteListRetrieveSerializer
    unsafe_serializer_class = FavoriteCreateDestroySerializer

    def get_queryset(self):
        return Favorite.objects.filter(
            user__id=self.request.user.id
        ).select_related(
            'recipe',
            'recipe__author'
        ).prefetch_related(
            'recipe__tags',
            'recipe__recipe_ingredients',
            'recipe__recipe_ingredients__ingredient'
        )

    def get_serializer_class(self):
        if self.request.method in SAFE_METHODS:
            return self.safe_serializer_class
        return self.unsafe_serializer_class
