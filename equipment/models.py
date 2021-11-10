from django.db import models
from datetime import datetime
from django.utils import timezone

class Equipment(models.Model):
    """ Equipment Model """
    name = models.CharField(max_length=255)
    label = models.CharField(max_length=255, unique=True)
    location = models.CharField(max_length=255)
    image = models.ImageField(upload_to="uploads/", default="default.png")
    note = models.TextField(default="Text here")


    def __str__(self):
        return (
            f"{self.name}({self.label}) is in {self.location} with the note {self.note}"
        )

    @property
    def get_name(self):
        return self.name


# TODO: Create disposable model
