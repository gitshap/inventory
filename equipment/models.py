from decimal import MAX_EMAX
from django.db import models



# Staff names, email to be assigned to equipment/license
class Staff(models.Model):
    name = models.CharField(max_length=255, unique=True)
    email = models.CharField(max_length=255)
    designation = models.CharField(max_length=255, blank=True)
    anydesk_id = models.CharField(max_length=15, blank=True)

    def check_if_deployed(self):
        shap = Staff.objects.get(id=1)
        # 1 = SHAP/Default
        if self.owner == shap:
            return False
        else:
            return True

    
    def __str__(self):
        return f'{self.name}'
    


class Component(models.Model):
    name_of_component = models.CharField(max_length=255)
    model_number = models.CharField(max_length=255)
    quantity = models.IntegerField(default=0)
    is_disposed = models.BooleanField(default=False)
    owner = models.ForeignKey(Staff, on_delete=models.CASCADE, default=1)



    def check_if_deployed(self):
        shap = Staff.objects.get(id=1)
        # 1 = SHAP/Default
        if self.owner == shap:
            return False
        else:
            return True
    def count_deployed(self):
        shap = Staff.objects.get(id=1)
        return Component.objects.filter(owner=shap).count()

    def __str__(self):
        return f'{self.name_of_component} - {self.quantity} pcs'

    
class Equipment(models.Model):
    """ Equipment Model """

    WORKING = 'WORKING'
    TO_BE_REPAIRED = 'TO BE REPAIRED'
    BROKEN = 'BROKEN'

    STATUS_CHOICES = [
        (WORKING, 'WORKING'),
        (TO_BE_REPAIRED, 'TO BE REPAIRED'),
        (BROKEN, 'BROKEN')
    ]
    name = models.CharField(max_length=255)
    label = models.CharField(max_length=255, primary_key=True)
    location = models.CharField(max_length=255)
    image = models.ImageField(upload_to="uploads/", default="default.png")
    note = models.TextField(default="Text here")
    date_created = models.DateField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=30, choices=STATUS_CHOICES)
    owner = models.ForeignKey(Staff, on_delete=models.CASCADE, default=1)
    is_disposed = models.BooleanField(default=False)
    components = models.ManyToManyField(Component)
    

    def __str__(self):
        return (
            f"{self.name}({self.label}) is in {self.location} with the note {self.note} with components {self.components}"
        )

    @property
    def get_name(self):
        return self.name

    @property
    def get_status(self):
        return f'{self.name}-{self.label} is with the status of {self.status}'

    def check_if_deployed(self):
        shap = Staff.objects.get(id=1)
        # 1 = SHAP/Default
        if self.owner == shap:
            return False
        else:
            return True


    def count_deployed(self):
        shap = Staff.objects.get(id=1)
        return Equipment.objects.filter(owner=shap).count()
        


class License(models.Model):
    name = models.CharField(max_length=255)
    key = models.CharField(max_length=100)
    owner = models.ForeignKey(Staff, on_delete=models.CASCADE, default=1)
    is_assigned = models.BooleanField(default=False)

    def check_if_deployed(self):
        if self.is_assigned is True:
            return True
        else:
            return False
            
    def count_deployed(self):
        return License.objects.filter(is_assigned=False).count()


    def __str__(self):
        return f'{self.owner} has current ownership of {self.name} with the key {self.key}'


class Consumable(models.Model):
    name = models.CharField(max_length=255)
    owner = models.ForeignKey(Staff, on_delete=models.CASCADE, default=1)
    quantity = models.IntegerField(default=0)
    is_assigned = models.BooleanField(default=False)


    def check_if_deployed(self):
        shap = Staff.objects.get(id=1)
        # 1 = SHAP/Default
        if self.owner == shap:
            return False
        else:
            return True

            
    def count_deployed(self):
        shap = Staff.objects.get(id=1)
        return Consumable.objects.filter(owner=shap).count()

    def __str__(self):
        return f'{self.name}/{self.quantity} items'


