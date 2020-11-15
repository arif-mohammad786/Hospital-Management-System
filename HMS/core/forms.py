from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,UsernameField,PasswordChangeForm
from django.utils.translation import gettext,gettext_lazy as _
from .models import specialisation,doctorsmodel,appointmentmodel


class signupform(UserCreationForm):
    password1=forms.CharField(label='Password',label_suffix=" ",widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2=forms.CharField(label='Password Confirmation(again)',label_suffix=" ",widget=forms.PasswordInput(attrs={'class':'form-control'}))
    class Meta:
        model=User
        fields=['username','first_name','last_name','email']
        labels={'username':'Username','first_name':'First Name','last_name':'Last Name','email':'Email'}
        widgets={
            'username':forms.TextInput(attrs={'class':'form-control'}),
            'first_name':forms.TextInput(attrs={'class':'form-control'}),
            'last_name':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'})
        }

class loginform(AuthenticationForm):
    username=UsernameField(label_suffix=" ",widget=forms.TextInput(attrs={'autofocus':True,'class':'form-control'}))
    password=forms.CharField(label_suffix=" ",label=_("Password"),strip=False,widget=forms.PasswordInput(attrs={'autocomplete':'current-password','class':'form-control'}))

class profileform(forms.ModelForm):
    class Meta:
        model=User
        fields=['username','first_name','last_name','email','last_login','date_joined']
        widgets={
            'username':forms.TextInput(attrs={'class':'form-control'}),
            'first_name':forms.TextInput(attrs={'class':'form-control'}),
            'last_name':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control','readonly':'readonly'}),
            'last_login':forms.DateTimeInput(attrs={'class':'form-control','readonly':'readonly'}),
            'date_joined':forms.DateTimeInput(attrs={'class':'form-control','readonly':'readonly'}),

        }
class specialisationform(forms.ModelForm):
    class Meta:
        model=specialisation
        fields=['specialisation','date']
        labels={
            'specialisation':'Enter Doctor Specialisation'
        }
        
        widgets={
            'specialisation':forms.TextInput(attrs={'class':'form-control'}),
            'date':forms.DateInput(attrs={'class':'form-control','type':'date'})
        }

class doctorsform(forms.ModelForm):
    class Meta: 
        model=doctorsmodel
        fields="__all__"
        labels={
            'specialisation':'Select Doctor\'s Specialisation','dname':'Doctor\'s Name','address':'Doctor\'s Clinic Address',
            'fees':'Doctor\'s Consultancy Fees','pno':'Phone Number','email':'Doctor\'s Email'
        }
        widgets={
            'specialisation':forms.Select(attrs={'class':'form-control'}),
            'dname':forms.TextInput(attrs={'class':'form-control'}),
            'address':forms.Textarea(attrs={'class':'form-control','rows':3}),
            'fees':forms.NumberInput(attrs={'class':'form-control'}),
            'pno':forms.NumberInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
            'password':forms.PasswordInput(attrs={'class':'form-control'})     
            
                       }


class passwordchangecustomform(PasswordChangeForm):
    def __init__(self,user,*args,**kwargs):
        super(passwordchangecustomform,self).__init__(user,*args,**kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class']='form-control'


class searchpatientform(forms.Form):
    email=forms.CharField( max_length=70, required=True,label='Enter Patient\'s Email To Be Searched',label_suffix=" " ,
    widget=forms.TextInput(attrs={'class':'form-control'}))


class selectdepartmentform(forms.Form):
    pi=specialisation.objects.all()
    spec=[]
    for s in pi:
        spec.append((s.specialisation,s.specialisation),)
    department=forms.ChoiceField( required=True,label='Select Department',label_suffix=" " ,choices=spec,
    widget=forms.Select(attrs={'class':'form-control'}))



class appointmentform(forms.ModelForm):
    class Meta: 
        model=appointmentmodel
        fields="__all__"
        labels={
            'department':'Select Department','docname':'Doctor\'s Name','pname':'Patient Name','bookingdate':'Booking Date',
            'appointmentdate':'Appointment Date','uname':''
        }
        widgets={
            'department':forms.TextInput(attrs={'class':'form-control','readonly':'readonly'}),
            'docname':forms.Select(attrs={'class':'form-control'}),
            'pname':forms.TextInput(attrs={'class':'form-control'}),
            'bookingdate':forms.DateInput(attrs={'class':'form-control','type':'date'}),    
            'appointmentdate':forms.DateInput(attrs={'class':'form-control','type':'date'}),
            'uname':forms.HiddenInput()
            
             }



class contactusform(forms.Form):
    name=forms.CharField( max_length=70, required=True,label=" ",label_suffix=" " ,
    widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Name'}))
    email=forms.EmailField( required=True,label=" ",label_suffix=" " ,
    widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'Email'}))
    subject=forms.CharField( max_length=70, required=True,label=" ",label_suffix=" " ,
    widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Subject'}))
    desc=forms.TimeField( required=True,label=" ",label_suffix=" " ,
    widget=forms.Textarea(attrs={'class':'form-control','placeholder':'Name','rows':3}))