from django.db import models
from django.contrib.auth.models import User

class Customer(models.Model): #name,phone ,email,vehicle_no,running_km , working_status

    name=models.CharField(max_length=200)

    phone=models.CharField(max_length=200)

    email=models.EmailField()

    vehicle_no=models.CharField(max_length=200)

    running_km=models.PositiveBigIntegerField()

    working_status_choices =(

        ("pending","pending"),
        ("in-progress","in-progress"),
        ("completed","completed"),
    )
    
    work_status=models.CharField(max_length=300,choices=working_status_choices,default="pending")

    service_adviser=models.ForeignKey(User,on_delete=models.CASCADE)

    created_date=models.DateTimeField(auto_now_add=True)

    updated_date=models.DateTimeField(auto_now=True)

    is_active=models.BooleanField(default=True)

    def __str__(self):

        return self.name
    
#- customer: ForeignKey relationship to the Customer model
#- description: (string) Description of the work done on the vehicle
#- amount: (float) Amount charged for the work

class Work(models.Model):

    customer_obj=models.ForeignKey(Customer,on_delete=models.CASCADE)

    description=models.CharField(max_length=500)

    amount=models.FloatField()

    created_date=models.DateTimeField(auto_now_add=True)

    updated_date=models.DateTimeField(auto_now=True)

    is_active=models.BooleanField(default=True)



