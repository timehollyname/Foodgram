from django.urls import include, path
from rest_framework.routers import DefaultRouter

from . import views

app_name = 'api'

router_v1 = DefaultRouter()

router_v1.register(
    r'favorites', views.FavoriteViewSet, basename='favorites')
router_v1.register(
    r'ingredients', views.IngredientViewSet, basename='ingredients')
router_v1.register(
    r'subscriptions', views.SubscriptionViewSet, basename='subscriptions')
router_v1.register(
    r'purchases', views.PurchasesViewSet, basename='purchases')

urlpatterns = [
    path('v1/', include(router_v1.urls)),
]
