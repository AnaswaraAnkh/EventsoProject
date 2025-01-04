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
from django.contrib import admin
from django.urls import path

from Admin.views import  Accept_CameraMan, Accept_MakeupArtist, AddEventTeam, Adminhome, Cameramanhome, EventTeamEdit, Login, Reject_CameraMan, Reject_MakeupArtist, Reply, Verify_Cameraman, Verify_MakeupArtist, ViewEventTeam, Viewcomplaint

urlpatterns = [
   path("",Login.as_view(),name="Login"),
   path('ViewEventTeam',ViewEventTeam.as_view(),name="ViewEventTeam"),
   path('Adminhome',Adminhome.as_view(),name='Adminhome'),
   path('Cameramanhome',Cameramanhome.as_view(),name='Cameramanhome'),
   path('AddEventTeam',AddEventTeam.as_view(),name='AddEventTeam'),
   path('EventTeamEdit/<int:T_id>/',EventTeamEdit.as_view(),name='EventTeamEdit'),
#    path('EventTeamDlt/<int:T_id>/',EventTeamDlt.as_view(),name='EventTeamDlt'),
   path('Verify_Cameraman',Verify_Cameraman.as_view(),name='Verify_Cameraman'),
   path('Accept_CameraMan/<int:C_id>/',Accept_CameraMan.as_view(),name='Accept_CameraMan'),
   path('Reject_CameraMan/<int:C_id>/',Reject_CameraMan.as_view(),name='Reject_CameraMan'),
   path('Verify_MakeupArtist',Verify_MakeupArtist.as_view(),name='Verify_MakeupArtist'),
   path('Accept_MakeupArtist/<int:M_id>/',Accept_MakeupArtist.as_view(),name='Accept_MakeupArtist'),
   path('Reject_MakeupArtist/<int:M_id>/',Reject_MakeupArtist.as_view(),name='Reject_MakeupArtist'),
   path('Viewcomplaint',Viewcomplaint.as_view(),name='Viewcomplaint'),
   path('Reply/<int:C_id>/',Reply.as_view(),name='Reply'),
]
