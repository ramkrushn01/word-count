from django.shortcuts import render,HttpResponse,redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.core.exceptions import *

from wordapp.models import Contact
# Create your views here.
def userIsKnown(request):
    infoDist = dict()
    if request.user.is_anonymous:
        infoDist = {"user":False}
        return infoDist
    else:
        infoDist = {"user":True}
        return infoDist

def home(request):
    infoDist = userIsKnown(request)
    infoDist['username'] = request.user
    return render(request,'home.html',infoDist)

def membership(request):
    return render(request,'membership.html',userIsKnown(request))

def contact(request):
    infoDist = userIsKnown(request)
    if request.method == "POST":
        try:
            email = request.POST.get('email')
            name = request.POST.get('name')
            message = request.POST.get('message')
            contact = Contact(email=email,name=name,message=message)
            contact.save()
            messages.success(request,"Message save successful! Thanks for communicating")
            return redirect('/contact')
        except Exception as ee:
            print(ee)
            messages.error("Internal Server Error!")
            return redirect('/contact')

    if infoDist.get('user'):
        user = User.objects.get(username=request.user)
        infoDist['email'] = user.email
        infoDist['name'] = user.username
        
    return render(request,'contact.html',infoDist)

def about(request):
    return render(request,'about.html',userIsKnown(request))

def textHistory(request):
    messages.success(request,"This featured available coming soon !")
    return render(request,'history.html') 

def signUpUser(request):
    if request.method == "POST":
        try:
            name = request.POST.get('name')
            surname = request.POST.get('surname')
            email = request.POST.get('email')
            password = request.POST.get('password')
            user = User.objects.create_user(username=name,email=email,password=password)
            user.last_name = surname
            user.save()
            messages.success(request,"Create user successfully!")
            return redirect('/')
        except Exception as ee:
            print(str(ee))
            if "Duplicate entry" in str(ee):
                messages.error(request,"User already exist goto login page !")
            else:
                messages.error(request,"Internal server error")

    return render(request,'signup.html',userIsKnown(request))


def loginUser(request):
    if request.method == "POST":
        try:
            username = request.POST.get("username")
            password = request.POST.get("password")
            user = authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
                messages.success(request,"Login Successful !")
                return redirect('/')
            else:
                messages.error(request,"Check username and password is case sensitive !")
        except Exception as ee:
            print(ee)
            messages.error(request,"Internal server error")

    return render(request,'login.html',userIsKnown(request))


def logoutUser(request):
    if userIsKnown(request):
        logout(request)
        messages.success(request,"Logout successful !")
        return redirect('/login')
    else:
        messages.error(request,"Login first !")
        return redirect('/login')

def forgotPassword(request):
    if userIsKnown(request).get('user'):
        messages.warning(request,"Logout first and forgot password")
        return redirect('/')

    if request.method == "POST":
        try:
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = User.objects.get(username=username)
            if user is not None:
                user.set_password(password)
                user.save()
                messages.success(request,"Password reset successful !")
                return redirect('/login')
            else:
                messages.error(request,"Please enter correct username !")
                return redirect('/forgotpassword')
        
        except Exception as ee:
            print(ee.args)
            messages.error(request,"Internal server error !")
        
    return render(request,'forgotpassword.html')
