from django.http import HttpResponseRedirect
from django.shortcuts import redirect


class AuthorMixin():
    def get(self, request, *args, **kwargs):
        response = super().get(request, *args, **kwargs)

        if self.request.user.id != self.object.author.id:
            return redirect(self.object.get_absolute_url())

        return response # noqa


class RecipeFormMixin():
    def form_valid(self, form):
        self.object = form.save(author=self.request.user)
        return HttpResponseRedirect(self.get_success_url())
