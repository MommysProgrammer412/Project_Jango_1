from django.contrib import admin
from .models import Master, Order, Service

# регистрация в одну строку в админке 
admin.site.register(Master)
admin.site.register(Order)
admin.site.register(Service)