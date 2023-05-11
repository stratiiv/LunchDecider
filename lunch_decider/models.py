from django.db import models
from django.contrib.auth import get_user_model

class Restaurant(models.Model):
    """
    Model representing a restaurant.

    Attributes:
        name (str): The name of the restaurant.
        address (str): The address of the restaurant.
        contact (str): The contact information of the restaurant.
    """

    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    contact = models.CharField(max_length=100)

    def __str__(self):
        """
        Return a string representation of the restaurant.

        Returns:
            str: The name of the restaurant.
        """

        return self.name 


class Menu(models.Model):
    """
    Model representing a menu for a restaurant.

    Attributes:
        restaurant (Restaurant): The restaurant associated with the menu.
        date (date): The date of the menu.
        items (str): The items included in the menu.
    """

    restaurant = models.OneToOneField(Restaurant, on_delete=models.CASCADE)
    date = models.DateField()
    items = models.TextField()

    def __str__(self):
        """
        Return a string representation of the menu.

        Returns:
            str: The menu items and the associated restaurant name.
        """

        return f"{self.items} in {self.restaurant.name} restaurant"


class Vote(models.Model):
    """
    Model representing a vote for a menu by an employee.

    Attributes:
        menu (Menu): The menu for which the vote is cast.
        employee (User): The employee who cast the vote.
        created_at (date): The date and time when the vote was created.
    """

    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    employee = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    created_at = models.DateField(auto_now_add=True)

    # add unique constraint so single employee can't vote twice
    class Meta:
        unique_together = ['menu', 'employee']

    def __str__(self):
        """
        Return a string representation of the vote.

        Returns:
            str: The string representation of the associated menu.
        """

        return str(self.menu)
