from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing, name='landing'),
    path('masters/<int:master_id>/', views.master_detail, name='master_detail'),
    path('thanks/', views.thanks, name='thanks'),
    path('test/', views.test, name='test'),
    path('orders/', views.orders_list, name='orders_list'),
    path('orders/<int:order_id>/', views.order_detail, name='order_detail'),
]