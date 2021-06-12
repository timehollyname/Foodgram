from django.urls import path

from . import views

app_name = 'users'

urlpatterns = [
    path(
        r'signup/',
        views.SignUpView.as_view(),
        name='signup'
    ),
    path(
        r'signin/',
        views.SignInView.as_view(),
        name='signin'
    ),
    path(
        r'logout/',
        views.LogoutView.as_view(),
        name='logout'
    ),

    path(
        r'password/change/',
        views.PasswordChangeView.as_view(),
        name='password_change'
    ),
    path(
        r'password/change/done/',
        views.PasswordChangeDoneView.as_view(),
        name='password_change_done'
    ),

    path(
        r'password/reset/',
        views.PasswordResetView.as_view(),
        name='password_reset'
    ),
    path(
        r'password/reset/done/',
        views.PasswordResetDoneView.as_view(),
        name='password_reset_done'
    ),
    path(
        r'reset/<uuid:uidb64>/<token>/',
        views.PasswordResetConfirmView.as_view(),
        name='password_reset_confirm'
    ),
    path(
        r'reset/done/',
        views.PasswordResetCompleteView.as_view(),
        name='password_reset_complete'
    ),

    path(
        r'favorites/',
        views.FavoritesView.as_view(),
        name='favorites'
    ),
    path(
        r'purchases/',
        views.PurchasesView.as_view(),
        name='purchases'
    ),
    path(
        r'purchases/pdf/',
        views.PurchasesPdfView.as_view(),
        name='purchases_pdf'
    ),
    path(
        r'subscriptions/',
        views.SubscriptionsView.as_view(),
        name='subscriptions'
    ),
    path(
        r'<str:username>/',
        views.RecipesView.as_view(),
        name='recipes'
    ),
]
