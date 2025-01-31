from django.db import IntegrityError
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from django.views import View

from Admin.models import LoginTable
from Cameraman.form import CameramanForm, GalleryImageForm, PhotographySkillForm
from Cameraman.models import  CameraBooking, CameraManProfile, GalleryImage
from TeamEvent.form import EvegalleryForm
from User_Profile.models import Complaint, Payment, Rating_Review_Table

# Create your views here.
class ServiceSelection(View):
    def get(self,request):
        return render(request,"Serviceselection.html")
    
class CameraManreg(View):
    def get(self,request):
        return render(request,"CameraReg.html")
    def post(self, request):
        form = CameramanForm(request.POST)
        
        if form.is_valid():
            try:
                # Check if username already exists
                if LoginTable.objects.filter(username=request.POST['username']).exists():
                    return HttpResponse('''<script>alert("Username already exists! Please choose a different one.");window.location="{% url 'CameraManreg' %}"</script>''')
                
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

                return HttpResponse('''<script>alert("Registered successfully!");window.location="/cam/CameraManreg/"</script>''')
            
            except IntegrityError as e:
                # Print the exact error for debugging
                print(f"IntegrityError: {e}")
                return HttpResponse('''<script>alert("An error occurred while processing your request. Please try again.");window.location="{% url 'CameraManreg' %}"</script>''')
        else:
            # Print form errors for debugging
            print("Form is not valid. Errors:", form.errors)
            return HttpResponse('''<script>alert("Form submission failed. Please check the form and try again.");window.location="{% url 'CameraManreg' %} "</script>''')
        

class Addskils(View):
    def get(self,request):
        return render(request,"Addskills.html")
    def post(self, request):
        form = PhotographySkillForm(request.POST)

        if form.is_valid():
            # Get the current user from the session
            user_id = request.session.get("user_id")
            try:
                # Get the login object
                login_object = LoginTable.objects.get(id=user_id)

                # Create a new PhotographySkill object and assign the login object to it
                photography_skill = form.save(commit=False)  # Don't save to DB yet
                photography_skill.LOGINID = login_object  # Assign the login object
                photography_skill.save()  # Now save it to the DB

                return HttpResponse('''<script>alert("Successfully Added!");window.location="/cam/Addskils"</script>''')
            except LoginTable.DoesNotExist:
                return HttpResponse('''<script>alert("Failed to find user. Please log in again.");window.location="/cam/Addskils"</script>''')

        return HttpResponse('''<script>alert("Failed to add skill. Please try again.");window.location="/cam/Addskils"</script>''')
    
class AddCamGallery(View):
    def get(self, request):
        Camid = request.session.get("user_id")
        obj=GalleryImage.objects.filter(LOGINID=Camid)
        return render(request, "CamGallery.html",{'images':obj})
    def post(self, request):
        # Retrieve the user ID from the session
        camid = request.session.get("user_id")
        if not camid:
            return render(request, "CamGallery.html", {
                "error": "User not logged in or session expired.",
                "form": EvegalleryForm(),
                "images": GalleryImage.objects.all(),
            })

        # Handle the form submission
        form = EvegalleryForm(request.POST, request.FILES)
        if form.is_valid():
            gallery_image = form.save(commit=False)  # Create the instance but don't save it yet
            gallery_image.LOGINID_id = camid  # Assign the foreign key
            gallery_image.save()  # Save the instance to the database
            return HttpResponse('''<script>alert("Added");window.location="/event/upload-image"</script>''')  # Redirect to the gallery page or any other desired URL

        # If the form is not valid, re-render the form with errors
        images = GalleryImage.objects.all()
        return render(request, "CamGallery.html", {'images': images, 'form': form, 'error': form.errors})





class ViewBooking(View):
    def get(self, request):
     Serviceproviderid = request.session.get("user_id")
     obj=CameraBooking.objects.filter(Status='PENDING',CAMERAMANLID_id=Serviceproviderid)
     print(obj)
     return render(request, "VerifyCameraBooking.html",{'val':obj})
    

class Accept_Booking(View):
    def get(self, request, B_id):
            Book =CameraBooking .objects.get(id=B_id)
            print(Book)  # Fetch the instance
            Book.Status = 'CONFIRMED'  # Update the status
            Book.save()  # Save the changes
            return HttpResponse('''<script>alert("successfully Confirmed");window.location="/cam/ViewBooking"</script>''')  
    
class Cancel_Booking(View):
    def get(self, request, B_id):
            Book =CameraBooking .objects.get(id=B_id)
            print(Book)  # Fetch the instance
            Book.Status = 'CANCELLED'  # Update the status
            Book.save()  # Save the changes
            return HttpResponse('''<script>alert("successfully Cancelled");window.location="/cam/ViewBooking"</script>''')  
    
class ViewRating_Review(View):
    def get(self,request):
     Serviceproviderid = request.session.get("user_id")
     obj=Rating_Review_Table.objects.filter(SERVICEPROVIDERLID=Serviceproviderid).select_related('USERLID')
     print(obj)
     return render(request, "ViewRatingReview.html",{'val':obj})
    

class CamComplaint(View):
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
    


class ViewCamPayment(View):
    def get(self, request):
        Serviceproviderid = request.session.get("user_id")
        print(Serviceproviderid)
        
        # Use select_related to join related tables efficiently
        obj = Payment.objects.filter(SERVICE_ID=Serviceproviderid).select_related('ACCOUNT_ID', 'ACCOUNT_ID__USERLID')
        print(obj)
        
        return render(request, "ViewCamPayment.html", {'val': obj})





        
    


     

     