from django.shortcuts import render
from django.http import HttpResponse
from .data import masters, services, orders, MENU_ITEMS

def main(request):
    """Главная страница (лендинг)"""
    context = {
        'masters': masters,
        'services': services,
    }
    return render(request, 'base.html', context)

def landing(request):
    """Главная страница (лендинг)"""
    context = {
        'masters': masters,
        'services': services,
    }
    return render(request, 'landing.html', context)

def thanks(request):
    """Страница благодарности за заявку"""
    masters_count = len(masters)
    context = {
        'masters_count': masters_count,
        'menu_items': MENU_ITEMS
    }
    return render(request, 'core/thanks.html', context)

def orders_list(request):
    """Список всех заявок"""
    context = {
        'orders': orders,
        'title': 'Список заказов'
    }
    return render(request, 'core/orders_list.html', context)

def order_detail(request, order_id):
    """Детали конкретной заявки"""
    try:
        order = [o for o in orders if o['id'] == order_id][0]
    except IndexError:
        return HttpResponse(status=404)
    
    # Найдем мастера для этой заявки
    master = next((master for master in masters if master['id'] == order['master_id']), None) if order else None
    
    context = {
        'title': f'заказ №{order_id}',
        'order': order,
        'master': master,
    }
    return render(request, 'core/order_detail.html', context)

def master_detail(request, master_id):
    """Детали конкретного мастера"""
    try:
        master = [m for m in masters if m['id'] == master_id][0]
    except IndexError:
        return HttpResponse('Мастера не найдено')
    return HttpResponse(f"<h1>{master['name']}</h1>")

class Employee:
    def __init__(self, name: str, is_active: bool, is_married: bool, age: int, salary: float, position: str, hobbies: list):
        self.name = name
        self.is_active = is_active
        self.is_married = is_married
        self.age = age
        self.salary = salary
        self.position = position
        self.hobbies = hobbies

    def __str__(self):
        return f'Имя: {self.name}.\nВозраст: {self.age}.\nЗарплата: {self.salary}.\nДолжность: {self.position}.'

def test(request):
    employee = Employee('Алевтина', True, True, 42, 100000, 'manager', ['Журналы про усы', 'Компьютерные игры', 'Пиво'])
    employee2 = Employee('Бородач', True, False, 25, 50000, 'master', ['Садоводство', 'Пиво', 'Компьютерные игры'])
    employee3 = Employee("Барбарис", True, False, 30, 60000, 'master', ['Газонокосилки', 'Пиво', 'Стрельба из арбалета'])
    employee4 = Employee("Сифон", True, True, 35, 70000, 'master', ['Брендовый шмот', 'Походы в ГУМ', 'Аниме'])

    employees = [employee, employee2, employee3, employee4]

    context = {
        'string': 'Мастер по усам',
        'number': 42,
        'list_': ['Стрижка бороды', 'Усы-таракан', 'Укладка бровей'],
        'dict_': {'best_master': 'Алевтина Арбузова'},
        'employee': employee,
        'employee2': employee2,
        'employees': employees
    }
    return render(request, 'test.html', context)