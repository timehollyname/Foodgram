import debug_toolbar
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('__debug__/', include(debug_toolbar.urls)),

    path('admin/', admin.site.urls),
    path('api/', include('api.urls', namespace='api')),
    path('users/', include('users.urls', namespace='users')),
    path('', include('recipes.urls', namespace='recipes')),
]
