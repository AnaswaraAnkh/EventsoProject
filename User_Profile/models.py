
from django.db import models

from Admin.models import LoginTable

class User_Table(models.Model):
    First_Name=models.CharField(max_length=50,blank=True,null=True)
    Last_Name=models.CharField(max_length=50,blank=True,null=True)
    Location=models.CharField(max_length=50,blank=True,null=True)
    Phone_Number=models.BigIntegerField(blank=True,null=True)
    Email=models.CharField(max_length=50,blank=True,null=True)
    LOGINID=models.ForeignKey(LoginTable,on_delete=models.CASCADE,null=True,blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)




class Complaint(models.Model):
    USERLID = models.ForeignKey(LoginTable, on_delete=models.CASCADE, null=True, blank=True, related_name='user_complaints')
    SERVICEPROVIDERID = models.ForeignKey(LoginTable, on_delete=models.CASCADE, null=True, blank=True, related_name='serviceprovider_complaints')
    Complaint = models.CharField(max_length=50, blank=True, null=True)
    Date = models.DateField(max_length=30, blank=True, null=True)
    Reply = models.CharField(max_length=50, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    


class Rating_Review_Table(models.Model):
    USERLID = models.ForeignKey(LoginTable, on_delete=models.CASCADE, null=True, blank=True, related_name='user_reviews')
    SERVICEPROVIDERLID = models.ForeignKey(LoginTable, on_delete=models.CASCADE, null=True, blank=True, related_name='serviceprovider_reviews')
    Rating = models.IntegerField(blank=True, null=True)
    Review = models.CharField(max_length=50, blank=True, null=True)
    Date = models.DateField(max_length=30, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)


class Payment(models.Model):
    account_number=models.CharField(max_length=50)
    IFSC=models.CharField(max_length=50)
    key=models.CharField(max_length=50)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method=models.CharField(max_length=50, blank=True, null=True)
    status=models.CharField(max_length=50, blank=True, null=True)
    USERLID = models.ForeignKey(LoginTable,on_delete=models.CASCADE,blank=True,null=True,related_name='user_payment')
    SERVICEPROVIDERLID = models.ForeignKey(LoginTable, on_delete=models.CASCADE, null=True, blank=True, related_name='serviceprovider_payment')
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)


    

    

