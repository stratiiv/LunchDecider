from datetime import date
from rest_framework import generics, status
from rest_framework.response import Response
from .models import Restaurant, Menu, Vote
from .serializers import RestaurantSerializer, MenuSerializer, EmployeeSerializer, VoteSerializer, VoteResultSerializer
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import get_user_model
from django.db import models
from rest_framework.views import APIView
from .services import get_current_day_vote_results


class EmployeeCreateView(generics.CreateAPIView):
    """
    API view for creating an employee.

    Endpoint: /api/employees/create/
    Method: POST
    """

    queryset = get_user_model().objects.all()
    serializer_class = EmployeeSerializer


class RestaurantCreateView(generics.CreateAPIView):
    """
    API view for creating a restaurant.

    Endpoint: /api/restaurants/create/
    Method: POST
    """

    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer


class MenuCreateView(generics.CreateAPIView):
    """
    API view for creating a menu.

    Endpoint: /api/menus/create/
    Method: POST
    """

    queryset = Menu.objects.all()
    serializer_class = MenuSerializer


class VoteCreateView(generics.CreateAPIView):
    """
    API view for creating a vote.

    Endpoint: /api/votes/create/
    Method: POST
    """

    queryset = Vote.objects.all()
    serializer_class = VoteSerializer


class CurrentDayMenuView(generics.RetrieveAPIView):
    """
    API view for retrieving the menu for the current day.

    Endpoint: /api/menus/current-day/
    Method: GET
    """

    serializer_class = MenuSerializer

    def get_object(self):
        """
        Get the menu object for the current day.

        Returns:
            Menu: The menu object for the current day.
        """

        return Menu.objects.filter(date=date.today()).first()


class VoteResultsView(APIView):
    """
    API view for retrieving the vote results for the current day.

    Endpoint: /api/votes/results/
    Method: GET
    """

    def get(self, request):
        """
        Get the vote results for the current day.

        Returns:
            Response: The serialized vote results data.
        """

        votes = get_current_day_vote_results()
        serializer = VoteResultSerializer(votes, many=True)
        return Response(serializer.data)
