from django.shortcuts import render,redirect
from store.models.customer import Customer
from django.contrib.auth.hashers import check_password
from django.views import View



class Login(View):
    returnurl=None
    def get(self,request):
        Login.returnurl=request.GET.get('return_url')
        return  render(request,'login.html')
    
    def post(self,request):
        error_msg=None
        email=request.POST.get('email')
        password=request.POST.get('password')
        customer=Customer.get_by_email(email)
        if customer:
            if(check_password(password,customer.password)):
                request.session['customer']=customer.id
                if(Login.returnurl):
                    return redirect(self.returnurl)
                return redirect('/')
            else:
                error_msg="Please enter valid Password" 
                
        else:
            error_msg="Please enter registered Email Address"
        return render(request,'login.html',{'error':error_msg})


def logout(request):
    request.session.clear()
    return redirect('/')
