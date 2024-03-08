from django.views.generic import DetailView
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView

from django_filters.views import FilterView

from .filters import MenuFilter
from .forms import BookingForm
from .models import Menu, Category


class HomeView(TemplateView):
    template_name = "index.html"


class AboutView(TemplateView):
    template_name = "about.html"


class MenuView(FilterView):
    template_name = "menu.html"
    context_object_name = "menu"
    model = Menu
    filterset_class = MenuFilter

    def get_queryset(self):
        return Menu.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["category"] = Category.objects.all()

        return context


class MenuItemView(DetailView):
    template_name = "menu_item.html"
    context_object_name = "menu_item"
    model = Menu
    pk_url_kwarg = "pk"


class BookingView(CreateView):
    template_name = "booking.html"
    form_class = BookingForm

    def post(self, request, *args, **kwargs):
        return super(BookingView, self).post(request, *args, **kwargs)

    def form_valid(self, form):
        form.save()
        return super(BookingView, self).form_valid(form)

    def get_success_url(self):
        return "/"
