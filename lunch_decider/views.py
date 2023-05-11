from rest_framework import generics, status
from rest_framework.response import Response
from .models import Restaurant, Menu, Vote
from .serializers import RestaurantSerializer, MenuSerializer, EmployeeSerializer, VoteSerializer
from datetime import date
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import get_user_model


class EmployeeCreateView(generics.CreateAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = EmployeeSerializer


class RestaurantCreateView(generics.CreateAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer


class MenuCreateView(generics.CreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer


class VoteCreateView(generics.CreateAPIView):
    queryset = Vote.objects.all()
    serializer_class = VoteSerializer


class CurrentDayMenuView(generics.RetrieveAPIView):
    serializer_class = MenuSerializer

    def get_object(self):
        current_date = date.today()
        return Menu.objects.filter(date=current_date).first()
 

