from django import forms
from django.forms import ModelForm

from Cameraman.models import CameraBooking
from Admin import form
from MakeupArtist.models import Makeupbooking
from TeamEvent.models import Eventbooking
from User_Profile.models import Complaint, Payment, Rating_Review_Table, User_Table

class UserRegistrationForm(forms.ModelForm):
    class Meta:
        model = User_Table
        fields = ['First_Name', 'Last_Name', 'Location', 'Phone_Number', 'Email']

class EventbookingForm(forms.ModelForm):
    class Meta:
        model = Eventbooking
        fields = [ 'Event', 'Phone_Number', 'Date', ]
       

class MakeupBookingForm(forms.ModelForm):
    class Meta:
        model = Makeupbooking
        fields = [ 'Event', 'Phone_Number', 'Date', ]

class CameraBookingForm(forms.ModelForm):
    class Meta:
        model = CameraBooking
        fields = [ 'Event', 'Phone_Number', 'Date', ]


class ComplaintForm(forms.ModelForm):
    class Meta:
        model=Complaint
        fields=['Complaint','Date','Reply']

class RatingForm(form.ModelForm):
    class Meta:
        model=Rating_Review_Table
        fields=['Rating','Review','Date']

class PaymentForm(form.ModelForm):
    class Meta:
        model=Payment
        fields=['Amount','Status']

