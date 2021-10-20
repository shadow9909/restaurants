from django.urls import path

from .views import addRestaurant, restaurant, restaurants, updateRestaurant


urlpatterns = [
    path('', restaurants, name="restaurants"),
    path('restaurant/<str:pk>/', restaurant, name="restaurant"),
    path('add-restaurant/', addRestaurant,name='add-restaurant'),
    path('update-restaurant/<str:pk>', updateRestaurant,name='update-restaurant')

]
