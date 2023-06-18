from typing import Any, Dict
from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404
from django.http.response import JsonResponse
import os
from accounts.models import ShiftDaily
import time
import json

# Create your views here.

class HomeView(TemplateView):
    template_name=os.path.join("shiftcontrol","home.html")

class LoginHomeView(LoginRequiredMixin,TemplateView):
    template_name=os.path.join("shiftcontrol","login_home.html")

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context= super().get_context_data(**kwargs)
        user_id=self.request.user.id
        shift=ShiftDaily.objects.filter(user_id=user_id).all()
        shift_length=ShiftDaily.objects.filter(user_id=user_id).count()
        all_shift=[None]*shift_length
        for i,detail in enumerate(shift):
            all_shift[i]={
                    "title":detail.shift_time,
                    "date":detail.date,
                    "user":detail.user,
                }  
            
        context["all_shift"]=all_shift
        return context


            