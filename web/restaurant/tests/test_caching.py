import random
from django.test import TestCase

from restaurant.models import Category, Menu
from restaurant.utils import cache_menu, get_cached_menu


class TestCacheSystem(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.category_1 = Category.objects.create(title="Main")
        cls.category_2 = Category.objects.create(title="Breakfasts")
        categories = [cls.category_1, cls.category_2]
        cls.menu = []

        for i in range(1, 10000):
            menu_item = Menu.objects.create(
                title=f"number {i}",
                price=i / 2,
                category=random.choice(categories)
            )
            cls.menu.append(menu_item)

    def test_cached_menu(self):
        initial_menu_ids = [m.id for m in self.menu]

        cache_menu()
        cached_menu = get_cached_menu()
        cached_menu_ids = [m["id"] for m in cached_menu]

        self.assertListEqual(initial_menu_ids, cached_menu_ids)
