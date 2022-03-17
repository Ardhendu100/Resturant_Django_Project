from django.db import models
import datetime
from django.contrib.auth.models import User,auth
# Create your models here.

class Category(models.Model):
    Name=models.CharField(max_length=50)

    def __str__(self):
        return self.Name

    @staticmethod
    def get_all_categories():
        return Category.objects.all()


class FoodItem(models.Model):
    Sno=models.AutoField(primary_key=True)
    Category=models.ForeignKey(Category, on_delete=models.CASCADE)
    Name=models.CharField(max_length=50)
    Description=models.CharField(max_length=250)
    Price=models.IntegerField()
    Image=models.ImageField(upload_to='static/images', default=" ")

    def __str__(self):
        return self.Name
    @staticmethod
    def get_foodItems_by_id(ids):
        return FoodItem.objects.filter(Sno__in=ids)   #here ids is a list so to acesss all id we need to write id__in

    @staticmethod
    def get_all_foodItems():
        return FoodItem.objects.all()

    @staticmethod
    def get_all_foodItems_by_categoryid(category_id):
        if category_id:
            return FoodItem.objects.filter(Category = category_id)
        else:
            return FoodItem.get_all_foodItems();
    

class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    password = models.CharField(max_length=20)


    def __str__(self):
        return self.first_name+" "+self.last_name+"-"+self.phone

    
class Order(models.Model):
    full_name=models.CharField(max_length=200,default=" ")
    product=models.ForeignKey(FoodItem,on_delete=models.CASCADE)
    customer=models.ForeignKey(User,on_delete=models.CASCADE,default=" ")
    quantity=models.IntegerField(default=1)
    address=models.CharField(max_length=200,default=" ")
    landmark=models.CharField(max_length=200,default=" ")
    phone=models.CharField(max_length=10,default=" ")
    email = models.EmailField(default=" ")
    price=models.IntegerField()
    date=models.DateField(default=datetime.datetime.today())
    status=models.BooleanField(default=False)
    def __str__(self):
        return self.full_name+"-"+self.phone

    @staticmethod
    def get_orders_by_customer(customer):
        return Order.objects.filter(customer=customer)


    
