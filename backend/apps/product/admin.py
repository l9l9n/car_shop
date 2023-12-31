from django.contrib import admin
from .models import Car, CarImage


@admin.register(CarImage)
class PhotoAdmin(admin.ModelAdmin):
    list_display = [
        'car',
        'photo',
    ]


@admin.register(Car)
class UserAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'name',
        'age',
        # 'photo',
        'color',
        'price',
        'transmission',
        'engin',
        'volume',
        'vile_side',
        'mileage',
        'condition'
    ]
