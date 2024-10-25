"""
URL configuration for EventsoPro project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path

from Cameraman.views import *



urlpatterns = [
    path('ServiceSelection/',ServiceSelection.as_view(),name="ServiceSelection"),
    path('CameraManreg/', CameraManreg.as_view(), name="CameraManreg"),
    path('Addskils',Addskils.as_view(),name="Addskils"),
    path('uploadImages',uploadImages.as_view(),name='uploadImages'),
    path('ViewBooking',ViewBooking.as_view(),name='ViewBooking'),
    path('Accept_Booking/<int:B_id>/',Accept_Booking.as_view(),name='Accept_Booking'),
    path('Cancel_Booking/<int:B_id>/',Cancel_Booking.as_view(),name='Cancel_Booking'),
    path('ViewRating_Review',ViewRating_Review.as_view(),name='ViewRating_Review'),
    path('CamComplaint',CamComplaint.as_view(),name='CamComplaint'),
    path('ViewCamPayment',ViewCamPayment.as_view(),name='ViewCamPayment'),
    
    

    
   
]
