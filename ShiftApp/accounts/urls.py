from django.urls import path
from . import views

app_name="accounts"

urlpatterns=[
    path("login/",views.LoginView.as_view(),name="login"),
    path("regist/",views.RegistView.as_view(),name="regist"),
    path("shiftchoice/",views.ShiftChoiceView.as_view(),name="shiftchoice"),
    path("logout/",views.LogoutView.as_view(),name="logout"),
    path("calendar/",views.CalendarView.as_view(),name="calendar"),
]