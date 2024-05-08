import random
from decimal import Decimal

from django.test import TestCase
from restaurant.utils import (cache_menu, create_category, create_menu,
                              get_cached_menu)


class TestCacheSystem(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.category_1 = create_category(title="Main")
        cls.category_2 = create_category(title="Breakfasts")
        categories = [cls.category_1, cls.category_2]
        cls.menu = []
        fixed_price = Decimal("0.99")

        for i in range(1, 999):
            menu_item = create_menu(
                title=f"number {i}",
                price=Decimal(i + fixed_price),
                category=random.choice(categories)
            )
            cls.menu.append(menu_item)

    def test_cached_menu(self):
        initial_menu_ids = [m.id for m in self.menu]

        cache_menu()
        cached_menu = get_cached_menu()
        cached_menu_ids = [m["id"] for m in cached_menu]

        self.assertListEqual(initial_menu_ids, cached_menu_ids)
