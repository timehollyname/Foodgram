from recipes.models import Tag  # type: ignore
from rest_framework.viewsets import ReadOnlyModelViewSet

from ..serializers import TagSerializer


class TagViewSet(ReadOnlyModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    pagination_class = None
