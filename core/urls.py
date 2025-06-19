# core/urls.py
from django.contrib import admin
from django.urls import path
from .views import master_detail, thanks, orders_list, order_detail, service_create
# Эти маршруты будут доступны с префиксом /barbershop/

urlpatterns = [
    path('masters/<int:master_id>/', master_detail),
    path('thanks/', thanks, name='thanks'),
    path('orders/', orders_list, name='orders_list'),
    path('orders/<int:order_id>/', order_detail, name='order_detail'),
    path('service_create/', service_create, name='service_create'),

]