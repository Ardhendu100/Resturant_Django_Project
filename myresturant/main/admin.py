from django.contrib import admin
from .models import FoodItem,Category,Customer,Order
# Register your models here.
admin.site.register(FoodItem)
admin.site.register(Category)
admin.site.register(Customer)
admin.site.register(Order)