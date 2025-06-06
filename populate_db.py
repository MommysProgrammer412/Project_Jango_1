# Добавьте эти строки в начало файла populate_db.py
from core.models import Service, Master, Order, Review
from datetime import datetime, timedelta
from django.utils import timezone

# Создание услуг
services = [
    Service.objects.create(
        name="Мужская стрижка",
        description="Классическая мужская стрижка с укладкой",
        price=1500.00,
        duration=30,
        is_popular=True
    ),
    Service.objects.create(
        name="Стрижка машинкой",
        description="Быстрая стрижка машинкой под одну насадку",
        price=800.00,
        duration=15,
        is_popular=False
    ),
    Service.objects.create(
        name="Бритье бороды",
        description="Профессиональное бритье бороды опасной бритвой",
        price=1200.00,
        duration=20,
        is_popular=True
    ),
    Service.objects.create(
        name="Укладка волос",
        description="Стильная укладка волос с использованием профессиональных средств",
        price=700.00,
        duration=15,
        is_popular=False
    ),
    Service.objects.create(
        name="Комплекс (стрижка + борода)",
        description="Комплексная услуга: стрижка волос и оформление бороды",
        price=2500.00,
        duration=60,
        is_popular=True
    )
]

# Создание мастеров
masters = [
    Master.objects.create(
        name="Иван Петров",
        phone="+7 (999) 123-45-67",
        address="ул. Барбершопная, 1",
        experience=5,
        is_active=True
    ),
    Master.objects.create(
        name="Алексей Сидоров",
        phone="+7 (999) 987-65-43",
        address="ул. Барбершопная, 1",
        experience=3,
        is_active=True
    ),
    Master.objects.create(
        name="Дмитрий Кузнецов",
        phone="+7 (999) 555-55-55",
        address="ул. Барбершопная, 1",
        experience=7,
        is_active=True
    ),
    Master.objects.create(
        name="Михаил Иванов",
        phone="+7 (999) 111-22-33",
        address="ул. Барбершопная, 1",
        experience=2,
        is_active=False
    )
]

# Добавление услуг мастерам
# Иван выполняет все услуги
for service in services:
    masters[0].services.add(service)

# Алексей выполняет стрижки и укладки
masters[1].services.add(services[0], services[1], services[3])

# Дмитрий специализируется на бородах и комплексных услугах
masters[2].services.add(services[2], services[4])

# Михаил выполняет базовые услуги
masters[3].services.add(services[0], services[1])

# Импорт datetime для работы с датами
from datetime import datetime, timedelta
from django.utils import timezone

# Создание заказов
orders = [
    Order.objects.create(
        client_name="Петр Иванов",
        phone="+7 (999) 111-11-11",
        comment="Хочу модную стрижку",
        status="approved",
        master=masters[0],
        appointment_date=timezone.now() + timedelta(days=1, hours=2)
    ),
    Order.objects.create(
        client_name="Сергей Смирнов",
        phone="+7 (999) 222-22-22",
        comment="Нужно подровнять бороду",
        status="in_awaiting",
        master=masters[2],
        appointment_date=timezone.now() + timedelta(days=2)
    ),
    Order.objects.create(
        client_name="Андрей Козлов",
        phone="+7 (999) 333-33-33",
        status="completed",
        master=masters[1],
        appointment_date=timezone.now() - timedelta(days=1)
    ),
    Order.objects.create(
        client_name="Владимир Новиков",
        phone="+7 (999) 444-44-44",
        comment="Первый раз у вас, хочу комплексную услугу",
        status="not_approved",
        appointment_date=timezone.now() + timedelta(days=3, hours=4)
    )
]

# Добавление услуг к заказам
orders[0].services.add(services[0], services[3])  # Стрижка + укладка
orders[1].services.add(services[2])  # Бритье бороды
orders[2].services.add(services[1])  # Стрижка машинкой
orders[3].services.add(services[4])  # Комплекс

# Создание отзывов
reviews = [
    Review.objects.create(
        text="Отличная стрижка! Мастер учел все мои пожелания.",
        client_name="Петр Иванов",
        master=masters[0],
        rating=5,
        is_published=True
    ),
    Review.objects.create(
        text="Хорошо подстригли, но долго ждал своей очереди.",
        client_name="Сергей Смирнов",
        master=masters[1],
        rating=4,
        is_published=True
    ),
    Review.objects.create(
        text="Борода выглядит отлично, но цена высоковата.",
        client_name="Андрей Козлов",
        master=masters[2],
        rating=4,
        is_published=True
    ),
    Review.objects.create(
        text="Не понравилось обслуживание.",
        client_name="Владимир Новиков",
        master=masters[0],
        rating=2,
        is_published=False
    )
]

print("Тестовые данные успешно созданы!")
print(f"Создано {len(services)} услуг")
print(f"Создано {len(masters)} мастеров")
print(f"Создано {len(orders)} заказов")
print(f"Создано {len(reviews)} отзывов")