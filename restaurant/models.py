from django.db import models


class Booking(models.Model):
    name = models.CharField(max_length=100)
    no_of_guests = models.PositiveIntegerField()
    bookingDate = models.DateField()

    def __str__(self):
        return f"{self.name} - {self.no_of_guests} - {self.bookingDate}"


class Menu(models.Model):
    title = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    inventory = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.title} - {self.price} - {self.inventory}"
