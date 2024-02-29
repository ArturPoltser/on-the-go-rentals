from django.urls import path

from rentals.views import (
    index,
    InsuranceListView,
    InsuranceCreateView,
    InsuranceUpdateView,
    InsuranceDeleteView,
    CarListView,
    CarDetailView,
    CarCreateView,
    CarUpdateView,
    CarDeleteView,
    RenterListView,
    RenterDetailView,
    RenterCreateView,
    RenterDeleteView,
)


urlpatterns = [
    path("", index, name="index"),
    path(
        "insurances/",
        InsuranceListView.as_view(),
        name="insurances-list",
    ),
    path(
        "insurances/create/",
        InsuranceCreateView.as_view(),
        name="insurance-create",
    ),
    path(
        "insurances/<int:pk>/update/",
        InsuranceUpdateView.as_view(),
        name="insurance-update",
    ),
    path(
        "insurances/<int:pk>/delete/",
        InsuranceDeleteView.as_view(),
        name="insurance-delete",
    ),
    path("cars/", CarListView.as_view(), name="car-list"),
    path("cars/<int:pk>/", CarDetailView.as_view(), name="car-detail"),
    path("cars/create/", CarCreateView.as_view(), name="car-create"),
    path("cars/<int:pk>/update/", CarUpdateView.as_view(), name="car-update"),
    path("cars/<int:pk>/delete/", CarDeleteView.as_view(), name="car-delete"),
    path("renters/", RenterListView.as_view(), name="renter-list"),
    path(
        "renters/<int:pk>/", RenterDetailView.as_view(), name="renter-detail"
    ),
    path("renters/", RenterListView.as_view(), name="renter-list"),
    path(
        "renters/<int:pk>/", RenterDetailView.as_view(), name="renter-detail"
    ),
    path("renters/create/", RenterCreateView.as_view(), name="renter-create"),
    path(
        "renters/<int:pk>/delete/",
        RenterDeleteView.as_view(),
        name="renter-delete",
    ),
]

app_name = "rentals"
