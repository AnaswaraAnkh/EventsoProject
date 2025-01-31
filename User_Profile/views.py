
from django.db import IntegrityError
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views import View
import random
from .models import Account, LoginTable, User_Table

from Admin.models import LoginTable
from Cameraman.models import CameraBooking, CameraManProfile, GalleryImage, PhotographySkill
from MakeupArtist.models import MakeupArtistProfile, Makeupbooking
from User_Profile.models import Complaint, Rating_Review_Table
from TeamEvent.models import CateringService, Decor, EventTeamProfile, Eventbooking, FoodMenu
from User_Profile.form import CameraBookingForm, ComplaintForm, EventbookingForm, MakeupBookingForm, PaymentForm, RatingForm, UserRegistrationForm
from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, redirect
from django.views import View

from .models import LoginTable





class Userselect(View):
    def get(self, request):
        return render(request, "Userreg.html")

    def post(self, request):
     form = UserRegistrationForm(request.POST)
    
     if form.is_valid():
        try:
            # Check if username already exists
            if LoginTable.objects.filter(username=request.POST['username']).exists():
                return HttpResponse(
                    '''<script>alert("Username already exists! Please choose a different one.");window.location="/";</script>'''
                )
            
            # Create a new user in LoginTable with password hashing
            login_instance = LoginTable.objects.create_user(
                user_type='USER',
                username=request.POST['username'],
                password=request.POST['password']
            )
            
            # Save user registration form with reference to created user
            rf = form.save(commit=False)
            rf.LOGINID = login_instance
            rf.save()

            # Generate account details and save to Payment table
            payment_data = self.generate_account_details(login_instance.id)
            print("Payment data:", payment_data)  # Debugging: Check generated data

            # Save to Payment model
            payment_entry = Account.objects.create(
                account_number=payment_data['account_number'],
                key=payment_data['key'],
                IFSC=payment_data['IFSC'],
                amount=payment_data['amount'],
                
                USERLID=login_instance  # Verify ForeignKey field name
            )

            if payment_entry:
                print("Payment entry created successfully:", payment_entry)
            else:
                print("Payment entry creation failed.")

            return HttpResponse('''<script>alert("Registered");window.location="/"</script>''')# Update with actual URL name

        except Exception as e:
            print("Error creating user or saving payment:", e)
            form.add_error(None, "An error occurred during registration.")
    
     return render(request, "Userreg.html", {'form': form})


    def generate_account_details(self, user_id):
        """Generates account details to be saved in Payment table."""
        accntnumber = "".join(random.choice("1234567890") for _ in range(11))
        key = "".join(random.choice("1234567890") for _ in range(3))
        ifsc = "SBTR000055"
        amt = "500000"

        return {
            'account_number': accntnumber,
            'key': key,
            'IFSC': ifsc,
            'amount': amt,
            'member': user_id,
        }


    



class User_Home(View):
    def get(self,request):
        return render(request,"userhome.html")
    



class UserEvntPlan(View):
    def get(self, request):
        login_id = []
        # Get all event team profiles
        obj = EventTeamProfile.objects.all()
        print("Event team profiles:", obj)
        
        for i in obj:
            login_id.append(i.LOGINID)
        
        print("^^^$$$$$$$$$$$$$$$^^^^^", login_id)

        # Get ratings for the specific service providers
        ratings = Rating_Review_Table.objects.filter(SERVICEPROVIDERLID__in=login_id)

        # Create a mapping of LOGINID to its ratings
        rating_map = {}
        for rating in ratings:
            if rating.SERVICEPROVIDERLID not in rating_map:
                rating_map[rating.SERVICEPROVIDERLID] = []
            rating_map[rating.SERVICEPROVIDERLID].append(rating.Rating)

        print("Rating map:", rating_map)

        # Convert the event profiles to a list with ratings included
        event_profiles_with_ratings = []
        for event in obj:
            event_data = {
                'event': event,
                'ratings': rating_map.get(event.LOGINID, [])
            }
            event_profiles_with_ratings.append(event_data)

    
        return render(request, "userevent.html", {'events': event_profiles_with_ratings})

       
