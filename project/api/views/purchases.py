from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED, HTTP_204_NO_CONTENT
from rest_framework.viewsets import ViewSet
from users.models import Purchases  # type: ignore

from ..serializers import PurchasesSerializer


class PurchasesViewSet(ViewSet):
    serializer_class = PurchasesSerializer
    http_method_names = ('get', 'post', 'delete',)

    def list(self, request):
        purchases = Purchases(request)
        serializer = self.serializer_class(purchases)
        return Response(serializer.data)

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        pk = serializer.validated_data['recipe'].pk
        purchases = Purchases(request)
        purchases.add(pk)
        return Response({'recipe': pk}, status=HTTP_201_CREATED)

    def destroy(self, request, pk=None):
        purchases = Purchases(request)
        purchases.remove(int(pk))
        return Response(status=HTTP_204_NO_CONTENT)
