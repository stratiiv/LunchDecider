from django.urls import path
from . import views

urlpatterns = [
    path('employees/create/', views.EmployeeCreateView.as_view(), name='create-employee'),
    path('restaurants/create/', views.RestaurantCreateView.as_view(), name='create-restaurant'),
    path('menus/create/', views.MenuCreateView.as_view(), name='create-menu'),
    path('votes/create/', views.VoteCreateView.as_view(), name='create-vote'),
    path('menus/current/', views.CurrentDayMenuView.as_view(), name='current-day-menu'),
]