from django.conf import settings
from django.contrib.auth import views
from django.shortcuts import redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView

from ..forms import CreationForm
from ..mixins import ForUnauthorizedUsersMixin


class SignUpView(ForUnauthorizedUsersMixin, CreateView):
    form_class = CreationForm
    success_url = reverse_lazy('users:signin')
    template_name = 'users/registration/signup.html'


class SignInView(ForUnauthorizedUsersMixin, views.LoginView):
    template_name = 'users/registration/signin.html'


class LogoutView(views.LogoutView):
    template_name = None


class PasswordChangeView(views.PasswordChangeView):
    success_url = reverse_lazy('users:password_change_done')
    template_name = 'users/registration/password_change_form.html'

    def form_valid(self, form):
        self.request.session['PasswordChangeDoneView'] = True
        return super().form_valid(form)


class PasswordChangeDoneView(views.PasswordChangeDoneView):
    template_name = 'users/registration/password_change_done.html'

    def dispatch(self, request, *args, **kwargs):
        if not request.session.pop('PasswordChangeDoneView', None):
            return redirect(reverse(
                settings.IF_NOT_FOUND_SESSION_THEN_REDIRECT_TO
            ))
        return super().dispatch(request, *args, **kwargs)


class PasswordResetView(ForUnauthorizedUsersMixin, views.PasswordResetView):
    success_url = reverse_lazy('users:password_reset_done')
    email_template_name = 'users/registration/password_reset_email.html'
    template_name = 'users/registration/password_reset_form.html'

    def form_valid(self, form):
        self.request.session['PasswordResetDoneView'] = True
        return super().form_valid(form)


class PasswordResetDoneView(views.PasswordResetDoneView):
    template_name = 'users/registration/password_reset_done.html'

    def dispatch(self, request, *args, **kwargs):
        if not request.session.pop('PasswordResetDoneView', None):
            return redirect(reverse(
                settings.IF_NOT_FOUND_SESSION_THEN_REDIRECT_TO
            ))
        return super().dispatch(request, *args, **kwargs)


class PasswordResetConfirmView(views.PasswordResetConfirmView):
    success_url = reverse_lazy('users:password_reset_complete')
    template_name = 'users/registration/password_reset_confirm.html'

    def form_valid(self, form):
        self.request.session['PasswordResetCompleteView'] = True
        return super().form_valid(form)


class PasswordResetCompleteView(views.PasswordResetCompleteView):
    template_name = 'users/registration/password_reset_complete.html'

    def dispatch(self, request, *args, **kwargs):
        if not request.session.pop('PasswordResetCompleteView', None):
            return redirect(reverse(
                settings.IF_NOT_FOUND_SESSION_THEN_REDIRECT_TO
            ))
        return super().dispatch(request, *args, **kwargs)
