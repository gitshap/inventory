from datetime import datetime
from decimal import MAX_EMAX
from email.policy import default
from django.db import IntegrityError, models
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ObjectDoesNotExist

from random import randint, random


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

    class Status(models.TextChoices):
        WORKING = 'OK', _('Working')
        TO_BE_REPAIRED = 'TBD', _('To be repaired')
        DISPOSED = 'DP', _('Disposed')

  
    name_of_component = models.CharField(max_length=255)
    asset_tag = models.CharField(max_length=30, unique=True, default='SHAP', blank=True, null=True)
    date_purchased = models.DateField(blank=True, default=datetime.now)
    date_deprecated = models.DateField(blank=True, default=datetime.now)
    status = models.CharField(max_length=4,
                choices=Status.choices,
                default=Status.WORKING)

    in_use = models.BooleanField(default=False)


    def __str__(self):
        return f'{self.asset_tag} - {self.name_of_component}'

    def is_in_use(self):
        if self.in_use == True:
            return False

    def save(self, *args, **kwargs):
        random_number = randint(1, 500000)
        another_number = randint(500000, 999999)
        
        try:
            tag = Component.objects.latest('asset_tag')
            if Component.objects.get(asset_tag=tag.asset_tag):
                self.asset_tag = 'SC-' + str(random_number)
                super(Component, self).save(*args, **kwargs)
            else:
                self.asset_tag = 'SC-' + str(random_number)
                super(Component, self).save(*args, **kwargs)
                print("There was a constraint")
        except IntegrityError:
            self.asset_tag = 'SC-' + str(random_number)
            print("There was a constraint")
        except ObjectDoesNotExist:
            self.asset_tag = 'SC-' + str(another_number)
            print('New One')
        super(Component, self).save(*args, **kwargs)


    
class Equipment(models.Model):
    """ Equipment Model """

    class Status(models.TextChoices):
        WORKING = 'OK', _('Working')
        TO_BE_REPAIRED = 'TBD', _('To be repaired')
        DISPOSED = 'DP', _('Disposed')


    owner = models.ForeignKey(Staff, on_delete=models.CASCADE)
     
    asset_tag = models.CharField(max_length=30, unique=True, default='shap', null=True, blank=True)
    name = models.CharField(max_length=255)
    status = models.CharField(max_length=5,
                choices=Status.choices,
                default=Status.WORKING)
    date_purchased = models.DateField(blank=True, default=datetime.now)
    date_deprecated = models.DateField(blank=True, default=datetime.now)

    components = models.ManyToManyField(Component, blank=True)


    def is_working(self):
        if self.status == 'OK':
            return True

    def __str__(self):
        return f'{self.name} {self.asset_tag}'

    def save(self, *args, **kwargs):
        random_number = randint(1, 500000)
        another_number = randint(500000, 999999)
        
        
        try:
            tag = Equipment.objects.latest('asset_tag')
            print(tag.asset_tag)
            if Equipment.objects.get(asset_tag=tag.asset_tag):
                self.asset_tag = 'SE-' + str(random_number)
                super(Equipment, self).save(*args, **kwargs)
                print('Goes here?')
            else:
                self.asset_tag = 'SE-' + str(random_number)
                super(Equipment, self).save(*args, **kwargs)
                print("There was a constraint2")
        except IntegrityError:
            self.asset_tag = 'SE-' + str(another_number)
            super(Equipment, self).save(*args, **kwargs)
            print("There was a IntegrityError")
            print(self.asset_tag)
        except ObjectDoesNotExist:
            self.asset_tag = 'SE-' + str(another_number)
            print('New One')
        super(Equipment, self).save(*args, **kwargs)

    
        


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


