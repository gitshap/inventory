from django.urls import path
from equipment.views import hello, equipment_view



urlpatterns = [
    path('', hello, name='hello'), 
    path('equipment/<str:label>/', equipment_view, name='equipment-view')
]
