from django.shortcuts import render,redirect
from store.models.customer import Customer
from store.models.orders import Orders as ord
from django.contrib.auth.hashers import check_password
from django.views import View
from store.middleware.auth import auth_middleware
from django.utils.decorators import method_decorator


class Orders(View):
    @method_decorator(auth_middleware)
    def get(self,request):
        customer=request.session.get('customer')
        orders=ord.get_order_by_customers(customer)
        orders=orders.reverse()
        return render(request,'orders.html',{'orders':orders})