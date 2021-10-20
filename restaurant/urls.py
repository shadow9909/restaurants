from django.urls import path

from .views import restaurant, restaurants


urlpatterns = [
    path('', restaurants, name="restaurants"),
    path('restaurant/<str:pk>/', restaurant, name="restaurant"),
]
