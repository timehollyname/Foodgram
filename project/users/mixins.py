from django.shortcuts import redirect
from django.urls import reverse


class ForUnauthorizedUsersMixin():
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect(reverse('recipes:home'))
        return super().dispatch(request, *args, **kwargs)
