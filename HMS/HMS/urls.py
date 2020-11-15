"""HMS URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from core import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name="home"),
    path('signup/',views.signupfunction,name="signup"),
    path('login/',views.loginfunction,name="login"),
    path('dashboard/',views.dashboard,name="dashboard"),
    path('logout/',views.logoutfunction,name="logout"),
    path('profile/',views.profilefunction,name="profile"),
    path('specialisation/',views.specialisationfunction,name="specialisation"),
    path('addspecialisation/',views.addspecialisationfunction,name="addspecialisation"),
    path('deletespecialisation/<int:id>/',views.deletespecialisationfunction,name="deletespecialisation"),
    path('editspecialisation/<int:id>/',views.editspecialisationfunction,name="editspecialisation"),
    path('availabledoctors/',views.availabledoctorsfunction,name="availabledoctors"),
    path('adddoctor/',views.adddoctorfunction,name="adddoctor"),
    path('deletedoctor/<int:id>/',views.deletedoctorfunction,name="deletedoctor"),
    path('editdoctor/<int:id>/',views.editdoctorfunction,name="editdoctor"),
    path('availablepatients/',views.availablepatientfunction,name="availablepatients"),
    path('addpatient/',views.addpatientfunction,name="addpatient"),
    path('deletepatient/<int:id>/',views.deletepatientfunction,name="deletepatient"),
    path('editpatient/<int:id>/',views.editpatientfunction,name="editpatient"),
    path('changepass/',views.passwordchangefunction,name="changepass"),
    path('searchpatient/',views.searchpatientfunction,name="searchpatient"),
    path('selectdepartment/',views.selectdepartmentfunction,name="selectdepartment"),
    path('bookappointment/',views.bookappointmentfunction,name="bookappointment"),
    path('userappointmenthistory/',views.user_appointment_history_function,name="userappointmenthistory"),
    path('todayappointment/',views.admin_today_appointment_function,name="todayappointment"),
    path('todayappointmentdelete/<int:id>/',views.today_appointment_delete_function,name="todayappointmentdelete"),
    path('todayappointmentedit/<int:id>/',views.today_appointment_edit_function,name="todayappointmentedit"),
    path('commingappointment/',views.admin_comming_appointment_function,name="commingappointment"),
    path('commingappointmentdelete/<int:id>/',views.comming_appointment_delete_function,name="commingappointmentdelete"),
    path('historyappointment/',views.admin_history_appointment_function,name="historyappointment"),
    path('historyappointmentdelete/<int:id>/',views.history_appointment_delete_function,name="historyappointmentdelete"),
    path('contactus/',views.contactusfunction,name="contactus"),

]
