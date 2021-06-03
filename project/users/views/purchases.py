from django.views.generic import TemplateView


class PurchasesView(TemplateView):
    template_name = 'users/purchases.html'
