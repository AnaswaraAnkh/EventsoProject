import json
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views import View
from django.contrib import messages

from Admin.models import LoginTable,Token
from django.contrib.auth import authenticate

from Admin.form import AddEventForm, Complaint_replyForm, EventUpdateForm
from Cameraman.models import CameraManProfile
from User_Profile.models import Complaint
from MakeupArtist.models import MakeupArtistProfile
from TeamEvent.models import EventTeamProfile

# Create your views here.
class Login(View):
    def get(self,request):
        return render(request,"login.html")
    def post(self, request):
        user_type = ""
        response_dict = {"success": False}
        landing_page_url = {
            "Admin": "Adminhome",
            "CameraMan":"Cameramanhome",
            "MakeupArtist":"MakeupArtisthome",
            "EventTeam": "Eventteam_home",
            "USER":"User_Home"




        }
        username = request.POST.get("username")
        print(username, 'username')
        password = request.POST.get("password")
        print(password, 'password')

        try:

            user = LoginTable.objects.get(username=username)
        except LoginTable.DoesNotExist:
            response_dict[
                "reason"
            ] = "no account found for this user name,please sign up."
            messages.error(request, response_dict["reason"])
            print(response_dict["reason"])
            return render(request,'login.html', {"error_message": response_dict.get("reason", "")})

        user = LoginTable.objects.filter(username=username, is_active="False").first()
        # print("is_activestatus",user.is_active)
        if user:
            response_dict[
                "reason"
            ] = "user is inactive ,pls contact admin."
            messages.error(request, response_dict["reason"])
            print(response_dict["reason"])
            return render(request,'login.html', {"error_message": response_dict.get("reason", "")})
        # authenticated = authenticate(email=username, password=password)
        # try:
        # print("invalid credentials")
        # user = Userprofile.objects.filter(email=username,is_active=True,password=password).first()
        # if user:
        #     response_dict[
        #         "reason"
        #     ]="invalid credentials."
        #     messages.error(request,response_dict["reason"])
        #     return render(request, self.templates_name, {"error_message": response_dict.get("reason", "")})
        user = authenticate(username=username, password=password)

        # user = Userprofile.objects.filter(email=username, is_active="True",password=password).first()
        print(user, 'auth')
        if user:
            session_dict = {"real_user": user.id}
            token, c = Token.objects.get_or_create(
                user=user, defaults={"session_dict": json.dumps(session_dict)}
            )

            user_type = user.user_type
            request.session["data"] = {
                "user_id": user.id,
                "user_type": user.user_type,
                "token": token.key,
                "username": user.username,
                "status": user.is_active,
            }
            print(user)
            print(user_type)
            request.session["user_id"] = user.id
            request.session["user"] = user.username
            request.session["token"] = token.key
            request.session["status"] = user.is_active
            return redirect(landing_page_url[user_type])
        else:
            response_dict[
                "reason"
            ] = "invalid credentials."
            messages.error(request, response_dict.get("reason", "An unknown error occurred"))

            print(response_dict["reason"])
            return render(request,'login.html', {"error_message": response_dict.get("reason", "")})
        return render(request,'Homepage.html', {"error_message": response_dict.get("reason","")})

    
class Adminhome(View):
    def get(self,request):
        return render(request,"Homepage.html")

class ViewEventTeam(View):
    def get(self,request):
        return render(request,"ViewEventteam.html")
    
class AddEventTeam(View):
    def get(self,request):
        return render(request,"Eventteam.html")
    def post(self,request):
        form=AddEventForm(request.POST)
        print("post")
        if form.is_valid():
            reg_form=form.save(commit=False)
            rf=LoginTable.objects.create_user(user_type='EventTeam',username=request.POST['username'],password=request.POST['password'])
            reg_form.LOGINID=rf
            rf.save()
            reg_form.save()

            return HttpResponse('''<script>alert("ADDED");window.location="ViewEventTeam"</script>''')
        return HttpResponse('''<script>alert("FAILED");window.location="ViewEventTeam"</script>''')
    
class ViewEventTeam(View):
    def get(self,request):
         obj = EventTeamProfile.objects.filter(is_active=True)
         print(obj)
         return render(request,"ViewEventteam.html",{'val':obj})

class EventTeamEdit(View):
    def get(self,request,T_id):
         obj = EventTeamProfile.objects.get(id=T_id)
         print(obj)
         return render(request,"Eventteamedit.html",{'val':obj})
    def post(self,request,T_id):
        obj =EventTeamProfile .objects.get(id=T_id)
        form = EventUpdateForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return HttpResponse('''<script>alert("successfully updated");window.location="/ViewEventTeam"</script>''')
        return HttpResponse('''<script>alert("Failed");window.location="/ViewEventTeam"</script>''')
    

