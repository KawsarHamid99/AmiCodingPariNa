from functools import partial
from django.shortcuts import render
import io
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .serializers import StudentSerializers
from django.shortcuts import render,HttpResponseRedirect
from .forms import SignupForm,LoginForm,KhojTheSearchForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from .models import Payload
from django.contrib.auth.models import User
import datetime


# Create Signup Function for Signup.
def Signup(request):
    if request.method=="POST":
        fm=SignupForm(request.POST)
        if fm.is_valid():
            fm.save()
    else:
        fm=SignupForm()
    return render(request,"signup.html",{"form":fm})

#User Login 
def Login_page(request):
    if not request.user.is_authenticated:
        if request.method=='POST':
            fm=LoginForm(request=request,data=request.POST)
            if fm.is_valid():
                uname=fm.cleaned_data.get('username')
                password=fm.cleaned_data.get('password')
                user=authenticate(username=uname,password=password)
                if user is not None:
                    login(request,user)
                    messages.success(request,"Login Successfyully..")
                    return HttpResponseRedirect("/profile/")

        else:
            fm=LoginForm()
        return render(request,"login.html",{'form':fm})
    else:
        return HttpResponseRedirect("/profile/")

#User Profile
def profile(request):
    if request.user.is_authenticated:
        if request.method=="POST":
            fm=KhojTheSearchForm(request.POST)
            input_value=request.POST["input_value"]
            khoj=request.POST["search_value"]
            date=datetime.datetime.now()

            x="FALSE"
            v=input_value.split(",")
            khoj=int(khoj)

            for i in range(len(v)):
                v[i]=int(v[i])
                if v[i] == khoj:
                    x="TRUE"
            v.sort()
            v.reverse()
            v=str(v)
            payload=Payload(user=request.user,input_value=v,timestamp=date)
            payload.save()
        
            return render(request,"home.html",{'form':fm,"result":x})
        else:
            fm=KhojTheSearchForm()
        
        return render(request,"home.html",{'form':fm})
    else:
        return HttpResponseRedirect("/login/")


# Logout Function
def logout_page(request):
    logout(request)
    return HttpResponseRedirect("/login/")


#API
#run myapi.py to show the data

@csrf_exempt
def RestApt(request):
    if request.method=='GET':
        data={}
        fm=User.objects.all()
        i=0
        p=0
        for val in fm:
            data[i]={"status": "succes","user_id”":val.id,"payload":[]}
            
            payloads=val.payload_set.all()
            for load in payloads:
                data[i]["payload"].append({"timestamp":load.timestamp,"input_values":load.input_value})
                p=p+1
            i=i+1

        json_data=JSONRenderer().render(data)
        print(json_data)
        return HttpResponse(json_data,content_type='application/json')