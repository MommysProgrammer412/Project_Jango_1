from django.shortcuts import render
from django.http import HttpResponse
from .data import *

masters = [
    {"id": 1, "name": "Эльдар 'Бритва' Рязанов"},
    {"id": 2, "name": "Зоя 'Ножницы' Космодемьянская"},
    {"id": 3, "name": "Борис 'Фен' Пастернак"},
    {"id": 4, "name": "Иннокентий 'Лак' Смоктуновский"},
    {"id": 5, "name": "Раиса 'Бигуди' Горбачёва"},
]

def main(request):
    return HttpResponse("""
<h1>Добро пожаловать в наш барbershop!</h1>
<p>Мы предлагаем широкий выбор услуг для вашего путешествия.</p>
""")

def master_detail(request, master_id):
    try:
        master = [m for m in masters if m['id'] == master_id][0]
    except IndexError:
        return HttpResponse('Мастера не найдено')
    return HttpResponse(f"<h1>{master['name']}</h1>")

def thanks(request):
    masters_count = len(masters)
    context = {'masters_count': masters_count}
    return render(request, 'thanks.html', context)

def test(request):
    class Employee:
        def __init__(self, name, is_active):
            self.name = name
            self.is_active = is_active
       
        def __str__(self):
            return f'Экземпляр класса {self.__class__.__name__} с именем {self.name}'
       
        def say_my_name(self):
            return f'Меня зовут {self.name}'
    
    employee = Employee('Алевтина', True)

    context = {
        'string': 'Мастер по усам',
        'number': 42,
        'list_': ['Стрижка бороды', 'Усы-таракан', 'Укладка бровей'],
        'dict_': {'best_master': 'Алевтина Арбузова'},
        'employee': employee,
    }
    return render(request, 'test.html', context)