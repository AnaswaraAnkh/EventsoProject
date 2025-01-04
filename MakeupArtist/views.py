from django.db import IntegrityError
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views import View

from Admin.models import *
from User_Profile.models import Complaint, Payment
from MakeupArtist.models import Makeupbooking
from MakeupArtist.form import *

# Create your views here.
class MakeupArtistRegistration(View):
    def get(self,request):
        return render(request,"MakeupReg.html")
    def post(self, request):
        form = MakeupregForm(request.POST)
        
        if form.is_valid():
            try:
                # Check if username already exists
                if LoginTable.objects.filter(username=request.POST['username']).exists():
                    return HttpResponse('''<script>alert("Username already exists! Please choose a different one.");window.location="/"</script>''')
                
                # Create a new user
                login_instance = LoginTable.objects.create_user(
                    user_type='Pending',
                    username=request.POST['username'],
                    password=request.POST['password']
                )
                
                # Save the shop details with reference to the created user
                reg_form = form.save(commit=False)
                reg_form.LOGINID = login_instance
                reg_form.save()

                return HttpResponse('''<script>alert("Registered successfully!");window.location="/"</script>''')
            
            except IntegrityError as e:
                # Print the exact error for debugging
                print(f"IntegrityError: {e}")
                return HttpResponse('''<script>alert("An error occurred while processing your request. Please try again.");window.location="/"</script>''')
        else:
            # Print form errors for debugging
            print("Form is not valid. Errors:", form.errors)
            return HttpResponse('''<script>alert("Form submission failed. Please check the form and try again.");window.location="/"</script>''')
        
    
class MakeupArtisthome(View):
    def get (self,request):
        return render(request,"Makeuphomepage.html")
    
class MakeupBooking(View):
    def get(self,request):
        Serviceproviderid = request.session.get("user_id")
        obj=Makeupbooking.objects.filter(Status='PENDING',MAKEUPLID=Serviceproviderid)
        print(obj)
        return render(request,"Verifymakeupbooking.html",{'val':obj})
    
class Accept_MakeupBooking(View):
    def get(self, request, M_id):
            mak =Makeupbooking .objects.get(id=M_id)
            print(mak)  # Fetch the instance
            mak.Status = 'CONFIRMED'  # Update the status
            mak.save()  # Save the changes
            return HttpResponse('''<script>alert("successfully Confirmed");window.location="/mak/MakeupBooking"</script>''') 
    
class Cancel_MakeupBooking(View):
    def get(self, request, M_id):
            mak =Makeupbooking .objects.get(id=M_id)
            print(mak)  # Fetch the instance
            mak.Status = 'CANCELLED'  # Update the status
            mak.save()  # Save the changes
            return HttpResponse('''<script>alert("successfully Canceleld");window.location="/mak/MakeupBooking"</script>''') 
    
class View_MakPayment(View):
     def get(self,request):
        Serviceproviderid= request.session.get("user_id")
        print(Serviceproviderid)
        obj=Payment.objects.filter(SERVICEPROVIDERLID=Serviceproviderid).select_related('USERLID')
        print(obj)
        return render(request,"ViewCamPayment.html",{'val':obj})
     
class View_Makcomplaint(View):
    def get(self, request):
        Serviceproviderid = request.session.get("user_id")
        print(Serviceproviderid)
        obj = Complaint.objects.filter(SERVICEPROVIDERID=Serviceproviderid).select_related('USERLID')
        print(obj)
        return render(request, "CamComplaint.html", {'val': obj})

    def post(self, request):
        complaint_id = request.POST.get('complaintId')
        print("ssss",complaint_id)
        replytext = request.POST.get('Reply')
        print("ggg",replytext)
        
        if complaint_id and replytext:
            try:
                complaint = Complaint.objects.get(id=complaint_id)
                print(complaint)
                complaint.Reply = replytext
                complaint.save()
                return JsonResponse({'success': True, 'message': 'Reply submitted successfully'})
            except Complaint.DoesNotExist:
                return JsonResponse({'success': False, 'message': 'Complaint not found'})
        return JsonResponse({'success': False, 'message': 'Invalid data'})
    

    

        