from django.db import models
import uuid

# Create your models here.
class Restaurant(models.Model):

    VEG_NONVEG = (
        ('VEG', 'VEG'),
        ('NONVEG', 'NONVEG')
    )
    PRICE = (
        ('3000', '$$$'),
        ('1500', '$$'),
        ('800', '$')
    )
    DINE_IN = (
        ('1', 'Yes'),
        ('0', 'No')
    )
    DELIVERY = (
        ('1', 'Yes'),
        ('0', 'No')
    )
    id = models.UUIDField(default=uuid.uuid4 ,unique=True, editable=False, primary_key=True)
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=2000)
    veg_nonveg = models.CharField(max_length=50, choices=VEG_NONVEG, default="")
    price = models.CharField(max_length=30, choices=PRICE, default="$$$")
    dine_in = models.CharField(max_length=200, choices=DINE_IN, default="")
    delivery = models.CharField(max_length=200, choices=DELIVERY, default="Yes")
    contact = models.CharField(max_length=10, default="XXXXX-XXXXX")
    created = models.DateTimeField(auto_now_add=True)
    tag = models.ManyToManyField('Tag', blank= True)
    def __str__(self):
        return self.name

class Tag(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name

class Review(models.Model):
    VOTE_TYPE=(
        ('up', 'Up Vote'),
        ('down', 'Down Vote')
    )

    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    value = models.CharField(max_length=200, choices=VOTE_TYPE)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    def __str__(self):
        return self.name
