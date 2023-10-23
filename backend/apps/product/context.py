from random import random

from .models import Car


def get_cars(request):
    car = sorted(Car.objects.all().order_by("name"), key=lambda x: random())
    return {"car_index": car[:3]}
