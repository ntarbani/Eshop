from django.shortcuts import render,redirect
from django.views.generic.base import View
from store.models.product import Product
from store.models.category import Category
from store.models.orders import Orders
from store.models.customer import Customer



# Create your views here.
class CheckOut(View):
    def post(self,request):
        address=request.POST.get('address')
        phone=request.POST.get('phone')
        customer=request.session.get('customer')
        cart=request.session.get('cart')
        products=Product.get_product_by_ids(list(cart.keys()))

        for product in products:
            order=Orders(customer=Customer(id=customer),product=product,price=product.price,quantity=cart.get(str(product.id)),address=address,phone=phone)
            print(order.placeOrder())
        request.session['cart']={}
        return render(request,'checkout.html')