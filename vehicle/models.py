from django.db import models

class Vehicle(models.Model):
    model = models.CharField(max_length=50)
    year = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.model} ({self.year})"

