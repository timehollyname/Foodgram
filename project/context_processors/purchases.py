from users.models import Purchases  # type: ignore


def number_of_recipes_in_purchases(request):
    purchases = Purchases(request)
    return {'number_of_recipes_in_purchases': purchases.count()}
