from django.urls import path
from equipment.views import (
     checkout_consumable, create_consumable, delete_consumable, detail_consumable, equipment_view, csv_to_import, list_users ,home_view, login_view, licenses_view, list_equipments, search_consumable, search_user, staff_profile, update_consumable, view_consumable, view_deployed,
     
)


# license views
from equipment.licenses import create_license, update_license
from equipment.equipment_views import create_equipment

urlpatterns = [
    path('', home_view, name='home_view'),
    path('csv/', csv_to_import, name='csv_importer'),
    path('login/', login_view, name='login_view'),
    path('equipment/<str:label>/', equipment_view, name='equipment-view'),
    path('licenses/', licenses_view, name='list_licenses'),
    path('equipments/', list_equipments, name='list_equipments'),
    path('users/', list_users, name='list_users'),



    # license views
    path('license/create_license/', create_license, name='create_license'),
    path('license/update_license/<int:pk>', update_license, name='update_license'),


    # consumable views
    path('consumable/create_consumable/', create_consumable, name='create_consumable'),
    path('consumable/view_consumable/', view_consumable, name='view_consumable'),
    path('consumable/deployed/', view_deployed, name='view_deployed'),
    path('consumable/checkout_consumable/<int:id>', checkout_consumable, name='checkout_consumable'),
    path('consumable/update_consumable/<int:id>', update_consumable, name='update_consumable'),
    path('consumable/delete_consumable/<int:id>', delete_consumable, name='delete_consumable'),
    path('consumable/detail_consumable/<int:id>', detail_consumable, name='detail_consumable'),
    path('consumable/search_consumable/', search_consumable, name='search_consumable'),


    # staff views
    path('staff/profile/<int:id>/', staff_profile, name='staff_profile'),
    path('staff/search_user/', search_user, name='search_user'),
    

    # Equipment views
    path('equipment/create_equipment', create_equipment, name='create_equipment'),
    
]