class EventDetails(View):
    def get(self, request, E_id):
        return render(request, "usereventdetails.html")
    
    def post(self, request, E_id):
        option = request.POST.get('select')
        obj = []
        obje = []

        if option == "decor":
            obj = Decor.objects.filter(EVELID=E_id)
        elif option == "food":
            # Fetch all catering services related to the selected event
            obje = CateringService.objects.filter(EVELID=E_id)
            for catering_service in obje:
                # Add a food_menu attribute to each catering service with its related food items
                catering_service.food_menu = FoodMenu.objects.filter(EVELID=catering_service.EVELID)
                for food in catering_service.food_menu:
                 print("Food Name:", food.name)
                 print("Image URL:", food.image.url if food.image else "No image")
               
                

        return render(
            request,
            "usereventdetails.html",
            {
                'val': obj,
                'option': option,
                'valu': obje
            }
        )
    

        

class UserMakeup(View):
    def get(self, request):
        # Get all makeup artist profiles
        obj = MakeupArtistProfile.objects.all()
        
        # Extract the LOGINIDs of each makeup artist
        login_id = [artist.LOGINID for artist in obj]
        
        # Get ratings for the specific makeup artists
        ratings = Rating_Review_Table.objects.filter(SERVICEPROVIDERLID__in=login_id)

        # Create a mapping of LOGINID to its ratings
        rating_map = {}
        for rating in ratings:
            if rating.SERVICEPROVIDERLID not in rating_map:
                rating_map[rating.SERVICEPROVIDERLID] = []
            rating_map[rating.SERVICEPROVIDERLID].append(rating.Rating)

        # Create a list of makeup artists with their ratings
        makeup_profiles_with_ratings = []
        for artist in obj:
            artist_data = {
                'artist': artist,
                'ratings': rating_map.get(artist.LOGINID, [])
            }
            makeup_profiles_with_ratings.append(artist_data)

        # Pass the data to the template
        return render(request, "Usermakeup.html", {'artists': makeup_profiles_with_ratings})

class ViewMakeupGallery(View):
    def get(self,request,M_id):
         obj=GalleryImage.objects.filter(LOGINID=M_id)
         return render(request,"Viewmakeupgallery.html",{'val':obj})
    
class Camerauser(View):
    def get(self, request):
        obj = CameraManProfile.objects.all()
        print("hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh")
        data = []
        for photographer in obj:
            skills = PhotographySkill.objects.filter(LOGINID=photographer.LOGINID)
            data.append({'photographer': photographer, 'skills': skills})
        return render(request, "UserCamera.html", {'data': data})


class Camgalley(View):
    def get(self,request,C_id):
         obj=GalleryImage.objects.filter(LOGINID=C_id)
         print(obj)
         return render(request,"Viewcameragallery.html",{'val':obj})
        
class EventBookingView(View):
    def get(self, request, B_id):
        # Render the booking form template
        form = EventbookingForm()
        return render(request, 'usereventbooking.html', {'form': form})

    def post(self, request, B_id):
        user_id = request.session.get("user_id")
        print("loginidof usr",user_id)  # Get the logged-in user's ID from the session
        if not user_id:
            return HttpResponse("User not logged in", status=401)  # Check if user is logged in

        form = EventbookingForm(request.POST)
        if form.is_valid():
            # Retrieve the LoginTable instances for user and event
            try:
                user_login = LoginTable.objects.get(id=user_id)
                print(user_login)
                event_login = LoginTable.objects.get(id=B_id)
            except LoginTable.DoesNotExist:
                return HttpResponse("User or Event not found", status=404)

            # Save the form data with additional user and event info
            booking = form.save(commit=False)  # Create the Eventbooking instance without saving
            booking.USERLID = user_login
            booking.EVELID = event_login
            booking.save()  # Save the instance with populated fields

            return HttpResponse('''<script>alert("BOOKED");window.location="/user/User_Home"</script>''')
        return HttpResponse('''<script>alert("Failed");window.location="/user/User_Home"</script>''')
    
class Makeupuserbooking(View):
    def get(self, request, M_id):
        form = MakeupBookingForm()
        return render(request, "Makeupbooking.html", {'form': form})
    
    def post(self, request, M_id):
        user_id = request.session.get("user_id")
        
        if not user_id:
            return HttpResponse("User not logged in", status=401)
        
        form = MakeupBookingForm(request.POST)
        
        if form.is_valid():
            try:
                user_login = LoginTable.objects.get(id=user_id)
                event_login = LoginTable.objects.get(id=M_id)
            except LoginTable.DoesNotExist:
                return HttpResponse("User or Event not found", status=404)

            booking = form.save(commit=False)
            booking.USERLID = user_login
            booking.MAKEUPLID = event_login
            booking.save()

            return HttpResponse('''<script>alert("BOOKED");window.location="/user/User_Home"</script>''')
        return HttpResponse('''<script>alert("Failed");window.location="/user/User_Home"</script>''')
      
        

