from django.contrib import admin
from django.urls import path
from core.views import master_detail, thanks, test, orders_list, order_detail

urlpatterns = [
    path('masters/<int:master_id>/', master_detail),
    path('thanks/', thanks, name='thanks'),
    path('orders/', orders_list, name='orders_list'),
    path('orders/<int:order_id>/', order_detail, name='order_detail'),
]