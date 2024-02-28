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
