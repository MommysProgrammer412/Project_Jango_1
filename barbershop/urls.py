from django.contrib import admin
from django.urls import path, include
from core.views import main, landing

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main, name='main'),  # Оставляем основной маршрут на main
    path('barbershop/', include('core.urls')),  # Сохраняем префикс barbershop
    path('landing/', landing, name='landing'),  # Добавляем отдельный маршрут для landing
]
