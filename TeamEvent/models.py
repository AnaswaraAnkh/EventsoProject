from django.db import models

from Admin.models import LoginTable

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
   
 