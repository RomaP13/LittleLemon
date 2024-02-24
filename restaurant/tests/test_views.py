from django.test import TestCase
from django.urls import reverse
from rest_framework import status

from restaurant.models import Menu


class MenuViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        number_of_food = 5
        for food_num in range(1, number_of_food + 1):
            Menu.objects.create(
                title="Food %s" % food_num, price=food_num * 10, inventory=food_num * 2
            )

    def test_getall(self):
        response = self.client.get(reverse("items"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        menus = Menu.objects.all().order_by("id")
        expected_data = [
            {"title": menu.title, "price": str(menu.price), "inventory": menu.inventory}
            for menu in menus
        ]
        actual_data = [
            {"title": item['title'], "price": item['price'], "inventory": item['inventory']}
            for item in response.data
        ]
        self.assertEqual(actual_data, expected_data)
