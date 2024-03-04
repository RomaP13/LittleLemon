from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView
from .forms import BookingForm


class HomeView(TemplateView):
    template_name = "index.html"


class AboutView(TemplateView):
    template_name = "about.html"


def menu(request):
    context = {}
    return render(request, "menu.html", context)


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
