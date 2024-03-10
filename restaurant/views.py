from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
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
    paginate_by = 4

    def get_queryset(self):
        # Add ordering to avoid UnorderedObjectListWarning
        return Menu.objects.all().order_by("id")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["category"] = Category.objects.all()
        page = self.request.GET.get("page", 1)
        paginator = Paginator(self.object_list, self.paginate_by)

        try:
            menu = paginator.page(page)
        except PageNotAnInteger:
            menu = paginator.page(1)
        except EmptyPage:
            menu = paginator.page(paginator.num_pages)

        context["menu"] = menu

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
