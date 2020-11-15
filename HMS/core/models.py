from django.db import models
from . import config
from django.contrib.auth.models import User
# Create your models here.
class specialisation(models.Model):
    specialisation=models.CharField(max_length=70)
    date=models.DateField()

class doctorsmodel(models.Model):
    pi=specialisation.objects.all()
    spec=[]
    for s in pi:
        spec.append((s.specialisation,s.specialisation),)
    specialisation=models.CharField(max_length=70,choices=spec)
    dname=models.CharField(max_length=70)
    address=models.TextField()
    fees=models.IntegerField()
    pno=models.CharField(max_length=10)
    email=models.EmailField()
    password=models.CharField(max_length=500)


class appointmentmodel(models.Model): 
    pi=doctorsmodel.objects.all()
    spec=[]
    for s in pi:
        spec.append((s.dname,s.dname),)
    department=models.CharField(max_length=70)
    docname=models.CharField(max_length=70,choices=spec)
    pname=models.CharField(max_length=70)
    bookingdate=models.DateField()
    appointmentdate=models.DateField()
    uname=models.CharField(max_length=70,null=True)

    