from users.models import Purchases  # type: ignore


def number_of_recipes_in_purchases(request):
    return {'number_of_recipes_in_purchases': Purchases(request).count()}
