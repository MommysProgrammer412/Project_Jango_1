from django.contrib import admin
from django.urls import path
from core.views import landing, master_detail, thanks, test, orders_list, order_detail

urlpatterns = [
    path('admin/', admin.site.urls),  # Добавил стандартный путь к админке
    path('', landing, name='landing'),
    path('masters/<int:master_id>/', master_detail, name='master_detail'),
    path('thanks/', thanks, name='thanks'),
    path('test/', test, name='test'),  # Добавил путь к функции test
    path('orders/', orders_list, name='orders_list'),
    path('orders/<int:order_id>/', order_detail, name='order_detail'),
]