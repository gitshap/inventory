from django.db import models


class Equipment(models.Model):
    name = models.CharField(max_length=255)
    label = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    image = models.ImageField(upload_to ='uploads/')

    def __str__(self):
        return f"{self.name}({self.label}) is in {self.location}"
