from django.contrib import admin

from Cameraman.models import  CameraBooking, CameraManProfile, GalleryImage, PhotographySkill

# Register your models here.
admin.site.register(CameraManProfile)
admin.site.register(PhotographySkill)
admin.site.register(GalleryImage)
admin.site.register(CameraBooking)


