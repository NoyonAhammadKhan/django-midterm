from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Brand(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return f"{self.name}"


class Car(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(
        upload_to='car_app/media/uploads/', blank=True, null=True)
    description = models.TextField()
    quantity = models.IntegerField()
    price = models.FloatField()
    owner = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='added_cars')
    brand_name = models.ForeignKey(
        Brand, on_delete=models.CASCADE, related_name='cars')

    def __str__(self):
        return f"{self.name}"


class Comment(models.Model):
    name = models.CharField(max_length=50)
    comment = models.TextField()
    car = models.ForeignKey(
        Car, on_delete=models.CASCADE, related_name='comments')

    def __str__(self) -> str:
        return f"{self.car} comments"


class Order(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="orders")
    car = models.ForeignKey(Car, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user}'s order"
