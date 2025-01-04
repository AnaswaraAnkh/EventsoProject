from django import forms
from django.forms import ModelForm

from Cameraman.models import GalleryImage
from TeamEvent.models import CateringService, Decor, FoodMenu
from MakeupArtist.models import MakeupArtistProfile

class CateringServiceForm(forms.ModelForm):
    class Meta:
        model = CateringService
        fields = [
            'catering_name',
            'contact_number',
            'email',
            'catering_type',
            'cost_per_plate',
            'menu_description',
            'address',
        ]


class DecorForm(forms.ModelForm):
    class Meta:
        model = Decor
        fields = ['name', 'category', 'price', 'description', 'image']

class FoodMenuForm(forms.ModelForm):
    class Meta:
        model = FoodMenu
        fields = ['name', 'category', 'price', 'image', 'catering_service']

class EvegalleryForm(forms.ModelForm):
     

      class Meta:
        model=GalleryImage
        fields=['image']




