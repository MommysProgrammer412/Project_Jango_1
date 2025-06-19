# core/urls.py
from django.contrib import admin
from django.urls import path
from .views import landing, master_detail, thanks, orders_list, order_detail, add_review
# Эти маршруты будут доступны с префиксом /barbershop/

urlpatterns = [
    path('', landing, name='landing'),
    path('masters/<int:master_id>/', master_detail, name='master_detail'),
    path('thanks/', thanks, name='thanks'),
    path('orders/', orders_list, name='orders_list'),
    path('orders/<int:pk>/', order_detail, name='order_detail'),
    path('add-review/', add_review, name='add_review'),
]