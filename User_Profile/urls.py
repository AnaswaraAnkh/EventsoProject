
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
    
    path('UserMakeup',UserMakeup.as_view(),name='UserMakeup'),
    path('ViewMakeupGallery/<int:M_id>/',ViewMakeupGallery.as_view(),name='ViewMakeupGallery'),
    path('Camerauser',Camerauser.as_view(),name='Camerauser'),
    path('Camgallery/<int:C_id>/',Camgalley.as_view(),name='Camgallery'),
    path('EventBookingView/<int:B_id>/',EventBookingView.as_view(),name='EventBookingView'),
    path('Makeupuserbooking/<int:M_id>/',Makeupuserbooking.as_view(),name='Makeupuserbooking'),
    path('Camerabooking/<int:C_id>/',Camerabooking.as_view(),name='Camerabooking'),
    path('UserComplaintadd',UserComplaintadd.as_view(),name='UserComplaintadd'),
    path('RatingandReview',RatingandReview.as_view(),name='RatingandReview'),
    path('Viewmakeuprating/<int:mak_id>/',Viewmakeuprating.as_view(),name='Viewmakeuprating'),
    path('MakePayment/<int:S_id>/',Payments.as_view(),name='MakePayment'),
    # path('MakePaymentmakeup/<int:M_id>/<int:id>',MakePayment.as_view(),name='MakePayment'),
    # path('MakePaymentcameraman/<int:M_id>/<int:id>',MakePayment.as_view(),name='MakePayment'),
    path('Viewuserbookingstatus',Viewuserbookingstatus.as_view(),name="Viewuserbookingstatus"),
    path('Vieweventrating/<int:mak_id>/',Vieweventrating.as_view(),name='Vieweventrating'),
    path('Viewcamerarating/<int:mak_id>/',Viewcamerarating.as_view(),name='Viewcamerarating'),
    path('ViewCameraskills/<int:user_id>/',ViewCameraskills.as_view(),name='ViewCameraskills'),
    path('Camgalley/<int:C_id>/',Camgalley.as_view(),name="Camgalley")

   
    
]
