from django.db import models
from django.contrib.auth import get_user_model


class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    contact = models.CharField(max_length=100)

    def __str__(self):
        return self.name 


class Menu(models.Model):
    restaurant = models.OneToOneField(Restaurant, on_delete=models.CASCADE)
    date = models.DateField()
    items = models.TextField()

    def __str__(self):
        return f"Menu for {self.restaurant.name} on {self.date}"


class Vote(models.Model):
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    employee = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.menu