from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.flatpages import views
from django.urls import include, path

urlpatterns = [
    path(r'admin/', admin.site.urls),
    path(r'pages/', include('django.contrib.flatpages.urls')),
    path(r'api/', include('api.urls', namespace='api')),
    path(r'users/', include('users.urls', namespace='users')),
    path(r'', include('recipes.urls', namespace='recipes')),
]

urlpatterns += [
    path(
        r'about-author/', views.flatpage, {'url': '/about-author/'},
        name='about-author'),
    path(
        r'about-spec/', views.flatpage, {'url': '/about-spec/'},
        name='about-spec'),
]

handler400 = 'foodgram.views.page_bad_request'
handler404 = 'foodgram.views.page_not_found'
handler500 = 'foodgram.views.server_error'

if settings.DEBUG:
    import debug_toolbar

    urlpatterns += [
        path(r'__debug__/', include(debug_toolbar.urls))
    ]

    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT)

    urlpatterns += static(
        settings.STATIC_URL,
        document_root=settings.STATIC_ROOT)
