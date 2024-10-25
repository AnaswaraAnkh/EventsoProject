from django.forms import ModelForm

from User_Profile.models import Complaint
from TeamEvent.models import EventTeamProfile


class AddEventForm(ModelForm):
    class Meta:
        model=EventTeamProfile
        fields=['EventName','Place','Post','Pin','Phone','Email']

        
class EventUpdateForm(ModelForm):
    class Meta:
        model=EventTeamProfile
        fields=['EventName','Place','Post','Pin','Phone','Email']

class Complaint_replyForm(ModelForm):
    class Meta:
        model=Complaint
        fields = ['Reply']