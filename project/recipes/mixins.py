from django.shortcuts import redirect


class AuthorMixin():
    def get(self, request, *args, **kwargs):
        response = super().get(request, *args, **kwargs)

        if self.request.user.id != self.object.author.id:
            return redirect(self.object.get_absolute_url())

        return response
