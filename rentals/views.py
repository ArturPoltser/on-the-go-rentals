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


class CarListView(LoginRequiredMixin, generic.ListView):
    model = Car
    paginate_by = 5


class CarDetailView(LoginRequiredMixin, generic.DetailView):
    model = Car


class CarCreateView(LoginRequiredMixin, generic.CreateView):
    model = Car
    success_url = reverse_lazy("rentals:car-list")


class CarUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Car
    success_url = reverse_lazy("rentals:car-list")


class CarDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Car
    success_url = reverse_lazy("rentals:car-list")


class RenterListView(LoginRequiredMixin, generic.ListView):
    model = Renter
    paginate_by = 5


class RenterDetailView(LoginRequiredMixin, generic.DetailView):
    model = Renter
    queryset = Renter.objects.prefetch_related("cars__insurance")


class RenterCreateView(LoginRequiredMixin, generic.CreateView):
    model = Renter


class RenterDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Renter
    success_url = reverse_lazy("")
