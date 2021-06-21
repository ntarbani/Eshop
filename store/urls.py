from django.contrib import admin
from django.urls import path
from .views import  index,login,signup,cart,checkout,orders
#from .middleware.auth import auth_middleware

urlpatterns = [
    path('', index.Index.as_view(),name='index'),
    path('signup', signup.Signup.as_view(),name='signup'), 
    path('login', login.Login.as_view(),name='login'), 
    path('logout', login.logout,name='logout'),
    path('cart', cart.Cart.as_view(),name='cart'),
    path('checkout', checkout.CheckOut.as_view(),name='checkout'),
    path('orders', orders.Orders.as_view(),name='orders'),  #path('orders', auth_middleware(orders.Orders.as_view()),name='orders'),
]
