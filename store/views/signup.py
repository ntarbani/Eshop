from django.shortcuts import render,redirect
from store.models.customer import Customer
from django.contrib.auth.hashers import make_password
from django.views import View


class Signup(View):
   
    def post(self,request):
        return self.registerUser(request)
    
    def get(self,request):
        return  render(request,'signup.html')

    def registerUser(self,request):
        fname=request.POST.get('fname')
        lname=request.POST.get('lname')
        phone=request.POST.get('phone')
        email=request.POST.get('email')
        password=request.POST.get('password')
        customer=Customer(fname=fname,lname=lname,phone=phone,email=email,password=password)
        values={}
        values['fname']=fname
        values['lname']=lname
        values['phone']=phone
        values['email']=email
        error_msg=self.customer_validation(fname,lname,phone,email,password)    
        if customer.ifExists():
            error_msg="Email already present" 
            values['email']=""
        if(not error_msg):
            customer.password=make_password(customer.password)
            customer.register()
            print(email)
            return redirect('/login')
        else:
            data={}
            data={'error':error_msg,'value':values }
            return render(request,'signup.html',data)
    
    def customer_validation(fname,lname,phone,email,password):
        error_msg=None    
        
        if(len(fname)<3):
            error_msg="First Name must be atleast 3 character long"
        elif(len(lname)<3):
                error_msg="Last Name must be atleast 3 character long"
        elif(len(phone)<10):
                error_msg="Phone must be atleast 10 character long"
        elif(len(email)<10):
                error_msg="email must be atleast 10 character long" 
        
        return error_msg 

 