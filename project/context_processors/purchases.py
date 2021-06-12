from users.models import Purchase  # type: ignore


def number_of_recipes_in_purchases(request):
    return {'number_of_recipes_in_purchases': Purchase(request).count()}