class Camerabooking(View):
    def get(self, request, C_id):
        form = MakeupBookingForm()
        return render(request, "Makeupbooking.html",{'form':form})
    
    def post(self, request, C_id):
        user_id = request.session.get("user_id")
        
        if not user_id:
            return HttpResponse("User not logged in", status=401)
        
        form = CameraBookingForm(request.POST)
        
        if form.is_valid():
            try:
                user_login = LoginTable.objects.get(id=user_id)
                event_login = LoginTable.objects.get(id=C_id)
            except LoginTable.DoesNotExist:
                return HttpResponse("User or Event not found", status=404)

            booking = form.save(commit=False)
            booking.USERLID = user_login
            booking.CAMERAMANLID = event_login
            booking.save()

            return HttpResponse('''<script>alert("BOOKED");window.location="/user/User_Home"</script>''')
        return HttpResponse('''<script>alert("Failed");window.location="/user/User_Home"</script>''')
    

class UserComplaintadd(View):
    def get(self, request):
        event_teams = EventTeamProfile.objects.filter(is_active=True).values('LOGINID', 'EventName')
        makeup_artists = MakeupArtistProfile.objects.filter(is_active=True).values('LOGINID', 'MakeupArtist')
        camera_teams = CameraManProfile.objects.filter(is_active=True).values('LOGINID', 'StudioName')

        context = {
            'service_providers': {
                'eventTeam': list(event_teams),
                'makeupArtist': list(makeup_artists),
                'cameraman': list(camera_teams),
            }
        }
        
        return render(request, "UserComplaintadd.html", context)

    def post(self, request):
        user_id = request.session.get("user_id")
        if not user_id:
            return HttpResponse("User not logged in", status=401)
        
        form = ComplaintForm(request.POST)
        
        if form.is_valid():
            try:
                user_login = LoginTable.objects.get(id=user_id)
                print(user_login)
            except LoginTable.DoesNotExist:
                return HttpResponse("User not found", status=404)

            # Get service provider ID from form data
            service_provider_id = request.POST.get("serviceProviderName")
            
            if not service_provider_id:
                return HttpResponse("Service Provider not selected", status=400)
            
            # Convert service_provider_id to an integer
            try:
                service_provider = LoginTable.objects.get(id=int(service_provider_id))
            except (LoginTable.DoesNotExist, ValueError):
                return HttpResponse("Service Provider not found", status=404)

            # Save the complaint
            complaint = form.save(commit=False)
            complaint.USERLID = user_login
            complaint.SERVICEPROVIDERID = service_provider
            complaint.save()  # date_submitted will be set here automatically

            return HttpResponse('''<script>alert("Complaint Submitted");window.location="/user/User_Home"</script>''')
        
        return HttpResponse('''<script>alert("Failed to submit complaint");window.location="/user/User_Home"</script>''')
    

class RatingandReview(View):
    def get(self, request):
        event_teams = EventTeamProfile.objects.filter(is_active=True).values('LOGINID', 'EventName')
        makeup_artists = MakeupArtistProfile.objects.filter(is_active=True).values('LOGINID', 'MakeupArtist')
        camera_teams = CameraManProfile.objects.filter(is_active=True).values('LOGINID', 'StudioName')

        context = {
            'service_providers': {
                'eventTeam': list(event_teams),
                'makeupArtist': list(makeup_artists),
                'cameraman': list(camera_teams),
            }
        }
        
        return render(request, "Addreviewandrating.html", context)

    def post(self, request):
        user_id = request.session.get("user_id")
        if not user_id:
            return HttpResponse("User not logged in", status=401)
        
        form =RatingForm(request.POST)
        
        if form.is_valid():
            try:
                user_login = LoginTable.objects.get(id=user_id)
                print(user_login)
            except LoginTable.DoesNotExist:
                return HttpResponse("User not found", status=404)

            # Get service provider ID from form data
            service_provider_id = request.POST.get("serviceProviderName")
            print(service_provider_id)
            
            if not service_provider_id:
                return HttpResponse("Service Provider not selected", status=400)
            
            # Convert service_provider_id to an integer
            try:
                service_provider = LoginTable.objects.get(id=int(service_provider_id))
            except (LoginTable.DoesNotExist, ValueError):
                return HttpResponse("Service Provider not found", status=404)

            # Save the complaint
            complaint = form.save(commit=False)
            complaint.USERLID = user_login
            complaint.SERVICEPROVIDERLID = service_provider
            complaint.save()  # date_submitted will be set here automatically

            return HttpResponse('''<script>alert("Added");window.location="/user/User_Home"</script>''')
        
        return HttpResponse('''<script>alert("Failed to submit complaint");window.location="/user/User_Home"</script>''')
    
