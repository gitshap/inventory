from django.urls import path
from equipment.views import equipment_view, csv_to_import, list_users ,home_view, login_view, licenses_view, list_equipments

urlpatterns = [
    path('', home_view, name='home_view'),
    path('csv/', csv_to_import, name='csv_importer'),
    path('login/', login_view, name='login_view'),
    path('equipment/<str:label>/', equipment_view, name='equipment-view'),
    path('licenses/', licenses_view, name='list_licenses'),
    path('equipments/', list_equipments, name='list_equipments'),
    path('users/', list_users, name='list_users'),
    
]

