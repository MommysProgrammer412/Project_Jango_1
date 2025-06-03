# core/urls.py
from django.contrib import admin
from django.urls import path
from .views import landing, master_detail, thanks, test, orders_list, order_detail

urlpatterns = [
    path('', landing, name='landing'),
    path('thanks/', thanks, name='thanks'),
    path('orders/', orders_list, name='orders_list'),
    path('orders/<int:order_id>/', order_detail, name='order_detail'),
    path('test/', test),
]