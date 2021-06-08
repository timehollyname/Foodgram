from django.views.generic import ListView
from recipes.models import Recipe  # type: ignore

from ..models import Purchases


class PurchasesView(ListView):
    context_object_name = 'recipes'
    template_name = 'users/purchases.html'

    def get_queryset(self):
        purchases = Purchases(self.request)

        if purchases.count() > 0:
            return Recipe.objects.filter(id__in=purchases.recipes)

        return []
