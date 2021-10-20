from django.urls import path
from equipment.views import hello, equipment_view



urlpatterns = [
    path('', hello, name='hello'), 
    path('equipment/<int:pk>/', equipment_view, name='equipment-view')
]
