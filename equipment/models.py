from django.db import models


class Equipment(models.Model):
    name = models.CharField(max_length=255)
    label = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    image = models.ImageField(upload_to="uploads/", default="default.png")
    note = models.TextField(default="Text here")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return (
            f"{self.name}({self.label}) is in {self.location} with the note {self.note}"
        )

    @property
    def get_name(self):
        return self.name
