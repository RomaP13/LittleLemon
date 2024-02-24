from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

from . import views

urlpatterns = [
    path("items/", views.MenuItemsView.as_view(), name="items"),
    path("items/<int:pk>", views.SingleMenuItemView.as_view()),
    path("api-token-auth/", obtain_auth_token),
]
