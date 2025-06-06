from django.contrib import admin
from .models import Order, Master, Service, Review

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    """Административная панель для модели Service"""
    list_display = ['name', 'price', 'duration', 'is_popular']
    list_filter = ['is_popular']
    search_fields = ['name', 'description']

@admin.register(Master)
class MasterAdmin(admin.ModelAdmin):
    """Административная панель для модели Master"""
    list_display = ['name', 'phone', 'experience', 'is_active']
    list_filter = ['is_active', 'experience']
    search_fields = ['name', 'phone']
    filter_horizontal = ['services']

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    """Административная панель для модели Order"""
    list_display = ['client_name', 'phone', 'status', 'master', 'appointment_date', 'date_created']
    list_filter = ['status', 'date_created', 'appointment_date']
    search_fields = ['client_name', 'phone', 'comment']
    filter_horizontal = ['services']
    readonly_fields = ['date_created', 'date_updated']

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    """Административная панель для модели Review"""
    list_display = ['client_name', 'master', 'rating', 'created_at', 'is_published']
    list_filter = ['rating', 'is_published', 'created_at']
    search_fields = ['client_name', 'text']
    readonly_fields = ['created_at']