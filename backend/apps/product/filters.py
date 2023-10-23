import django_filters
from .models import Car
from django import forms


class CarFilter(django_filters.FilterSet):
    transmission = django_filters.ModelChoiceFilter(
        field_name="transmission",
        queryset=Car.objects.all(),
        widget=forms.Select()
    )

    class Meta:
        model = Car
        fields = {
            'transmission': ['exact'],
            'name': ['icontains'],
            'price': ['exact', 'gte'],
            'mileage': ['exact', 'gte']
        }
