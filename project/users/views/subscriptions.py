from django.contrib.auth import get_user_model
from django.db.models import Count
from django.views.generic import ListView

User = get_user_model()


class SubscriptionsView(ListView):
    context_object_name = 'authors'
    template_name = 'users/subscriptions.html'
    paginate_by = 9

    def get_queryset(self):
        return User.objects.filter(
            subscribers__user__id=self.request.user.id
        ).annotate(
            recipes_count=Count('recipes')
        ).prefetch_related(
            'recipes'
        )
