from django.db import models

from Admin.models import LoginTable

# Create your models here.
class MakeupArtistProfile(models.Model):
    LOGINID=models.ForeignKey(LoginTable,on_delete=models.CASCADE,blank=True,null=True)
    MakeupArtist=models.CharField(max_length=30,blank=True,null=True)
    Address=models.CharField(max_length=100,blank=True,null=True)
    Phone=models.BigIntegerField(blank=True,null=True)
    Details=models.CharField(max_length=100,blank=True,null=True)
    Specialised=models.CharField(max_length=300,blank=True,null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)


