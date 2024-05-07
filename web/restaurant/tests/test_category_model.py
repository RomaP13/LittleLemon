from django.core.exceptions import ValidationError
from django.test import TestCase
from restaurant.utils import create_category


class CategoryModelTest(TestCase):

    def test_category_creation(self):
        """Test a valid category object"""
        category = create_category()
        self.assertEqual(category.title, "Soups")

    def test_invalid_title(self):
        """Test the menu with blank title"""
        with self.assertRaises(ValidationError):
            create_category(title="")
