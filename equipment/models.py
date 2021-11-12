from django.db import models
from datetime import datetime
import uuid



class Equipment(models.Model):
    """ Equipment Model """
    name = models.CharField(max_length=255)
    label = models.CharField(max_length=255, primary_key=True)
    location = models.CharField(max_length=255)
    image = models.ImageField(upload_to="uploads/", default="default.png")
    note = models.TextField(default="Text here")
    date_created = models.DateField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)


    def __str__(self):
        return (
            f"{self.name}({self.label}) is in {self.location} with the note {self.note}"
        )

    @property
    def get_name(self):
        return self.name


# TODO: Create disposable model
