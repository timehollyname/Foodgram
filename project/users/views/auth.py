from django.contrib.auth import views
from django.urls import reverse_lazy


class SignInView(views.LoginView):
    template_name = 'users/registration/signin.html'


class LogoutView(views.LogoutView):
    template_name = None


class PasswordChangeView(views.PasswordChangeView):
    success_url = reverse_lazy('users:password_change_done')
    template_name = 'users/registration/password_change_form.html'


class PasswordChangeDoneView(views.PasswordChangeDoneView):
    template_name = 'users/registration/password_change_done.html'


class PasswordResetView(views.PasswordResetView):
    success_url = reverse_lazy('users:password_reset_done')
    template_name = 'users/registration/password_reset_form.html'


class PasswordResetDoneView(views.PasswordResetDoneView):
    template_name = 'users/registration/password_reset_done.html'


class PasswordResetConfirmView(views.PasswordResetConfirmView):
    success_url = reverse_lazy('users:password_reset_complete')
    template_name = 'users/registration/password_reset_confirm.html'


class PasswordResetCompleteView(views.PasswordResetCompleteView):
    template_name = 'users/registration/password_reset_complete.html'
