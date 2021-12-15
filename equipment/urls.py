from django.urls import path
from equipment.views import equipment_view, csv_to_import, home_view, login_view

urlpatterns = [
    path('', home_view, name='home_view'),
    path('csv/', csv_to_import, name='csv_importer'),
    path('login/', login_view, name='login_view'),
    path('equipment/<str:label>/', equipment_view, name='equipment-view')
]

