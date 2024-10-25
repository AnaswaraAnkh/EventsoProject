from django.db import IntegrityError
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View

from Admin.models import *
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
        