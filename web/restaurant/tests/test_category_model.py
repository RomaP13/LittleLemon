from django.core.exceptions import ValidationError
from django.test import TestCase
from restaurant.utils import create_category


class CategoryModelTest(TestCase):

    # Test a valid category object
    def test_category_creation(self):
        category = create_category()
        self.assertEqual(category.title, "Soups")

    # Test the menu with blank title
    def test_invalid_title(self):
        with self.assertRaises(ValidationError):
            create_category(title="")
