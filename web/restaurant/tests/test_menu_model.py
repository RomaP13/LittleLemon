from decimal import Decimal

from django.core.exceptions import ValidationError
from django.test import TestCase
from restaurant.utils import create_category, create_menu


class MenuTest(TestCase):

    def setUp(self):
        self.category = create_category()
        self.menu = create_menu(category=self.category)

    def test_menu_creation(self):
        """Test a valid menu object"""
        self.assertEqual(self.menu.title, "Pozole")
        self.assertEqual(self.menu.price, Decimal("10.99"))
        self.assertEqual(self.menu.category.title, "Soups")

    def test_menu_foreign_key_relationship(self):
        """Test the foreign key relationship between Menu and Category"""
        self.assertEqual(self.menu.category, self.category)

    def test_invalid_title(self):
        """Test the menu with blank title"""
        with self.assertRaises(ValidationError):
            create_menu(title="", category=self.category)

    def test_invalid_price(self):
        """Test the menu with blank price"""
        with self.assertRaises(ValidationError):
            create_menu(price="", category=self.category)

    def test_price_below_min(self):
        """Test the price below min limit"""
        with self.assertRaises(ValidationError):
            create_menu(price="0", category=self.category)

    def test_price_above_max(self):
        """Test the price above max limit"""
        with self.assertRaises(ValidationError):
            create_menu(price="9999", category=self.category)

    def test_invalid_category(self):
        """Test the menu with blank category"""
        with self.assertRaises(ValidationError):
            create_menu(category=None)
