from django.views.generic import TemplateView


class SubscriptionsView(TemplateView):
    template_name = 'users/subscriptions.html'
