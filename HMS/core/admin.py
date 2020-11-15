from django.contrib import admin
from .models import specialisation,doctorsmodel,appointmentmodel
# Register your models here.
@admin.register(specialisation)
class adminspecialisation(admin.ModelAdmin):
    list_display=['id','specialisation','date']



@admin.register(doctorsmodel)
class admindoctorsmodel(admin.ModelAdmin):
    list_display=['id','specialisation','dname','address','fees','pno','email','password']


@admin.register(appointmentmodel)
class adminappointmentmodel(admin.ModelAdmin):
    list_display=['id','department','docname','pname','bookingdate','appointmentdate','uname']

