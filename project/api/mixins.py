from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet


class ListCreateRetrieveDestroyMixin(
        mixins.CreateModelMixin,
        mixins.RetrieveModelMixin,
        mixins.DestroyModelMixin,
        mixins.ListModelMixin,
        GenericViewSet):
    pass
