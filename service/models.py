from django.db import models
from django.db.models import Avg
from account.models import Profile

class Taxi(models.Model):
    name = models.CharField(max_length=20)
    price = models.IntegerField()
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Order(models.Model):
    taxi = models.ForeignKey(Taxi, on_delete=models.CASCADE)
    address = models.CharField(max_length=50)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)

    def __str__(self):
        return f'Order {self.profile} - {self.address}'

class StatusType(models.Model):
    raiting = models.IntegerField()

    def __str__(self):
        return {self.raiting}

class StatusDriver(models.Model):
    point = models.CharField(max_length=50)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)

    def __str__(self):
        return self.point






