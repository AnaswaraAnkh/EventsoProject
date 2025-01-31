
from django.contrib import admin
from django.urls import path

from TeamEvent.views import *
from MakeupArtist.views import *
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('Eventteam_home', Eventteam_home.as_view(), name="Eventteam_home"),
    path('Catering_Reg',Catering_Reg.as_view(),name='Catering_Reg'),
    path('View_EventPayment',View_EventPayment.as_view(),name='View_EventPayment'),
    path('View_Eventcomplaint',View_Eventcomplaint.as_view(),name='View_Eventcomplaint'),
    path('ViewEventRating_Review',ViewEventRating_Review.as_view(),name='ViewEventRating_Review'),
    path('EventteamBooking',EventteamBooking.as_view(),name='EventteamBooking'),
    path('Accept_EventteamBooking/<int:E_id>/',Accept_EventteamBooking.as_view(),name='Accept_EventteamBooking'),
    path('Cancel_EventBooking/<int:E_id>/',Cancel_EventBooking.as_view(),name='Cancel_EventBooking'),
    path('Adddecors',Adddecors.as_view(),name='Adddecors'),
    path('AddfoodMenu',AddfoodMenu.as_view(),name='AddfoodMenu'),
    path('upload-image',AddEventgallery.as_view() , name='upload_image'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    

    
]
