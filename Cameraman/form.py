from django import forms
from django.forms import ModelForm

from Cameraman.models import CameraManProfile, GalleryImage, PhotographySkill



class CameramanForm(forms.ModelForm):
    class Meta:
        model = CameraManProfile
        fields = ['StudioName', 'Address', 'Phone', 'Email', 'Details']


class PhotographySkillForm(forms.ModelForm):
    class Meta:
        model = PhotographySkill
        fields = ['skill_title', 'description', 'rate', 'package', 'price']

class GalleryImageForm(forms.ModelForm):
    class Meta:
        model = GalleryImage
        fields = ['image']

# class CameraBookingForm(forms.ModelForm):
    # class Meta:
    #     model = CameraBooking
    #     fields = ['Event', 'Phone_Number', 'Date', 'Status']
     
    
        
