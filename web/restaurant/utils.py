from django.core.cache import cache

from restaurant.models import Menu

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
