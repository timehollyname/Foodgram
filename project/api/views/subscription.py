from rest_framework.permissions import IsAuthenticated

from ..mixins import ListCreateRetrieveDestroyMixin
from ..serializers import SubscriptionSerializer


class SubscriptionViewSet(ListCreateRetrieveDestroyMixin):
    permission_classes = (IsAuthenticated,)
    serializer_class = SubscriptionSerializer
    pagination_class = None
    lookup_field = 'author'

    def get_queryset(self):
        return self.request.user.subscriptions.all()