class  EventTeamDlt(View):
    def get(Self,request,T_id):
        obj =EventTeamProfile.objects.get(id=T_id)
        obj.delete()
        return HttpResponse('''<script>alert("successfully deleted");window.location="/ViewEventTeam"</script>''')


        
    
class Verify_Cameraman(View):
    def get(self,request):
        
        obj=CameraManProfile.objects.filter(LOGINID__user_type='Pending')
        print(obj)
        if not obj:
            message = "No users to verify"
            return render(request, 'Viewcameraman.html', {'message': message})
        return render(request,'Viewcameraman.html',{'val':obj})
    

class Accept_CameraMan(View):
    def get(self, request, C_id):
        try:
            Cam = CameraManProfile.objects.get(id=C_id)
            print(Cam)  # Fetch the instance
            Cam.LOGINID.user_type = 'CameraMan'  # Update the status
            Cam.LOGINID.save()  # Save the changes
            return HttpResponse('''<script>alert("successfully Accepted");window.location="/Verify_Cameraman"</script>''')  
        except LoginTable.DoesNotExist:
            # Handle the case where the shop doesn't exist
            return HttpResponse("Cameraman not found", status=404)
        

class Reject_CameraMan(View):
    def get(self, request, C_id):
        try:
            Cam = CameraManProfile.objects.get(id=C_id)  # Fetch the instance
            Cam.LOGINID.user_type = 'Rejected'  # Update the status
            Cam.LOGINID.save()  # Save the changes
            return HttpResponse('''<script>alert("successfully Rejected");window.location="/"Verify_Cameraman</script>''')  
        except LoginTable.DoesNotExist:
            # Handle the case where the shop doesn't exist
            return HttpResponse("Shop not found", status=404)
        
class Verify_MakeupArtist(View):
    def get(self,request):
        
        obj=MakeupArtistProfile.objects.filter(LOGINID__user_type='Pending')
        print(obj)
        if not obj:
            message = "No users to verify"
            return render(request, 'Viewcameraman.html', {'message': message})
        return render(request,'ViewMakeupArtist.html',{'val':obj})
    
class Accept_MakeupArtist(View):
    def get(self, request, M_id):
            Mak = MakeupArtistProfile.objects.get(id=M_id)
            print(Mak)  # Fetch the instance
            Mak.LOGINID.user_type = 'MakeupArtist'  # Update the status
            Mak.LOGINID.save()  # Save the changes
            return HttpResponse('''<script>alert("successfully Accepted");window.location="/Verify_MakeupArtist"</script>''')  
        
        

class Reject_MakeupArtist(View):
    def get(self, request, M_id):
        Mak =MakeupArtistProfile .objects.get(id=M_id)  # Fetch the instance
        Mak.LOGINID.user_type = 'Rejected'  # Update the status
        Mak.LOGINID.save()  # Save the changes
        return HttpResponse('''<script>alert("successfully Rejected");window.location="/Verify_MakeupArtist"</script>''')  
        
class Viewcomplaint(View):
    def get(self, request):
        # Fetch complaints and annotate with service provider's username
        complaints = Complaint.objects.select_related('SERVICEPROVIDERID', 'USERLID').all()  # Use select_related for performance
        
        # Prepare context with complaints and corresponding service provider usernames
        complaint_data = []
        for complaint in complaints:
            complaint_data.append({
                'complaint_text': complaint.Complaint,  # Assuming this is the field for complaint text
                'service_provider_username': complaint.SERVICEPROVIDERID.username,
                'service_provider_user_type': complaint.SERVICEPROVIDERID.user_type,
                'user_username': complaint.USERLID.username,  # Add user who made the complaint
                'created_at': complaint.created_at,
                'id': complaint.id,  # Include complaint ID for action links
                'Reply': complaint.Reply if hasattr(complaint, 'Reply') else None,  # Ensure Reply exists
            })
        
        return render(request, "ComplaintandReply.html", {'val': complaint_data})
        
       
class Reply(View):
    def get(self,request,C_id):
        obj=Complaint.objects.get(id=C_id)
        print(obj)
        return render(request,"Reply.html",{'val':obj})
    def post(self, request, C_id):
        obj = Complaint.objects.get(id=C_id)
        form = Complaint_replyForm(request.POST, instance=obj)

        if form.is_valid():
            form.save()
            return HttpResponse('''<script>alert("Successfully Replied");window.location="/Viewcomplaint"</script>''')
        else:
            # Print form errors for debugging
            print(form.errors)
            return HttpResponse('''<script>alert("Failed to reply. Please check form errors.");window.location="/Viewcomplaint"</script>''')
        
class Cameramanhome(View):
    def get(self,request):
        return render(request,"Cameramanhome.html")




        
        

    
    
