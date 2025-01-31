from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from django.views import View


from Admin.models import LoginTable
from Cameraman.models import GalleryImage
from TeamEvent.models import CateringService, Eventbooking
from User_Profile.models import Complaint, Payment, Rating_Review_Table
from TeamEvent.form import CateringServiceForm, DecorForm, EvegalleryForm, FoodMenuForm

# Create your views here.
class Eventteam_home(View):
    def get(self, request):
        return render(request, "Eventteamhome.html")
    
class Catering_Reg(View):
    def get(self,request):
        return render(request,"cateringservice.html")
    def post(self, request):
       
        service_provider_id = request.session.get("user_id")
        
        
        try:
            service_provider = LoginTable.objects.get(id=service_provider_id)
        except LoginTable.DoesNotExist:
            return HttpResponse('''<script>alert("Invalid Service Provider");window.location="/event/Adddecors"</script>''')
        
        form=CateringServiceForm(request.POST)   
        
        if form.is_valid():
           
            catering = form.save(commit=False)
            
           
            catering.EVELID = service_provider 
            
            
            catering.save()
            return HttpResponse('''<script>alert("Catering Service Added");window.location="/event/Eventteam_home"</script>''')
        return HttpResponse('''<script>alert("Failed");window.location="/event/Eventteam_home"</script>''')
    
    
class AddEventgallery(View):
    def get(self, request):
        eventteamid = request.session.get("user_id")
        obj=GalleryImage.objects.filter(LOGINID=eventteamid)
        return render(request, "Evegalleryadd.html",{'images':obj})
    def post(self, request):
        # Retrieve the user ID from the session
        eventteamid = request.session.get("user_id")
        if not eventteamid:
            return render(request, "Evegalleryadd.html", {
                "error": "User not logged in or session expired.",
                "form": EvegalleryForm(),
                "images": GalleryImage.objects.all(),
            })

        # Handle the form submission
        form = EvegalleryForm(request.POST, request.FILES)
        if form.is_valid():
            gallery_image = form.save(commit=False)  # Create the instance but don't save it yet
            gallery_image.LOGINID_id = eventteamid  # Assign the foreign key
            gallery_image.save()  # Save the instance to the database
            return HttpResponse('''<script>alert("Added");window.location="/event/upload-image"</script>''')  # Redirect to the gallery page or any other desired URL

        # If the form is not valid, re-render the form with errors
        images = GalleryImage.objects.all()
        return render(request, "Evegalleryadd.html", {'images': images, 'form': form, 'error': form.errors})



class View_EventPayment(View):
    def get(self, request):
        Serviceproviderid = request.session.get("user_id")
        print(Serviceproviderid)
        
        # Use select_related to join related tables efficiently
        obj = Payment.objects.filter(SERVICE_ID=Serviceproviderid).select_related('ACCOUNT_ID', 'ACCOUNT_ID__USERLID')
        print(obj)
        
        return render(request, "ViewEventpayment.html", {'val': obj})

     
class View_Eventcomplaint(View):
    def get(self, request):
        Serviceproviderid = request.session.get("user_id")
        print(Serviceproviderid)
        obj = Complaint.objects.filter(SERVICEPROVIDERID=Serviceproviderid).select_related('USERLID')
        print(obj)
        return render(request, "EveComplaint.html", {'val': obj})

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
    

class ViewEventRating_Review(View):
    def get(self,request):
     Serviceproviderid = request.session.get("user_id")
     obj=Rating_Review_Table.objects.filter(SERVICEPROVIDERLID=Serviceproviderid).select_related('USERLID')
     print(obj)
     return render(request, "ViewRatingReview.html",{'val':obj})
    

class EventteamBooking(View):
    def get(self,request):
        Serviceproviderid = request.session.get("user_id")
        print(Serviceproviderid)
        obj=Eventbooking.objects.filter(Status='PENDING',EVELID=Serviceproviderid)
        print(obj)
        return render(request,"VerifyEventBooking .html",{'val':obj})
    
class Accept_EventteamBooking(View):
    def get(self, request, E_id):
            eve =Eventbooking.objects.get(id=E_id)
            print(eve)  # Fetch the instance
            eve.Status = 'CONFIRMED'  # Update the status
            eve.save()  # Save the changes
            return HttpResponse('''<script>alert("successfully Confirmed");window.location="/event/EventteamBooking"</script>''') 
    
class Cancel_EventBooking(View):
    def get(self, request, E_id):
            eve=Eventbooking .objects.get(id=E_id)
            print(eve)  # Fetch the instancE
            eve.Status = 'CANCELLED'  # Update the status
            eve.save()  # Save the changes
            return HttpResponse('''<script>alert("successfully Canceleld");window.location="/event/EventteamBooking"</script>''') 
    


class Adddecors(View):
    def get(self, request):
        return render(request, "decor.html")

    def post(self, request):
       
        service_provider_id = request.session.get("user_id")
        
        
        try:
            service_provider = LoginTable.objects.get(id=service_provider_id)
        except LoginTable.DoesNotExist:
            return HttpResponse('''<script>alert("Invalid Service Provider");window.location="/event/Adddecors"</script>''')
        
        form = DecorForm(request.POST, request.FILES)
        
        if form.is_valid():
           
            decor = form.save(commit=False)
            
           
            decor.EVELID = service_provider 
            
            
            decor.save()
            return HttpResponse('''<script>alert("Item Added");window.location="/event/Adddecors"</script>''')
        
        return HttpResponse('''<script>alert("Failed");window.location="/event/Adddecors"</script>''')
    
class AddfoodMenu(View):
    def get(self,request):
        obj=CateringService.objects.all()
        print(obj)
        return render(request,"foodmenu.html",{'val':obj})
    def post(self, request):
       
        service_provider_id = request.session.get("user_id")
        
        
        try:
            service_provider = LoginTable.objects.get(id=service_provider_id)
        except LoginTable.DoesNotExist:
            return HttpResponse('''<script>alert("Invalid Service Provider");window.location="/event/Adddecors"</script>''')
        
        form=FoodMenuForm(request.POST,request.FILES)   
        
        if form.is_valid():
           
            food = form.save(commit=False)
            
           
            food.EVELID = service_provider 
            
            
            food.save()
            return HttpResponse('''<script>alert("Item Added");window.location="/event/Eventteam_home"</script>''')
        return HttpResponse('''<script>alert("Failed");window.location="/event/Eventteam_home"</script>''')
    
    
    
    

    

     