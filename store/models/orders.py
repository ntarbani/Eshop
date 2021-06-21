from django.db import models
from django.db.models.fields.json import DataContains
from .product import Product
from .customer import  Customer
import datetime

class Orders(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    customer=models.ForeignKey(Customer,on_delete=models.CASCADE)
    quantity=models.IntegerField(default=1)
    price=models.IntegerField()
    address=models.CharField(max_length=200,default='')
    phone=models.CharField(max_length=12,default='')
    date=models.DateField(default=datetime.datetime.today)
    status=models.BooleanField(default=False)

    def placeOrder(self):
        self.save()

    @staticmethod
    def get_order_by_customers(customer):
        return Orders.objects.filter(customer=customer).order_by('date')