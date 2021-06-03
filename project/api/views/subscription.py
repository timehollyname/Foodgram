from django.db.models import Count
from rest_framework.permissions import SAFE_METHODS, IsAuthenticated
from users.models import Subscription  # type: ignore

from ..mixins import ListCreateRetrieveDestroyMixin
from ..serializers import (SubscriptionCreateDestroySerializer,
                           SubscriptionListRetrieveSerializer)


class SubscriptionViewSet(ListCreateRetrieveDestroyMixin):
    permission_classes = (IsAuthenticated,)

    safe_serializer_class = SubscriptionListRetrieveSerializer
    unsafe_serializer_class = SubscriptionCreateDestroySerializer

    def get_queryset(self):
        return Subscription.objects.filter(
            user__id=self.request.user.id
        ).annotate(
            recipes_count=Count('author__recipes')
        ).select_related(
            'author'
        ).prefetch_related(
            'author__recipes'
        ).prefetch_related(
            'author__recipes__tags'
        ).prefetch_related(
            'author__recipes__recipe_ingredients'
        ).prefetch_related(
            'author__recipes__recipe_ingredients__ingredient'
        )

    def get_serializer_class(self):
        if self.request.method in SAFE_METHODS:
            return self.safe_serializer_class
        return self.unsafe_serializer_class
