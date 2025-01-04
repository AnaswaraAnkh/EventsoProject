
from django.contrib import admin
from django.urls import path

from User_Profile.views import  *
from TeamEvent.views import *
from MakeupArtist.views import *


urlpatterns = [
    path('Userselect',Userselect.as_view(),name='Userselect'),
    path('User_Home',User_Home.as_view(),name='User_Home'),
    path('UserEvntPlan',UserEvntPlan.as_view(),name='UserEvntPlan'),
    path('EventDetails/<int:E_id>/',EventDetails.as_view(),name='EventDetails'),
    path('Eventgallery/<int:E_id>/',Eventgallery.as_view(),name='Eventgallery'),
    path('UserMakeup',UserMakeup.as_view(),name='UserMakeup'),
    path('MakeupGallery/<int:M_id>/',MakeupGallery.as_view(),name='MakeupGallery'),
    path('Camerauser',Camerauser.as_view(),name='Camerauser'),
    path('Camgallery/<int:C_id>/',Camgalley.as_view(),name='Camgallery'),
    path('EventBookingView/<int:B_id>/',EventBookingView.as_view(),name='EventBookingView'),
    path('Makeupuserbooking/<int:M_id>/',Makeupuserbooking.as_view(),name='Makeupuserbooking'),
    path('Camerabooking/<int:C_id>/',Camerabooking.as_view(),name='Camerabooking'),
    path('UserComplaintadd',UserComplaintadd.as_view(),name='UserComplaintadd'),
    path('RatingandReview',RatingandReview.as_view(),name='RatingandReview'),
    
    path('MakePayment/<int:M_id>/',MakePayment.as_view(),name='MakePayment'),
    path('Viewuserbookingstatus',Viewuserbookingstatus.as_view(),name="Viewuserbookingstatus"),
   
    
]
