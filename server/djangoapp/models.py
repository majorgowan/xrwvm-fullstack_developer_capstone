# Uncomment the following imports before adding the Model code
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.

# <HINT> Create a Car Make model `class CarMake(models.Model)`:
# - Name
# - Description
# - Any other fields you would like to include in car make model
# - __str__ method to print a car make object
class CarMake(models.Model):
    name = models.CharField(max_length=32)
    description = models.CharField(max_length=128)

    def __str__(self):
        return f"{self.name} ({self.description})"


# <HINT> Create a Car Model model `class CarModel(models.Model):`:
# - Many-To-One relationship to Car Make model (One Car Make has many
# Car Models, using ForeignKey field)
# - Name
# - Type (CharField with a choices argument to provide limited choices
# such as Sedan, SUV, WAGON, etc.)
# - Year (IntegerField) with min value 2015 and max value 2023
# - Any other fields you would like to include in car model
# - __str__ method to print a car make object
MODEL_TYPES = [
    ("SEDAN", "Sedan"),
    ("COUPE", "Coupe"),
    ("SUV", "SUV"),
    ("STATION_WAGON", "Station Wagon"),
    ("EV", "EV")
]


class CarModel(models.Model):
    name = models.CharField(max_length=32)
    model_type = models.CharField(max_length=24, choices=MODEL_TYPES,
                                  default="SEDAN")
    year = models.IntegerField(validators=[MinValueValidator(2015),
                                           MaxValueValidator(2023)])
    # Many-to-One relationship
    car_make = models.ForeignKey(CarMake, on_delete=models.CASCADE)

    def __str__(self):
        return (f"{self.car_make.name} {self.name}"
                + f" ({self.model_type}, {self.year})")
