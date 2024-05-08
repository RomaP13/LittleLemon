from django.core.cache import cache
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.views.generic import DetailView
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView
from django_filters.views import FilterView

from .filters import MenuFilter
from .forms import BookingForm
from .models import Category, Menu


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
        menu_ids = cache.get("menu_ids")

        if not menu_ids:
            menu = Menu.objects.select_related("category").all().order_by("id")
            menu_ids = list(menu.values_list("id", flat=True))
            cache.set("menu_ids", menu_ids)

        return Menu.objects.filter(id__in=menu_ids).order_by("id")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category = cache.get("category")

        if not category:
            category = Category.objects.all()
            cache.set("category", category)

        context["category"] = category
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

    def get_object(self):
        menu_item_id = self.kwargs.get(self.pk_url_kwarg)
        menu_item = cache.get(f"menu_item_{menu_item_id}")

        if not menu_item:
            menu_item = super().get_object()
            cache.set(f"menu_item_{menu_item_id}", menu_item)

        return menu_item


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
