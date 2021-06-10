from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED, HTTP_204_NO_CONTENT
from rest_framework.viewsets import ViewSet

from users.models import Purchases  # noqa

from ..serializers import PurchasesSerializer


class PurchasesViewSet(ViewSet):
    serializer_class = PurchasesSerializer
    http_method_names = ('get', 'post', 'delete',)
    purchases = None

    def dispatch(self, request, *args, **kwargs):
        self.purchases = Purchases(request)
        return super().dispatch(request, *args, **kwargs)

    def list(self, request):
        serializer = self.serializer_class(self.purchases)
        return Response(serializer.data)

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        id = serializer.validated_data.get('recipe').id
        self.purchases.add(id)
        return Response({'recipe': id}, status=HTTP_201_CREATED)

    def destroy(self, request, pk=None):
        self.purchases.remove(int(pk))
        return Response(status=HTTP_204_NO_CONTENT)
