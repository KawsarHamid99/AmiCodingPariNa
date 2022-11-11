from django.urls import path
from . import views
urlpatterns=[ 
    path("signup",views.Signup,name="signup"),
    path("",views.Login_page,name="login"),
    path("login/",views.Login_page,name="login"),
    path("profile/",views.profile,name="profile"),
    path("logout/",views.logout_page,name="logout"),
    
    path("RestApt/",views.RestApt,name="RestApt"),
]