from django.contrib import admin
from django.urls import path
from core.views import landing
from django.urls import include
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', landing, name='landing'),
    path('barbershop/', include('core.urls')),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns