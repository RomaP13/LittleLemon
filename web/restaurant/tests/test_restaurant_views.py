from django.test import Client, TestCase
from django.urls import reverse
from rest_framework import status

from restaurant.forms import BookingForm
from restaurant.models import Booking


class HomeAboutViewTest(TestCase):
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
        self.assertEqual(response.status_code, 200)
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
