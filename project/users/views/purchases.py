from io import BytesIO

from django.http import FileResponse
from django.shortcuts import redirect
from django.template.loader import get_template
from django.urls import reverse
from django.views.generic import ListView, View
from pdfkit import from_string

from recipes.models import Recipe  # noqa

from ..models import Purchase


class PurchasesView(ListView):
    context_object_name = 'recipes'
    template_name = 'users/purchases.html'

    def get_queryset(self):
        purchases = Purchase(self.request)
        objects = Recipe.objects

        if purchases.count() > 0:
            return objects.filter(id__in=purchases.recipes)

        return objects.none()


class PurchasesPdfView(View):
    http_method_names = ('get',)

    def get(self, request, *args, **kwargs):
        purchases = Purchase(self.request)

        if purchases.count() > 0:
            options = {
                'page-size': 'Letter',
                'margin-top': '0.75in',
                'margin-right': '0.75in',
                'margin-bottom': '0.75in',
                'margin-left': '0.75in',
                'encoding': 'UTF-8',
                'no-outline': None
            }

            context = {
                'recipes': Recipe.objects.filter(
                    id__in=purchases.recipes
                ).prefetch_related(
                    'recipe_ingredients',
                    'recipe_ingredients__ingredient'
                )
            }

            template = get_template('misc/pdf.html').render(context)
            pdf = from_string(template, False, options=options)

            return FileResponse(
                BytesIO(pdf), filename='recipes.pdf', as_attachment=True)

        return redirect(reverse('users:purchases'))
