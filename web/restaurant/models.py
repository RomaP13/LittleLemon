from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class Booking(models.Model):
    first_name = models.CharField(max_length=100, null=False, blank=False)
    last_name = models.CharField(max_length=100, null=False, blank=False)
    email = models.EmailField()
    phone_number = PhoneNumberField(null=False, blank=False, region="UA")
    reservation_date = models.DateField(null=False, blank=False)
    reservation_time = models.IntegerField(default=10, null=False,  blank=False,
                                           validators=[MinValueValidator(10),
                                                       MaxValueValidator(20)])

    class Meta:
        verbose_name = "booking"
        verbose_name_plural = "bookings"

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.reservation_date}"


class Category(models.Model):
    title = models.CharField(max_length=100, blank=False)

    class Meta:
        verbose_name = "category"
        verbose_name_plural = "categories"

    def __str__(self):
        return self.title


class Menu(models.Model):
    title = models.CharField(max_length=100, null=False, blank=False)
    price = models.DecimalField(max_digits=10, decimal_places=2,
                                null=False, blank=False)
    menu_item_description = models.TextField(max_length=1000, default='')
    image = models.ImageField(upload_to="menus_images", null=True, blank=True)
    category = models.ForeignKey(to=Category, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "menu"
        verbose_name_plural = "menus"

    def __str__(self):
        return self.title
