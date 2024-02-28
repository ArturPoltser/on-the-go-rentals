from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from rentals.models import Renter, Car, Insurance


def index(request: HttpRequest) -> HttpResponse:
    num_renters = Renter.objects.count()
    num_cars = Car.objects.count()
    num_insurances = Insurance.objects.count()

    context = {
        "num_renters": num_renters,
        "num_cars": num_cars,
        "num_insurances": num_insurances,
    }

    return render(request, "rentals/index.html", context=context)


class InsuranceListView(LoginRequiredMixin, generic.ListView):
    model = Insurance
    context_object_name = "manufacturer_list"
    template_name = "rentals/insurance_list.html"
    paginate_by = 5


class InsuranceCreateView(LoginRequiredMixin, generic.CreateView):
    model = Insurance
    fields = "__all__"
    success_url = reverse_lazy("rentals:insurances-list")


class InsuranceUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Insurance
    fields = "__all__"
    success_url = reverse_lazy("rentals:insurances-list")


class InsuranceDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Insurance
    success_url = reverse_lazy("rentals:insurances-list")
