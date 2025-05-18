from django.contrib import admin
from django.urls import path
from core.views import master_detail, thanks

urlpatterns = [
    path('masters/<int:master_id>/', master_detail),
    path('thanks/', thanks),
    
]