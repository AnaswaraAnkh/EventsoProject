from django import forms
from django.forms import ModelForm

from MakeupArtist.models import MakeupArtistProfile

class MakeupregForm(ModelForm):
    class Meta:
        model=MakeupArtistProfile
        fields=['MakeupArtist','Address','Phone','Details','Specialised']



