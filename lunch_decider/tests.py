import pytest
from rest_framework.test import APIClient
from django.urls import reverse
from django.contrib.auth import get_user_model
from .models import Restaurant, Menu, Vote
from .serializers import RestaurantSerializer, MenuSerializer, VoteSerializer


@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture
def create_user():
    def _create_user(username, password):
        User = get_user_model()
        return User.objects.create_user(username=username, password=password)

    return _create_user


@pytest.mark.django_db
def test_create_restaurant(api_client):
    url = reverse('create-restaurant')
    data = {
        'name': 'Restaurant 1',
        'address': 'Address 1',
        'contact': 'Contact 1',
    }
    response = api_client.post(url, data, format='json')
    assert response.status_code == 201
    assert Restaurant.objects.count() == 1
    assert Restaurant.objects.first().name == 'Restaurant 1'


@pytest.mark.django_db
def test_create_menu(api_client, create_user):
    user = create_user('testuser', 'testpassword')
    api_client.force_authenticate(user=user)

    restaurant = Restaurant.objects.create(name='Restaurant 1', address='Address 1', contact='Contact 1')
    url = reverse('create-menu')
    data = {
        'restaurant': restaurant.id,
        'date': '2023-05-11',
        'items': 'Item 1, Item 2, Item 3',
    }
    response = api_client.post(url, data, format='json')
    assert response.status_code == 201
    assert Menu.objects.count() == 1
    assert Menu.objects.first().restaurant == restaurant


# Add more tests for other API views, serializers, etc.