class Viewuserbookingstatus(View):
    def get(self, request):
        user_id = request.session.get("user_id")
        
        event_bookings = Eventbooking.objects.filter(USERLID=user_id)
        for booking in event_bookings:
            evelid = booking.EVELID
            payment = Payment.objects.filter(SERVICE_ID=evelid).first()
            if payment:
                booking.payment_status = payment.Status
            else:
                booking.payment_status = "Not Paid"  # Explicitly set to "Not Paid" if no payment found

        makeup_bookings = Makeupbooking.objects.filter(USERLID=user_id)
        for booking in makeup_bookings:
            maklid = booking.MAKEUPLID
            payment = Payment.objects.filter(SERVICE_ID=maklid).first()
            if payment:
                booking.payment_status = payment.Status
            else:
                booking.payment_status = "Not Paid"

        cameraman_bookings = CameraBooking.objects.filter(USERLID=user_id)
        for booking in cameraman_bookings:
            camlid = booking.CAMERAMANLID
            payment = Payment.objects.filter(SERVICE_ID=camlid).first()
            if payment:
                booking.payment_status = payment.Status
            else:
                booking.payment_status = "Not Paid"

        return render(request, "booking status.html", {
            'event_bookings': event_bookings,
            'makeup_bookings': makeup_bookings,
            'cameraman_bookings': cameraman_bookings
        })





from decimal import Decimal
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import LoginTable, Account, Payment

from django.contrib import messages

class Payments(View):
    def get(self, request, S_id):
        obj = LoginTable.objects.filter(id=S_id)
        user_id = request.session.get("user_id")
        obj1 = Account.objects.get(USERLID=user_id)
        return render(request, "payment.html", {'val': obj, 'val1': obj1})

    def post(self, request, S_id):
        form = PaymentForm(request.POST)
        user_id = request.session.get("user_id")
        account = Account.objects.get(USERLID=user_id)  # Get user account

        # Retrieve the entered PIN and amount
        entered_key = request.POST.get('key')
        amount = float(request.POST.get('amount'))

        # Check if entered PIN matches
        if entered_key != account.key:
            return HttpResponse('''<script>alert("Incorrect PIN!");window.location='/user/Viewuserbookingstatus'</script>''')

        # Check if sufficient balance is available
        if account.amount < Decimal(amount):  # Ensure amount is treated as Decimal
            return HttpResponse('''<script>alert("Insufficient balance!");window.location='/user/Viewuserbookingstatus'</script>''')

        # Deduct the amount from the account balance
        account.amount -= Decimal(amount)
        account.save()

        # Create the payment record
        payment = Payment(
            SERVICE_ID=LoginTable.objects.get(id=S_id),
            ACCOUNT_ID=account,
            Amount=Decimal(amount),
            Status="Paid"
        )
        payment.save()

        return HttpResponse('''<script>alert("Payment Successful!");window.location='/user/Viewuserbookingstatus'</script>''')






class Viewmakeuprating(View):
    def get(self,request,mak_id):
        obj=Rating_Review_Table.objects.filter(SERVICEPROVIDERLID=mak_id)
        print(obj)
        return render(request,"Viewmakeuprating.html",{'val':obj})
    
class Vieweventrating(View):
    def get(self,request,mak_id):
        obj=Rating_Review_Table.objects.filter(SERVICEPROVIDERLID=mak_id)
        print(obj)
        return render(request,"Vieweventrating.html",{'val':obj})
    
class Viewcamerarating(View):
    def get(self,request,mak_id):
        obj=Rating_Review_Table.objects.filter(SERVICEPROVIDERLID=mak_id)
        print(obj)
        return render(request,"Vieweventrating.html",{'val':obj})
    
class ViewCameraskills(View):
    def get(self, request, user_id):
        obj = PhotographySkill.objects.filter(LOGINID=user_id).first()  # Get the first object (or None if no object found)
        
        if obj:
            return render(request, "viewcameraskill.html", {'skill': obj})
        else:
            return render(request, "viewcameraskill.html", {'skill': None})

