from rest_framework.permissions import IsAuthenticated

from ..mixins import ListCreateRetrieveDestroyMixin
from ..serializers import FavoriteSerializer


class FavoriteViewSet(ListCreateRetrieveDestroyMixin):
    permission_classes = (IsAuthenticated,)
    serializer_class = FavoriteSerializer
    pagination_class = None
    lookup_field = 'recipe'

    def get_queryset(self):
        return self.request.user.favorites.all()
