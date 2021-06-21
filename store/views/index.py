from django.shortcuts import render,redirect
from django.views.generic.base import View
from store.models.product import Product
from store.models.category import Category



# Create your views here.

    





class Index(View):
    def get(self,request):
        cart=request.session.get('cart')
        if not cart:
            request.session['cart']={}
        products=Product.get_all_products()
        category=Category.get_all_categories()
        categoryID=request.GET.get('category')
        if(categoryID):
            products=Product.get_by_id( categoryID)
        data={}
        data['products']=products
        data['category']=category
        return  render(request,'index.html',data)

    def post(self,request):
        product=request.POST.get('id')
        remove=request.POST.get('remove')
        cart=request.session.get('cart')
        if(cart):
            quantity=cart.get(product)
            if quantity:
                if remove:
                    if quantity<=1:
                        cart.pop(product)
                    else:
                        cart[product]=quantity-1
                else:    
                    cart[product]=quantity+1
            else:
                cart[product]=1
        else:
            cart={}
            cart[product]=1
        request.session['cart']=cart
        print(cart)
        return redirect('/')

  
