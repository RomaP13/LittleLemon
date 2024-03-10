from django_filters import FilterSet

from .models import Menu


class MenuFilter(FilterSet):
    class Meta:
        model = Menu
        fields = ["category"]
