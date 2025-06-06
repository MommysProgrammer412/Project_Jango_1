from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Service(models.Model):
    """
    Модель для представления услуг барбершопа.
    
    Attributes:
        name (str): Название услуги
        description (str): Описание услуги
        price (Decimal): Цена услуги
        duration (int): Длительность выполнения услуги в минутах
        is_popular (bool): Флаг популярности услуги
        image (ImageField): Изображение услуги
    """
    name = models.CharField(max_length=200, verbose_name="Название")
    description = models.TextField(blank=True, verbose_name="Описание")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена")
    duration = models.PositiveIntegerField(verbose_name="Длительность", help_text="Время выполнения в минутах")
    is_popular = models.BooleanField(default=False, verbose_name="Популярная услуга")
    image = models.ImageField(upload_to="services/", blank=True, null=True, verbose_name="Изображение")
    
    class Meta:
        verbose_name = "Услуга"
        verbose_name_plural = "Услуги"
    
    def __str__(self):
        return self.name


class Master(models.Model):
    """
    Модель для представления мастеров барбершопа.
    
    Attributes:
        name (str): Имя мастера
        photo (ImageField): Фотография мастера
        phone (str): Телефон мастера
        address (str): Адрес мастера
        experience (int): Стаж работы в годах
        services (ManyToManyField): Связь с услугами, которые выполняет мастер
        is_active (bool): Статус активности мастера
    """
    name = models.CharField(max_length=150, verbose_name="Имя", default="Неизвестный мастер")
    photo = models.ImageField(upload_to="masters/", blank=True, null=True, verbose_name="Фотография")
    phone = models.CharField(max_length=20, verbose_name="Телефон")
    address = models.CharField(max_length=255, verbose_name="Адрес")
    experience = models.PositiveIntegerField(verbose_name="Стаж работы", help_text="Опыт работы в годах")
    services = models.ManyToManyField(Service, related_name="masters", verbose_name="Услуги")
    is_active = models.BooleanField(default=True, verbose_name="Активен")
    
    class Meta:
        verbose_name = "Мастер"
        verbose_name_plural = "Мастера"
    
    def __str__(self):
        return self.name


class Order(models.Model):
    """
    Модель для представления заказов клиентов.
    
    Attributes:
        client_name (str): Имя клиента
        phone (str): Телефон клиента
        comment (str): Комментарий к заказу
        status (str): Статус заказа
        date_created (datetime): Дата создания заказа
        date_updated (datetime): Дата обновления заказа
        master (ForeignKey): Связь с мастером, который выполняет заказ
        services (ManyToManyField): Связь с услугами, которые включены в заказ
        appointment_date (datetime): Дата и время записи
    """
    STATUS_CHOICES = [
        ("not_approved", "Не подтвержден"),
        ("moderated", "Прошел модерацию"),
        ("spam", "Спам"),
        ("approved", "Подтвержден"),
        ("in_awaiting", "В ожидании"),
        ("completed", "Завершен"),
        ("canceled", "Отменен")
    ]
    
    client_name = models.CharField(max_length=100, verbose_name="Имя клиента")
    phone = models.CharField(max_length=20, verbose_name="Телефон")
    comment = models.TextField(blank=True, verbose_name="Комментарий")
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default="not_approved", verbose_name="Статус")
    date_created = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    date_updated = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")
    master = models.ForeignKey(Master, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Мастер")
    services = models.ManyToManyField(Service, related_name="orders", verbose_name="Услуги")
    appointment_date = models.DateTimeField(null=True, blank=True, verbose_name="Дата и время записи")
    
    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"
    
    def __str__(self):
        return f"Заказ {self.id} от {self.client_name}"


class Review(models.Model):
    """
    Модель для представления отзывов клиентов.
    
    Attributes:
        text (str): Текст отзыва
        client_name (str): Имя клиента
        master (ForeignKey): Связь с мастером, о котором оставлен отзыв
        photo (ImageField): Фотография к отзыву
        created_at (datetime): Дата создания отзыва
        rating (int): Оценка от 1 до 5
        is_published (bool): Статус публикации отзыва
    """
    text = models.TextField(verbose_name="Текст отзыва")
    client_name = models.CharField(max_length=100, blank=True, verbose_name="Имя клиента")
    master = models.ForeignKey(Master, on_delete=models.CASCADE, verbose_name="Мастер")
    photo = models.ImageField(upload_to="reviews/", blank=True, null=True, verbose_name="Фотография")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    rating = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)],
        verbose_name="Оценка"
    )
    is_published = models.BooleanField(default=True, verbose_name="Опубликован")
    
    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"
    
    def __str__(self):
        return f"Отзыв от {self.client_name} о мастере {self.master}"