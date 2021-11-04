import csv
from django.urls import path
from equipment.views import hello, equipment_view, csv_to_import



urlpatterns = [
    path('', hello, name='hello'), 
    path('csv/', csv_to_import, name='csv_importer'), 
    path('equipment/<str:label>/', equipment_view, name='equipment-view')
]
