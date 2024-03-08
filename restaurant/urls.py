from django.urls import path

from . import views

urlpatterns = [
    path("", views.HomeView.as_view(), name="home"),
    path("about/", views.AboutView.as_view(), name="about"),
    path("menu/", views.MenuView.as_view(), name="menu"),
    path('menu_item/<int:pk>/', views.MenuItemView.as_view(), name="menu_item"),
    path("booking/", views.BookingView.as_view(), name="booking")
]
