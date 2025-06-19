from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Order, Master, Service, Review
from django.shortcuts import get_object_or_404
from django.db.models import Q
from django.shortcuts import redirect
from django.contrib import messages

def landing(request):
    # Получаем всех активных мастеров из базы данных
    masters = Master.objects.filter(is_active=True).exclude(first_name="first_name").exclude(last_name="last_name")
    
    # Получаем все услуги из базы данных
    services = Service.objects.all()
    
    # Получаем отзывы
    reviews = Review.objects.all().order_by('-date_created')[:6]  # Последние 6 отзывов
    
    context = {
        "title": "Главная - Барбершоп Арбуз",
        "services": services,  # Теперь из базы данных
        "masters": masters,    # Теперь из базы данных
        "reviews": reviews,    # Новое - отзывы из базы данных
        "years_on_market": 50,
    }
    return render(request, "core/landing.html", context)


def master_detail(request, master_id):
    master = get_object_or_404(Master, id=master_id)
    return HttpResponse(f"<h1>{master.first_name} {master.last_name}</h1>")

def thanks(request):
    masters_count = Master.objects.filter(is_active=True).count()
    
    context = {
        "masters_count": masters_count,
    }
    
    return render(request, "core/thanks.html", context)


@login_required
def orders_list(request):
    if request.method == "GET":
        # Получаем все заказы, отсортированные по убыванию даты создания
        all_orders = Order.objects.select_related("master").prefetch_related("services").order_by("-date_created")
        
        # Получаем строку поиска
        search_query = request.GET.get("search", None)

        if search_query:
            # Получаем чекбоксы
            check_boxes = request.GET.getlist("search_in")
            
            # Если чекбоксы не выбраны, по умолчанию ищем по имени
            if not check_boxes:
                check_boxes = ["name"]

            # Проверяем Чекбоксы и добавляем Q объекты в запрос
            filters = Q()

            if "name" in check_boxes:
                filters |= Q(client_name__icontains=search_query)
                
            if "phone" in check_boxes:
                filters |= Q(phone__icontains=search_query)
            
            if "comment" in check_boxes:
                filters |= Q(comment__icontains=search_query)

            if filters:
                all_orders = all_orders.filter(filters)

        # Отправляем все заказы в контекст
        context = {
            "title": "Заказы",
            "orders": all_orders,
        }

        return render(request, "core/orders_list.html", context)


@login_required
def order_detail(request, pk):

    order = get_object_or_404(Order, id=pk)

    # Если заказ не найден, возвращаем 404 - данные не найдены

    context = {"title": f"Заказ №{pk}", "order": order}

    return render(request, "core/order_detail.html", context)

def add_review(request):
    if request.method == "POST":
        client_name = request.POST.get("client_name")
        master_id = request.POST.get("master_id")
        rating = request.POST.get("rating")
        text = request.POST.get("text")
        
        # Проверяем, что все необходимые поля заполнены
        if client_name and master_id and rating and text:
            try:
                # Получаем мастера по ID
                master = Master.objects.get(id=master_id)
                
                # Создаем новый отзыв
                review = Review(
                    client_name=client_name,
                    master=master,
                    rating=int(rating),
                    text=text
                )
                review.save()
                
                # Добавляем сообщение об успехе
                messages.success(request, "Спасибо за ваш отзыв! Он успешно добавлен.")
            except Master.DoesNotExist:
                messages.error(request, "Выбранный мастер не найден.")
            except Exception as e:
                messages.error(request, f"Произошла ошибка при сохранении отзыва: {str(e)}")
        else:
            messages.error(request, "Пожалуйста, заполните все обязательные поля.")
            
    # Перенаправляем на главную страницу с якорем на секцию отзывов
    return redirect("landing")