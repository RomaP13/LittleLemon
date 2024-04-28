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
        self.assertEqual(self.menu.price, "10.99")
        self.assertEqual(self.menu.category.title, "Soups")

    # Test the foreign key relationship between Menu and Category
    def test_menu_foreign_key_relationship(self):
        self.assertEqual(self.menu.category, self.category)

    # Test the menu with blank title
    def test_invalid_title(self):
        menu_invalid_title = create_menu(title="", category=self.category)
        self.assertRaises(ValidationError, menu_invalid_title.full_clean)

    # Test the menu with blank price
    def test_invalid_price(self):
        menu_invalid_price = create_menu(price="", category=self.category)
        self.assertRaises(ValidationError, menu_invalid_price.full_clean)

    # Test the price below min limit
    def test_price_below_min(self):
        menu_invalid_price = create_menu(price="0", category=self.category)
        self.assertRaises(ValidationError, menu_invalid_price.full_clean)

    # Test the price above max limit
    def test_price_above_max(self):
        menu_invalid_price = create_menu(price="9999", category=self.category)
        self.assertRaises(ValidationError, menu_invalid_price.full_clean)

    # Test the menu with blank category
    def test_invalid_category(self):
        category = create_category(title="")
        menu_invalid_category = create_menu(category=category)
        self.assertRaises(ValidationError, menu_invalid_category.full_clean)
