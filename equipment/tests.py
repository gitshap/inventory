from django.test import TestCase
from equipment.models import Equipment


class EquipmentTestCase(TestCase):
    def setUp(self):
        Equipment.objects.create(name='Keyboard', label='KB')

    def test_equipment_get_name(self):
        """ Test if the model method `get_name` is working and returns the name"""
        equipment = Equipment.objects.get(label='KB')
        self.assertEqual(equipment.get_name, 'Keyboard')

    
