from django.db import models

from Admin.models import LoginTable
from User_Profile.models import User_Table

# Create your models here.
class EventTeamProfile(models.Model):
    LOGINID=models.ForeignKey(LoginTable,on_delete=models.CASCADE,blank=True,null=True)
    EventName=models.CharField(max_length=30,blank=True,null=True)
    Place=models.CharField(max_length=30,blank=True,null=True)
    Post=models.CharField(max_length=30,blank=True,null=True)
    Pin=models.IntegerField(blank=True,null=True)
    Phone=models.BigIntegerField(blank=True,null=True)
    Email=models.CharField(max_length=30,blank=True,null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    


class CateringService(models.Model):
    CATERING_TYPES = [
        ('buffet', 'Buffet'),
        ('normal', 'Normal'),
    ]

    catering_name = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=15)
    email = models.EmailField()
    catering_type = models.CharField(max_length=10, choices=CATERING_TYPES)
    cost_per_plate = models.DecimalField(max_digits=10, decimal_places=2)
    menu_description = models.TextField()
    address = models.CharField(max_length=255)
    EVELID = models.ForeignKey(LoginTable,on_delete=models.CASCADE, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)

class Eventbooking(models.Model):
    USERLID = models.ForeignKey(LoginTable,on_delete=models.CASCADE,related_name='Eventuserbookings')
    EVELID = models.ForeignKey(LoginTable,on_delete=models.CASCADE,related_name='Event_bookings')
    Event = models.CharField(max_length=300, blank=True, null=True)
    Phone_Number = models.BigIntegerField(blank=True, null=True)
    Date = models.DateField(blank=True, null=True)  # Removed max_length, not applicable for DateField

    STATUS_CHOICES = [
        ('PENDING', 'Pending'),
        ('CONFIRMED', 'Confirmed'),
        ('CANCELLED', 'Cancelled')
    ]
    Status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='PENDING')
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True) 


class Decor(models.Model):
    CATEGORY_CHOICES = [
        ('Table Setup', 'Table Setup'),
        ('Lighting', 'Lighting'),
        ('Floral Arrangement', 'Floral Arrangement'),
        ('Centerpiece', 'Centerpiece'),
        ('Stage Decoration', 'Stage Decoration'),
    ]
    EVELID = models.ForeignKey(LoginTable, on_delete=models.CASCADE,related_name='eve')
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='static')
   
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True) 


class FoodMenu(models.Model):
    CATEGORY_CHOICES = [
        ('Appetizer', 'Appetizer'),
        ('Main Course', 'Main Course'),
        ('Dessert', 'Dessert'),
        ('Beverage', 'Beverage'),
    ]

    name = models.CharField(max_length=100)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='static')
    catering_service = models.ForeignKey(CateringService, on_delete=models.CASCADE, related_name="food_items")
    
    EVELID=models.ForeignKey(LoginTable,on_delete=models.CASCADE,null=True,blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True) 





   
 