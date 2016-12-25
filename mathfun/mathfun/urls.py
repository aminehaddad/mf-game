from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings

urlpatterns = []

if settings.DJANGO_ADMIN_ENABLED:
    urlpatterns += [
        url(r'^admin/', admin.site.urls),
    ]

urlpatterns += [
    url(r'', include('mf_game.urls')),
]
