from django.urls import path
from . import views
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    path('token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('employees/create/', views.EmployeeCreateView.as_view(), name='create-employee'),
    path('restaurants/create/', views.RestaurantCreateView.as_view(), name='create-restaurant'),
    path('menus/create/', views.MenuCreateView.as_view(), name='create-menu'),
    path('menus/current/', views.CurrentDayMenuView.as_view(), name='current-day-menu'),
    path('votes/create/', views.VoteCreateView.as_view(), name='create-vote'),
    path('votes/results/', views.VoteResultsView.as_view(), name='vote-results'),
]