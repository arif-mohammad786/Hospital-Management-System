from django.shortcuts import render,HttpResponseRedirect
from .forms import signupform,loginform,profileform,specialisationform,doctorsform,passwordchangecustomform,searchpatientform,selectdepartmentform,appointmentform,contactusform
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from .models import specialisation,doctorsmodel,appointmentmodel
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm
from . import config
from datetime import date

# Create your views here.
def home(request):
    return render(request,'core/home.html')

# view function for signup
def signupfunction(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('/dashboard/')
    else:
        if request.method=="POST":
            fm=signupform(request.POST)
            if fm.is_valid():

                eml=fm.cleaned_data['email']
                usr=User.objects.filter(email=eml)
                if usr:
                    messages.warning(request,'You Have an Account With This Email !!')
                    return HttpResponseRedirect('/signup/')
                else:
                    fm.save()
                    messages.success(request,'You Have Successfully Signed Up !!!')
        else:
            fm=signupform()
    return render(request,'core/signup.html',{'form':fm})

# view function for login

def loginfunction(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('/dashboard/')
    else:
        if request.method=="POST":
            fm=loginform(request=request,data=request.POST)
            if fm.is_valid():
                uname=fm.cleaned_data['username']
                upass=fm.cleaned_data['password']
                user=authenticate(username=uname,password=upass)
                if user != None:
                    login(request,user)
                    return HttpResponseRedirect('/dashboard/')

        else:
            fm=loginform()
    return render(request,'core/login.html',{'form':fm})

# view function for logout 
def logoutfunction(request):
    if request.user.is_authenticated:
        logout(request)
        return HttpResponseRedirect('/')
    else:
        return HttpResponseRedirect('/login/')

# view function for Dashboard
def dashboard(request):
    if request.user.is_authenticated:
        if request.user.is_superuser:
            return render(request,'core/admindashboard.html')
        else:
            return render(request,'core/dashboard.html')
    else:
        return HttpResponseRedirect('/login/')
    return HttpResponseRedirect('/dashboard/')

# view function to show profile of user
def profilefunction(request):
    if request.user.is_authenticated:
        if request.method=="POST":
            fm=profileform(request.POST,instance=request.user)
            if fm.is_valid():
                fm.save()
                messages.success(request,'Successfully Saved !!!')
        else:
            fm=profileform(instance=request.user)
    else:
        return HttpResponseRedirect('/login/')
    return render(request,'core/profile.html',{'form':fm})

# view function to show all the doctors specialisations
def specialisationfunction(request):
    if request.user.is_authenticated:
        specialisations=specialisation.objects.all()
        return render(request,'core/showspecialisation.html',{'specialisations':specialisations})
    else:
        return HttpResponseRedirect('/login/')


# view function to add specialisation
def addspecialisationfunction(request):
    if request.user.is_authenticated:
        if request.method=="POST":
            fm=specialisationform(request.POST)
            if fm.is_valid():
                fm.save()
                messages.success(request,'Specialisation successfully saved !!!')
        else:
            fm=specialisationform()
        return render(request,'core/addspecialisation.html',{'form':fm})
    else:
        return HttpResponseRedirect('/login/')


# view function to delete specialisation
def deletespecialisationfunction(request,id):
    if request.user.is_authenticated:
        if request.method=="POST":
            pi=specialisation.objects.get(pk=id)
            pi.delete()
            return HttpResponseRedirect('/specialisation/')
    else:
        return HttpResponseRedirect('/login/')



# view function to edit specialisation
def editspecialisationfunction(request,id):
    if request.user.is_authenticated:
        if request.method=="POST":
            pi=specialisation.objects.get(pk=id)
            fm=specialisationform(request.POST,instance=pi)
            if fm.is_valid():
                fm.save()
                messages.success(request,'Specialisation Successfully Edited !!!')
        else:
            pi=specialisation.objects.get(pk=id)
            fm=specialisationform(instance=pi)
        return render(request,'core/editspecialisation.html',{'form':fm})
    else:
        return HttpResponseRedirect('/login/')




# view function to show all the available doctors
def availabledoctorsfunction(request):
    if request.user.is_authenticated:
        doctors=doctorsmodel.objects.all()
        return render(request,'core/availabledoctors.html',{'doctors':doctors})
    else:
        return HttpResponseRedirect('/login/')




# view function to add new doctor
def adddoctorfunction(request):
    if request.user.is_authenticated:
        if request.method=="POST":
            fm=doctorsform(request.POST)
            if fm.is_valid():
                fm.save()
                messages.success(request,'New Doctor successfully Added !!!')
        else:
            fm=doctorsform()
        return render(request,'core/adddoctor.html',{'form':fm})
    else:
        return HttpResponseRedirect('/login/')




# view function to delete doctor
def deletedoctorfunction(request,id):
    if request.user.is_authenticated:
        if request.method=="POST":
            pi=doctorsmodel.objects.get(pk=id)
            pi.delete()
            return HttpResponseRedirect('/availabledoctors/')
    else:
        return HttpResponseRedirect('/login/')




# view function to edit doctor
def editdoctorfunction(request,id):
    if request.user.is_authenticated:
        if request.method=="POST":
            pi=doctorsmodel.objects.get(pk=id)
            fm=doctorsform(request.POST,instance=pi)
            if fm.is_valid():
                fm.save()
                messages.success(request,'Doctor Successfully Edited !!!')
        else:
            pi=doctorsmodel.objects.get(pk=id)
            fm=doctorsform(instance=pi)
        return render(request,'core/editdoctor.html',{'form':fm})
    else:
        return HttpResponseRedirect('/login/')



# view function to show all the available patients
def availablepatientfunction(request):
    if request.user.is_authenticated:
        patients=User.objects.filter(is_superuser=False)
        return render(request,'core/availablepatients.html',{'patients':patients})
    else:
        return HttpResponseRedirect('/login/')

# view function to add patient by admin
def addpatientfunction(request):
    if request.user.is_authenticated:
        logout(request)
        return HttpResponseRedirect('/signup/')
    else:
        return HttpResponseRedirect('/login/')


# view function to delete patient
def deletepatientfunction(request,id):
    if request.user.is_authenticated:
        if request.method=="POST":
            pi=User.objects.get(pk=id)
            pi.delete()
            return HttpResponseRedirect('/availablepatients/')
    else:
        return HttpResponseRedirect('/login/')

    

# view function to edit patient
def editpatientfunction(request,id):
    if request.user.is_authenticated:
        if request.method=="POST":
            pi=User.objects.get(pk=id)
            fm=signupform(request.POST,instance=pi)
            if fm.is_valid():
                fm.save()
                messages.success(request,'Patient Successfully Edited !!!')
        else:
            pi=User.objects.get(pk=id)
            fm=signupform(instance=pi)
        return render(request,'core/editpatient.html',{'form':fm})
    else:
        return HttpResponseRedirect('/login/')


# view function to change the password
def passwordchangefunction(request):
    if request.user.is_authenticated:
        if request.method=="POST":
            fm=passwordchangecustomform(data=request.POST,user=request.user)
            if fm.is_valid():
                fm.save()
                messages.success(request,'Password Changed Successfully !!!')
        else:
            fm=passwordchangecustomform(user=request.user)
        return render(request,'core/changepass.html',{'form':fm})
    else:
        return HttpResponseRedirect('/login/')

# view function to search patient
def searchpatientfunction(request):
    if request.user.is_authenticated:
        if request.method=="POST":
            fm=searchpatientform(request.POST)
            if fm.is_valid():
                eml=fm.cleaned_data['email']
                patient=User.objects.get(email=eml)
                print(patient)
                print(patient.id)
                if patient:
                    return HttpResponseRedirect('/editpatient/'+str(patient.id)+'/')
                else:
                    messages.danger(request,'Patient Does Not Exist !!!')
        else:
            fm=searchpatientform()
    else:
        return HttpResponseRedirect('/login/')
    return render(request,'core/searchpatient.html',{'form':fm})


# view function to select department
def selectdepartmentfunction(request):
    if request.user.is_authenticated:
        if request.method=="GET":
            fm=selectdepartmentform(request.GET)
            if fm.is_valid():
                dprt=fm.cleaned_data['department']
                config.department=dprt
                request.session['department']=dprt
                return HttpResponseRedirect('/bookappointment/')
        else:
            fm=selectdepartmentform()
        return render(request,'core/selectdepartment.html',{'form':fm})
    else:
        return HttpResponseRedirect('/login/')

# view function to book appointment
def bookappointmentfunction(request):
    if request.user.is_authenticated:
        if request.method=="POST":
            fm=appointmentform(request.POST)
            if fm.is_valid():
                fm.save()
                messages.success(request,'Appointment Booked Successfully !!!')
        else:
            fm=appointmentform()
        pi=doctorsmodel.objects.filter(specialisation__iexact=request.session['department'])
        spec=[]
        for s in pi:
            spec.append((s.dname,s.dname),)
        fm.fields['docname'].choices=spec
        fm.fields['department'].initial=config.department
        fm.fields['uname'].initial=request.user.username
    else:
        return HttpResponseRedirect('/login/')
    return render(request,'core/bookappointment.html',{'form':fm})

# view function to show appointment history to user
def user_appointment_history_function(request):
    if request.user.is_authenticated:
        appointments=appointmentmodel.objects.filter(uname=request.user.username)
        return render(request,'core/userappointmenthistory.html',{'appointments':appointments})
    else:
        return HttpResponseRedirect('/login/')



# view function to show today's appointment to admin
def admin_today_appointment_function(request):
    if request.user.is_authenticated:
        appointments=appointmentmodel.objects.filter(appointmentdate=date.today())
        return render(request,'core/todayappointment.html',{'appointments':appointments})
    else:
        return HttpResponseRedirect('/login/')



# view function to delete today's appointment by admin
def today_appointment_delete_function(request,id):
    if request.user.is_authenticated:
        if request.method=="POST":
            pi=appointmentmodel.objects.get(pk=id)
            pi.delete()
            return HttpResponseRedirect('/todayappointment/')
    else:
        return HttpResponseRedirect('/login/')

    

# view function to edit today's appointment by admin

def today_appointment_edit_function(request,id):
    if request.user.is_authenticated:
        if request.method=="POST":
            pi=appointmentmodel.objects.get(pk=id)
            fm=appointmentform(request.POST,instance=pi)
            if fm.is_valid():
                fm.save()
                messages.success(request,'Appointment Successfully Edited !!!')
        else:
            pi=appointmentmodel.objects.get(pk=id)
            fm=appointmentform(instance=pi)
        return render(request,'core/editappointment.html',{'form':fm})
    else:
        return HttpResponseRedirect('/login/')



# view function to show comming appointment to admin
def admin_comming_appointment_function(request):
    if request.user.is_authenticated:
        appointments=appointmentmodel.objects.filter(appointmentdate__gt=date.today())
        return render(request,'core/commingappointment.html',{'appointments':appointments})
    else:
        return HttpResponseRedirect('/login/')
    

# view function to delete comming appointment by admin
def comming_appointment_delete_function(request,id):
    if request.user.is_authenticated:
        if request.method=="POST":
            pi=appointmentmodel.objects.get(pk=id)
            pi.delete()
            return HttpResponseRedirect('/commingappointment/')
    else:
        return HttpResponseRedirect('/login/')



# view function to show appointment history to admin
def admin_history_appointment_function(request):
    if request.user.is_authenticated:
        appointments=appointmentmodel.objects.filter(appointmentdate__lt=date.today())
        return render(request,'core/historyappointment.html',{'appointments':appointments})
    else:
        return HttpResponseRedirect('/login/')



# view function to delete history appointment by admin
def history_appointment_delete_function(request,id):
    if request.user.is_authenticated:
        if request.method=="POST":
            pi=appointmentmodel.objects.get(pk=id)
            pi.delete()
            return HttpResponseRedirect('/historyappointment/')
    else:
        return HttpResponseRedirect('/login/')


# view function for contact us form
def contactusfunction(request):
    fm=contactusform()
    return render(request,'core/contact.html',{'form':fm})