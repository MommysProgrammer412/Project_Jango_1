from django.shortcuts import render
from .data import masters, services, orders

def landing(request):
    """Главная страница (лендинг)"""
    context = {
        'masters': masters,
        'services': services,
    }
    return render(request, 'landing.html', context)

def master_detail(request, master_id):
    """Страница мастера"""
    master = next((m for m in masters if m['id'] == master_id), None)
    context = {'master': master}
    return render(request, 'core/master_detail.html', context)

def thanks(request):
    """Страница благодарности за заявку"""
    masters_count = len(masters)
    context = {'masters_count': masters_count}
    return render(request, 'core/thanks.html', context)

def test(request):
    """Тестовая страница"""
    return render(request, 'test.html')

def orders_list(request):
    """Список всех заявок"""
    context = {
        'orders': orders,
        'title': 'Список заказов'
    }
    return render(request, 'core/orders_list.html', context)

def order_detail(request, order_id):
    """Детали конкретной заявки"""
    # Найдем заявку по ID
    order = next((order for order in orders if order['id'] == order_id), None)
    
    # Найдем мастера для этой заявки
    master = next((master for master in masters if master['id'] == order['master_id']), None) if order else None
    
    context = {
        'order': order,
        'master': master,
    }
    return render(request, 'core/order_detail.html', context)