from django.shortcuts import redirect, render
from .models import Restaurant
from .forms import RestaurantForm
# Create your views here.
def restaurants(request):
    restaurants = Restaurant.objects.all()
    context = {'restaurants': restaurants}
    return render(request, 'restaurant/restaurants.html', context)

def restaurant(request, pk):
    restaurant = Restaurant.objects.get(id=pk)
    context = {'restaurant': restaurant}
    return render(request, 'restaurant/single-restaurant.html', context)

def addRestaurant(request):
    form = RestaurantForm()
    context = {'form': form}
    if(request.method == "POST"):
        form = RestaurantForm(request.POST)
        if(form.is_valid):
            form.save()
            return redirect('restaurants')
    return render(request, 'restaurant/add-restaurant.html', context)

def updateRestaurant(request, pk):
    restaurant = Restaurant.objects.get(id=pk)
    form = RestaurantForm(instance=restaurant)
    context = {'form': form}
    if(request.method =='POST'):
        form = RestaurantForm(request.POST, instance=restaurant)
        if(form.is_valid):
            form.save()
            return redirect('restaurants')
    return render(request, 'restaurant/update-restaurant.html', context)


