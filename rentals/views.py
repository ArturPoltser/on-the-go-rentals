from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

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
