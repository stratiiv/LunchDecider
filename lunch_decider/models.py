from django.db import models
from django.contrib.auth.models import User


class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    department = models.CharField(max_length=100)
    position = models.CharField(max_length=100)

    def __str__(self):
        return self.user.username


class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    contact = models.CharField(max_length=100)

    def __str__(self):
        return self.name 


class Menu(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    date = models.DateField()
    items = models.TextField()

    def __str__(self):
        return str(self.date)


class Vote(models.Model):
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    employee = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.menu