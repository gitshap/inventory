from django.db import models


class Equipment(models.Model):
    """ Equipment Model """

    WORKING = 'WORKING'
    TO_BE_REPAIRED = 'TO_BE_REPAIRED'
    BROKEN = 'BROKEN'

    STATUS_CHOICES = [
        (WORKING, 'WORKING'),
        (TO_BE_REPAIRED, 'TO_BE_REPAIRED'),
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

    # TODO: Create Owner

    def __str__(self):
        return (
            f"{self.name}({self.label}) is in {self.location} with the note {self.note}"
        )

    @property
    def get_name(self):
        return self.name

    @property
    def get_status(self):
        return f'{self.name}-{self.label} is with the status of {self.status}'


class Disposable(models.Model):
    name = models.CharField(max_length=255)
    date_disposed = models.DateTimeField(auto_now_add=True)
    # TODO: CREATE MORE FIELDS FOR THE DISPOSABLE FIELD AND MIGRATE

    def __str__(self):
        return self.name

class Staff(models.Model):
    name = models.CharField(max_length=255, unique=True)
    email = models.CharField(max_length=255)
    designation = models.CharField(max_length=255, blank=True)
    def __str__(self):
        return f'Staff Name: {self.name}, Email: {self.email}'

class Licenses(models.Model):
    name = models.CharField(max_length=255)
    key = models.CharField(max_length=100)

    owner = models.ForeignKey(Staff, on_delete=models.CASCADE)
    status = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.owner} has current ownership of {self.name} with the key {self.key}'


