from rest_framework import generics
from .models import Restaurant, Menu, Employee, Vote
from .serializers import RestaurantSerializer, MenuSerializer, EmployeeSerializer, VoteSerializer
from datetime import date


class EmployeeCreateView(generics.CreateAPIView):
    queryset = Employee.objects.all()
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
 
