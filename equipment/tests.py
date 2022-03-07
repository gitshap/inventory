from django.test import TestCase
from equipment.models import Equipment, Consumable, Staff



    
class ConsumableTestCase(TestCase):
    def setUp(self):
        Staff.objects.create(name='SHAP', email='shap@smail.com')
        Consumable.objects.create(name='Printer Ink', quantity=50)

    def test_consumable_is_created(self):
        consumable = Consumable.objects.get(name='Printer Ink')
        self.assertEqual(consumable.name, 'Printer Ink')