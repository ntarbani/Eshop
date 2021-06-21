from django.db import models

class Customer(models.Model):
    fname=models.CharField(max_length=50)
    lname=models.CharField(max_length=50)
    phone=models.CharField(max_length=15)
    email=models.EmailField()
    password=models.CharField(max_length=500)


    def register(self):
        self.save()

    def ifExists(self):
        if(Customer.objects.filter(email=self.email)):
            return True
        return False
    
    def get_by_email(email):
        try: 
            return Customer.objects.get(email=email)
        except:
            return False
