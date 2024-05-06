from django.urls import path

from .views import BookingViewSet, MenuItemsView, SingleMenuItemView

app_name = "api"


booking_list = BookingViewSet.as_view({
    "get": "list",
    "post": "create",
})

booking_detail = BookingViewSet.as_view({
    "get": "retrieve",
    "put": "update",
    "patch": "partial_update",
    "delete": "destroy",
})

menu_list = MenuItemsView.as_view()

menu_item_list = SingleMenuItemView.as_view()

urlpatterns = [
    path("bookings/", booking_list, name="booking_list"),
    path("bookings/<int:pk>/", booking_detail, name="booking_detail"),
    path("menu/", menu_list, name="menu_list"),
    path("menu-item/<int:pk>/", menu_item_list, name="menu_item_detail"),
]
