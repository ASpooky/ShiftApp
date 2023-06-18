from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.views.generic.base import TemplateView,View
from django.views.generic.edit import CreateView,FormView
from .forms import (
    RegistForm,ShiftChoiceForm,UserLoginForm
)
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import authenticate,login,logout
from .models import ShiftDaily
from django.http import HttpResponse
from datetime import datetime
import os
# Create your views here.


class LoginView(FormView):
    template_name=os.path.join("accounts","login_page.html")
    form_class=UserLoginForm

    def post(self,request,*args,**kwargs):
        email=request.POST["email"]
        password=request.POST["password"]
        user=authenticate(email=email,password=password)
        if user is not None and user.is_active:
            login(request,user)
            return redirect("shiftcontrol:home")
        else:
            return redirect("accounts:login")
            
        

class RegistView(CreateView):
    template_name=os.path.join("accounts","regist.html")
    form_class=RegistForm

    success_url=reverse_lazy("shiftcontrol:home")

class ShiftChoiceView(LoginRequiredMixin,CreateView):
    template_name=os.path.join("accounts","shiftchoice.html")
    form_class=ShiftChoiceForm

    def post(self,request,*args,**kwargs):
        user=request.user
        shifts=request.POST["shift_time"]
        date=self.kwargs["day"]
        shiftdaily=ShiftDaily(shift_time=shifts,user=user,date=date)
        shiftdaily.save()
        return redirect("shiftcontrol:home")

    success_url=reverse_lazy("shiftcontrol:home")

class LogoutView(LoginRequiredMixin,View):

    def get(self,request,*args,**kwargs):
        logout(request)

        return redirect("shiftcontrol:home")
    
class CalendarView(LoginRequiredMixin,TemplateView):
    template_name=os.path.join("accounts","calendar.html")


