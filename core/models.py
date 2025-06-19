from doctest import master
from django.db import models
"""

"""


class Order(models.Model):

    # Статусы заказов
    STATUS_CHOICES = [
        ("not_approved", "Не подтвержден"),
        ("moderated", "Прошел модерацию"),
        ("spam", "Спам"),
        ("approved", "Подтвержден"),
        ("in_awaiting", "В ожидании"),
        ("completed", "Завершен"),
        ("canceled", "Отменен"),
    ]

    client_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    comment = models.TextField(blank=True)
    
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default="not_approved")
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    # Один ко многим
    master = models.ForeignKey("Master", on_delete=models.SET_NULL, null=True, related_name="orders")
    services = models.ManyToManyField("Service", related_name="orders", blank=True)
    appointment_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f"Заказ {self.id} от {self.client_name}"
    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"
        # сортитровка по умолчанию (- это по убыванию)
        ordering = ["-date_created"]

        indexes = [
            # Индекс по полю status
            models.Index(fields=['status'], name='status_idx'),
            # Индекс по полю date_created (хотя для сортировки он может создаться и так,
            # но явное указание не повредит и поможет при фильтрации)
            models.Index(fields=['date_created'], name='created_at_idx'),
            # Пример составного индекса, если бы мы часто искали заказы мастера за период
            # models.Index(fields=['client_name', 'phone'], name='master_created_idx'),
        ]

class Master(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to="images/masters/", blank=True, null=True)
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=255)
    email = models.EmailField(blank=True)
    experience = models.PositiveIntegerField()
    # Многие ко многим
    services = models.ManyToManyField("Service", related_name="masters")
    is_active = models.BooleanField(default=True)
    
    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"
    
    def __str__(self):
        return self.get_full_name()


class Service(models.Model):
    name = models.CharField(max_length=200, verbose_name="Название услуги")
    description = models.TextField(verbose_name="Описание услуги")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена услуги")
    duration = models.PositiveIntegerField(help_text="Время в минутах", verbose_name="Время выполнения услуги")
    is_popular = models.BooleanField(default=False, verbose_name="Популярная услуга")
    image = models.ImageField(upload_to="images/services/", blank=True, null=True, verbose_name="Изображение услуги")

    def __str__(self):
        return f"{self.name} - {self.price} руб."

    
    class Meta:
        verbose_name = "Услуга"
        verbose_name_plural = "Услуги"

class Review(models.Model):
    client_name = models.CharField(max_length=100, verbose_name="Имя клиента")
    text = models.TextField(verbose_name="Текст отзыва")
    rating = models.IntegerField(
        choices=[(i, str(i)) for i in range(1, 6)],
        default=5,
        verbose_name="Оценка"
    )
    master = models.ForeignKey(
        "Master", 
        on_delete=models.CASCADE, 
        related_name="reviews",
        verbose_name="Мастер"
    )
    date_created = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"
        ordering = ["-date_created"]

    def __str__(self):
        return f"Отзыв от {self.client_name} о мастере {self.master.first_name} {self.master.last_name}"