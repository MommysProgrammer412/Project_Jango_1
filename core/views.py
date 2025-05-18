from django.shortcuts import render
from django.http import HttpResponse


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
    return render(request, 'thanks.html')
