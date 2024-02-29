from django.conf import settings
from django.core.validators import (
    RegexValidator,
    MinValueValidator,
    MaxValueValidator,
)
from django.db import models
from django.contrib.auth.models import AbstractUser


class Insurance(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True, null=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class Renter(AbstractUser):
    max_daily_budget = models.IntegerField(
        validators=[
            MinValueValidator(
                limit_value=100,
                message="We don't have such car for this budget. Sorry."
            )
        ]
    )
    rental_time = models.IntegerField(
        validators=[
            MinValueValidator(
                limit_value=0,
                message="Rental time should be a non-negative integer."
            ),
            MaxValueValidator(
                limit_value=31,
                message="Rental time should not exceed 31 days."
            )
        ]
    )
    driver_license = models.CharField(
        max_length=255,
        unique=True,
        validators=[
            RegexValidator(
                regex=r"^[A-Z]{2}\d{5}$",
                message="Driver license should consist only of 7 characters: "
                        "first 2 characters are uppercase letters and "
                        "last 5 characters are digits"
            )
        ]
    )

    def __str__(self):
        return f"{self.username} ({self.first_name} {self.last_name})"


class Car(models.Model):
    model = models.CharField(max_length=255)
    year = models.IntegerField(
        validators=[
            MinValueValidator(
                limit_value=2005,
                message="Year should be from 2005 onwards."
            ),
            MaxValueValidator(
                limit_value=2023,
                message="Year should not exceed 2023."
            )
        ]
    )
    horsepower = models.IntegerField(
        validators=[
            MinValueValidator(
                limit_value=100,
                message="We can't rent car with less than 100 horsepowers."
            ),
            MaxValueValidator(
                limit_value=800,
                message="We can't rent car with more than 800 horsepowers."
            )
        ]
    )
    fuel_consumption = models.DecimalField(max_digits=2, decimal_places=1)
    daily_cost = models.IntegerField(
        validators=[
            MinValueValidator(
                limit_value=100,
                message="We can't rent car with daily price less than 100$."
            ),
            MaxValueValidator(
                limit_value=2000,
                message="We can't rent car with daily price more than 2000$."
            )
        ]
    )
    insurance = models.ForeignKey(Insurance, on_delete=models.CASCADE)
    available_to_rent = models.BooleanField(default=True)
    renter = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    renters_history = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="cars")

    def __str__(self):
        return self.model
