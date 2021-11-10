from django.urls import path
from equipment.views import equipment_view, csv_to_import, home_view

urlpatterns = [
    path('', home_view, name='home_view'),
    path('csv/', csv_to_import, name='csv_importer'),
    path('equipment/<str:label>/', equipment_view, name='equipment-view')
]

