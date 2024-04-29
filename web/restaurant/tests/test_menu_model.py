from decimal import Decimal

from django.core.exceptions import ValidationError
from django.test import TestCase
from restaurant.utils import create_category, create_menu


class MenuTest(TestCase):

    def setUp(self):
        self.category = create_category()
        self.menu = create_menu(category=self.category)

    # Test a valid menu object
    def test_menu_creation(self):
        self.assertEqual(self.menu.title, "Pozole")
        self.assertEqual(self.menu.price, Decimal("10.99"))
        self.assertEqual(self.menu.category.title, "Soups")

    # Test the foreign key relationship between Menu and Category
    def test_menu_foreign_key_relationship(self):
        self.assertEqual(self.menu.category, self.category)

    # Test the menu with blank title
    def test_invalid_title(self):
        with self.assertRaises(ValidationError):
            create_menu(title="", category=self.category)

    # Test the menu with blank price
    def test_invalid_price(self):
        with self.assertRaises(ValidationError):
            create_menu(price="", category=self.category)

    # Test the price below min limit
    def test_price_below_min(self):
        with self.assertRaises(ValidationError):
            create_menu(price="0", category=self.category)

    # Test the price above max limit
    def test_price_above_max(self):
        with self.assertRaises(ValidationError):
            create_menu(price="9999", category=self.category)

    # Test the menu with blank category
    def test_invalid_category(self):
        with self.assertRaises(ValidationError):
            create_menu(category=None)
