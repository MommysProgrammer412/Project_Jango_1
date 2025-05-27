from django.contrib import admin
from django.urls import path
from core.views import landing
from django.urls import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', landing, name='landing'),
    path('barbershop/', include('core.urls')),
]
