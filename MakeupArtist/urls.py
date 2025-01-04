
from django.contrib import admin
from django.urls import path

from MakeupArtist.views import *


urlpatterns = [
    path('MakeupArtisthome',MakeupArtisthome.as_view(),name="MakeupArtisthome"),
    path('MakeupArtistRegistration',MakeupArtistRegistration.as_view(),name='MakeupArtistRegistration'),
    path('MakeupBooking',MakeupBooking.as_view(),name="MakeupBooking"),
    path('Accept_MakeupBooking/<int:M_id>/',Accept_MakeupBooking.as_view(),name='Accept_MakeupBooking'),
    path('Cancel_MakeupBooking/<int:M_id>/',Cancel_MakeupBooking.as_view(),name='Cancel_MakeupBooking'),
    path('View_MakPayment',View_MakPayment.as_view(),name='View_MakPayment'),

]
