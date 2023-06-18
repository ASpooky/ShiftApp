from django.urls import path
from . import views

app_name="shiftcontrol"

urlpatterns=[
    path("home/",views.HomeView.as_view(),name="home"),
    path("login_home/",views.LoginHomeView.as_view(),name="login_home"),
    #path("login_home/",views.get_shift,name="login_home"),
]