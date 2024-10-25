from django.db import models

from Admin.models import LoginTable

# Create your models here.
class CameraManProfile(models.Model):
    LOGINID=models.ForeignKey(LoginTable,on_delete=models.CASCADE,blank=True,null=True)
    StudioName=models.CharField(max_length=30,blank=True,null=True)
    Address=models.CharField(max_length=100,blank=True,null=True)
    Phone=models.BigIntegerField(blank=True,null=True)
    Email=models.CharField(max_length=30,blank=True,null=True)
    Details=models.CharField(max_length=300,blank=True,null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)

class PhotographySkill(models.Model):
    PACKAGE_CHOICES = [
        ('wedding', 'Wedding Package'),
        ('portrait', 'Portrait Package'),
        ('event', 'Event Package'),
    ]
    LOGINID=models.ForeignKey(LoginTable,on_delete=models.CASCADE,blank=True,null=True)
    skill_title = models.CharField(max_length=100)
    description = models.TextField()
    rate = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    package = models.CharField(max_length=50, choices=PACKAGE_CHOICES,null=True,blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)


    def __str__(self):
        return self.skill_title
    

class GalleryImage(models.Model):
    LOGINID = models.ForeignKey(LoginTable, related_name='images', on_delete=models.CASCADE)
    image=models.FileField(max_length=50,null=True,blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)


class CameraBooking(models.Model):
    USERLID = models.ForeignKey(LoginTable,on_delete=models.CASCADE,related_name='user_bookings')
    CAMERAMANLID = models.ForeignKey(LoginTable,on_delete=models.CASCADE,related_name='cameraman_bookings')
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
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)  # Use auto_now for updated_at

