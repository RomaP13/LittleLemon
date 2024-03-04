from django.urls import path

from . import views

urlpatterns = [
    path("", views.HomeView.as_view(), name="home"),
    path("about/", views.AboutView.as_view(), name="about"),
    path("menu/", views.menu, name="menu"),
    path("booking/", views.BookingView.as_view(), name="booking")
]
