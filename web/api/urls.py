from django.urls import path

from .views import BookingViewSet, MenuItemsView, SingleMenuItemView

app_name = "api"

bookings_list = BookingViewSet.as_view({
    "get": "list",
    "post": "create",
})

menu_list = MenuItemsView.as_view()

menu_item_list = SingleMenuItemView.as_view()

urlpatterns = [
    path("bookings/", bookings_list, name="booking_list"),
    path("menu/", menu_list, name="menu_list"),
    path("menu-item/<int:pk>/", menu_item_list, name="menu_item_detail"),
]
