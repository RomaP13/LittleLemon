from django.core.cache import cache
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateAPIView,
    DestroyAPIView,
)
from rest_framework.viewsets import ModelViewSet


from restaurant.models import Booking, Menu
from restaurant.serializers import BookingSerializer, MenuSerializer


class BookingViewSet(ModelViewSet):
    serializer_class = BookingSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["reservation_date"]

    def get_queryset(self):
        bookings = cache.get("bookings")

        if not bookings:
            print("hit the db: api/book")
            bookings = Booking.objects.all()
            cache.set("bookings", bookings)

        return bookings


class MenuItemsView(ListCreateAPIView):
    serializer_class = MenuSerializer

    def get_queryset(self):
        menu = cache.get("menu")

        if not menu:
            print("hit the db: api/menu")
            menu = Menu.objects.all()
            cache.set("menu", menu)

        return menu


class SingleMenuItemView(RetrieveUpdateAPIView, DestroyAPIView):
    serializer_class = MenuSerializer

    def get_object(self):
        menu_item_id = self.kwargs.get(self.pk_url_kwarg)
        menu_item = cache.get(f"menu_item_{menu_item_id}")

        if not menu_item:
            print("hit the db: api/menu-item")
            menu_item = super().get_object()
            cache.set(f"menu_item_{menu_item_id}", menu_item)

        return menu_item
