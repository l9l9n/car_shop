from django.db import models
from PIL import Image
from .choice_data import TRANSMISSOINS_CHOICE, ENGINE_CHOICE, SIDE_CHOICE, CONDITION_CHOICE


class Car(models.Model):
    name = models.CharField("Название машины", max_length=90)
    age = models.DateTimeField("Год выпуска")
    # photo = models.ImageField('Фото машины', upload_to="media/")
    color = models.CharField("Цвет машины", max_length=90)
    transmission = models.CharField("Коробка передач", choices=TRANSMISSOINS_CHOICE, default='Автомат', max_length=90)
    price = models.DecimalField("Цена", max_digits=9, decimal_places=2)
    engin = models.CharField("Тип давигателя", choices=ENGINE_CHOICE, default='Бензин', max_length=90)
    volume = models.DecimalField('Объем двигателя', max_digits=9, decimal_places=2)
    vile_side = models.CharField('Расположение руля', choices=SIDE_CHOICE, default='Левая', max_length=90)
    mileage = models.DecimalField("Пробег", max_digits=9, decimal_places=2)
    condition = models.CharField('Состояние', choices=CONDITION_CHOICE, default='Новое', max_length=90)

    class Meta:
        verbose_name = 'Машине'
        verbose_name_plural = 'Машины'

    def __str__(self):
        return self.name


class CarImage(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='photos')
    photo = models.ImageField(upload_to='media/')

    def save(self, *args, **kwargs):
        super(CarImage, self).save(*args, **kwargs)
        img = Image.open(self.photo.path)
        if img.height > 1125 or img.width > 1125:
            img.thumbnail((1125, 1125))
        img.save(self.photo.path, quality=70, optimize=True)

    class Meta:
        verbose_name = 'Фото машины'
        verbose_name_plural = 'Фото машин'
