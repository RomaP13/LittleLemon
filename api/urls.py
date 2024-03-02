from django.urls import path

from .views import BookingViewSet

app_name = "api"

bookings_list = BookingViewSet.as_view({
    "get": "list",
    "post": "create",
})

urlpatterns = [
    path("bookings/", bookings_list, name="bookings")
]
