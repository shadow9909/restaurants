from django.contrib import admin

# Register your models here.
from .models import Restaurant, Tag, Review

admin.site.register(Restaurant)
admin.site.register(Tag)

admin.site.register(Review)
