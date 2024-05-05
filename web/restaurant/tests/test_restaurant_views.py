from decimal import Decimal

from django.core.cache import cache
from django.test import Client, TestCase, SimpleTestCase
from django.urls import reverse
from rest_framework import status

from restaurant.forms import BookingForm
from restaurant.models import Booking
from restaurant.utils import create_category, create_menu


class HomeAboutViewTest(SimpleTestCase):
    def setUp(self):
        self.client = Client()

    def test_home_view(self):
        response = self.client.get(reverse("restaurant:home"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTemplateUsed(response, "index.html")

    def test_about_view(self):
        response = self.client.get(reverse("restaurant:about"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTemplateUsed(response, "about.html")


class BookingViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.booking = reverse("restaurant:booking")

    def test_booking_view_get(self):
        response = self.client.get(self.booking)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTemplateUsed(response, "booking.html")
        self.assertIsInstance(response.context["form"], BookingForm)

    def test_booking_view_post(self):
        form_data = {
            "first_name": "John",
            "last_name": "Doe",
            "email": "john@example.com",
            "phone_number": "+380991234567",
            "reservation_date": "2024-05-10",
            "reservation_time": "10",
        }
        response = self.client.post(self.booking, form_data)

        self.assertEqual(response.status_code, status.HTTP_302_FOUND)
        self.assertRedirects(response, "/")

        # Check if the booking was created
        self.assertEqual(Booking.objects.count(), 1)


class MenuViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.menu = reverse("restaurant:menu")
        cache.clear()

    @classmethod
    def setUpTestData(cls):
        cls.category1 = create_category()
        cls.category2 = create_category(title="Appetizers")
        for i in range(1, 11):
            create_menu(title=f"Soup {i}",
                        price=Decimal(str(i) + "0.99"),
                        category=cls.category1)

        for i in range(1, 4):
            create_menu(title=f"Appetizer {i}",
                        price=Decimal(str(i) + "0.99"),
                        category=cls.category2)

    def test_menu_view_pagination(self):
        response = self.client.get(self.menu)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTemplateUsed(response, "menu.html")
        self.assertIn("menu", response.context)
        self.assertIn("category", response.context)
        self.assertEqual(len(response.context["menu"]), 4)

    def test_menu_view_filtering(self):
        # Test that we get 3 appetizers using filtering
        response = self.client.get(
            self.menu + "?category=" + str(self.category2.id))
        self.assertEqual(len(response.context["menu"]), 3)


class MenuItemViewTest(TestCase):
    def setUp(self):
        self.client = Client()

    @classmethod
    def setUpTestData(cls):
        category = create_category()
        cls.menu_item = create_menu(category=category)

    def test_menu_item_view(self):
        response = self.client.get(reverse("restaurant:menu_item",
                                           args=[self.menu_item.pk]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTemplateUsed(response, "menu_item.html")
        self.assertEqual(response.context["menu_item"], self.menu_item)
