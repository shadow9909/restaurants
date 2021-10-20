from django.shortcuts import render

# Create your views here.
def restaurants(request):
    return render(request, 'restaurant/restaurants.html')

def restaurant(request, pk):
    return render(request, 'restaurant/single-restaurant.html')

