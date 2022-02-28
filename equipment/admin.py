
from django.contrib import admin
from equipment.models import Component, Equipment, License, Staff, Consumable

admin.site.register(Equipment)
admin.site.register(Staff)
admin.site.register(License)
admin.site.register(Component)
admin.site.register(Consumable)