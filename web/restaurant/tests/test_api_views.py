from django.urls import reverse
from rest_framework.test import APIClient, APITestCase
from rest_framework import status

from restaurant.models import Booking, Category, Menu


class BookingAPIViewTest(APITestCase):
    fixtures = ["bookings.json"]

    def setUp(self):
        self.client = APIClient()
        self.booking = Booking.objects.first()
        self.booking_list = reverse("api:booking_list")
        self.booking_detail = reverse("api:booking_detail",
                                      kwargs={"pk": self.booking.pk})
        self.data = {
            "first_name": "Jane",
            "last_name": "Doe",
            "email": "jane.doe@example.com",
            "phone_number": "+380991234567",
            "reservation_date": "2024-06-11",
            "reservation_time": "12",
        }

    def test_get_bookings(self):
        response = self.client.get(self.booking_list)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Booking.objects.count(), 10)

    def test_create_booking(self):
        response = self.client.post(self.booking_list, self.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Booking.objects.count(), 11)

    def test_retrieve_booking(self):
        response = self.client.get(self.booking_detail)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["first_name"], self.booking.first_name)

    def test_update_booking(self):
        response = self.client.put(self.booking_detail, self.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["first_name"], "Jane")

    def test_partial_update_booking(self):
        data = {
            "first_name": "Joe",
            "email": "joe.doe@example.com",
        }
        response = self.client.patch(self.booking_detail, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["first_name"], "Joe")
        self.assertEqual(response.data["email"], "joe.doe@example.com")

    def test_delete_booking(self):
        response = self.client.delete(self.booking_detail)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Booking.objects.count(), 9)


class MenuItemsAPIViewTest(APITestCase):
    fixtures = ["categories.json", "menu_items.json"]

    def setUp(self):
        self.client = APIClient()
        self.menu_list = reverse("api:menu_list")

    def test_get_menu_items(self):
        response = self.client.get(self.menu_list)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Menu.objects.count(), 14)

    def test_create_menu_item(self):
        data = {
            "title": "Pozole",
            "price": "10.99",
            "category": Category.objects.first().pk,
        }
        response = self.client.post(self.menu_list, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Menu.objects.count(), 15)


class SingleMenuItemAPIViewTest(APITestCase):
    fixtures = ["categories.json", "menu_items.json"]

    def setUp(self):
        self.client = APIClient()
        self.menu = Menu.objects.first()
        self.menu_item_detail = reverse("api:menu_item_detail",
                                        kwargs={"pk": self.menu.pk})

    def test_retrieve_menu_item(self):
        response = self.client.get(self.menu_item_detail)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], self.menu.title)

    def test_update_menu_item(self):
        data = {
            "title": "Miso",
            "price": "22.99",
            "category": Category.objects.first().pk,
        }
        response = self.client.put(self.menu_item_detail, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], "Miso")

    def test_partial_update_menu_item(self):
        data = {
            "price": "15.50",
        }
        response = self.client.patch(self.menu_item_detail, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["price"], "15.50")

    def test_delete_menu_item(self):
        response = self.client.delete(self.menu_item_detail)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Menu.objects.count(), 13)
