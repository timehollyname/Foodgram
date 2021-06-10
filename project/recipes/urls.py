from django.urls import path

from . import views

app_name = 'recipes'

urlpatterns = [
    path(
        r'recipes/<int:pk>/',
        views.RecipeView.as_view(),
        name='recipe'
    ),
    path(
        r'recipes/<int:pk>/edit/',
        views.RecipeEditView.as_view(),
        name='recipeedit'
    ),
    path(
        r'recipes/<int:pk>/destroy/',
        views.RecipeDestroyView.as_view(),
        name='recipedestroy'
    ),
    path(
        r'recipes/create/',
        views.RecipeCreateView.as_view(),
        name='recipecreate'
    ),
    path(
        r'recipes/',
        views.HomeView.as_view(),
        name='home'
    ),
    path(
        r'',
        views.HomeView.as_view(),
        name='home'
    ),
]
