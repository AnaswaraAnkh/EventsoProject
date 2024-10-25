
from django.contrib import admin
from django.urls import path

from MakeupArtist.views import MakeupArtistRegistration, MakeupArtisthome



urlpatterns = [
    path('MakeupArtisthome',MakeupArtisthome.as_view(),name="MakeupArtisthome"),
    path('MakeupArtistRegistration',MakeupArtistRegistration.as_view(),name='MakeupArtistRegistration')
]
