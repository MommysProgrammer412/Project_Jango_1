from django.contrib import admin
from .models import Order, Master, Service

# регистрация в одну строку в админке
admin.site.register(Order) 
admin.site.register(Master)
admin.site.register(Service)