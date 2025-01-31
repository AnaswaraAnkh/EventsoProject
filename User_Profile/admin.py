from django.contrib import admin

from User_Profile.models import Account, Complaint, Payment, Rating_Review_Table, User_Table


# Register your models here.

admin.site.register(Complaint)
admin.site.register(User_Table)
admin.site.register(Rating_Review_Table)
admin.site.register(Account)
admin.site.register(Payment)

