from rest_framework import serializers
from lunch_decider.models import Menu, Restaurant, Vote
from django.contrib.auth import get_user_model


class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = '__all__'
       

class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = '__all__'
 

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = '__all__'


class VoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vote
        fields = '__all__'


class VoteResultSerializer(serializers.Serializer):
    restaurant_name = serializers.CharField(source='menu__restaurant__name')
    vote_count = serializers.IntegerField(source='count')
    menu_items = serializers.CharField(source='menu__items')