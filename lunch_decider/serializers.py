from rest_framework import serializers
from lunch_decider.models import Menu, Restaurant, Employee, Vote


class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
       

class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
 

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee


class VoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vote
    