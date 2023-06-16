from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.views.generic.base import TemplateView,View
from django.views.generic.edit import CreateView,FormView
from .forms import (
    RegistForm,ShiftChoiceForm,UserLoginForm
)
from django.contrib.auth import authenticate,login,logout
from .models import ShiftDaily
from django.http import HttpResponse
# Create your views here.


class LoginView(FormView):
    template_name="login_page.html"
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
    template_name="regist.html"
    form_class=RegistForm

    success_url=reverse_lazy("shiftcontrol:home")

class ShiftChoiceView(CreateView):
    template_name="shiftchoice.html"
    form_class=ShiftChoiceForm

    def post(self,request,*args,**kwargs):
        user=request.user
        shifts=request.POST["shift_time"]
        shiftdaily=ShiftDaily(shift_time=shifts,user=user)
        shiftdaily.save()
        return redirect("shiftcontrol:home")

    success_url=reverse_lazy("shiftcontrol:home")

class LogoutView(View):

    def get(self,request,*args,**kwargs):
        logout(request)

        return redirect("shiftcontrol:home")
    
class CalendarView(TemplateView):
    template_name="calendar.html"

