from django.core.cache import cache
from django.core.exceptions import ValidationError
from restaurant.models import Booking, Category, Menu

MENU_CACHE_KEY = "menu"


def cache_menu():
    menu = Menu.objects.all().order_by("id").select_related("category").values(
        "id",
        "title",
        "price",
        "category__title",
    )
    cache.set(MENU_CACHE_KEY, list(menu))


def get_cached_menu():
    return cache.get(MENU_CACHE_KEY)


def create_booking(**kwargs):
    defaults = {
        "first_name": "John",
        "last_name": "Doe",
        "email": "john.doe@example.com",
        "phone_number": "+380991234567",
        "reservation_date": "2024-05-10",
        "reservation_time": "10",
    }

    defaults.update(kwargs)

    return Booking(**defaults)


def create_category(**kwargs):
    defaults = {
        "title": "Soups",
    }
    defaults.update(kwargs)
    category = Category(**defaults)
    category.save()
    return category


def create_menu(**kwargs):
    defaults = {
        "title": "Pozole",
        "price": "10.99",
        "category": None,
    }

    defaults.update(kwargs)
    menu = Menu(**defaults)
    try:
        menu.full_clean()  # Validate the model instance
        menu.save()  # Save only if validation passes
    except ValidationError as e:
        # Handle the ValidationError if needed
        raise e
    return menu
