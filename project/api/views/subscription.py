from rest_framework.permissions import IsAuthenticated

from ..mixins import ListCreateRetrieveDestroyMixin
from ..serializers import SubscriptionSerializer


class SubscriptionViewSet(ListCreateRetrieveDestroyMixin):
    permission_classes = (IsAuthenticated,)
    serializer_class = SubscriptionSerializer

    def get_queryset(self):
        return self.request.user.subscriptions.all()
