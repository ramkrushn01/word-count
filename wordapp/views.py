from django.shortcuts import render,HttpResponse,redirect
from django.http import JsonResponse
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.core.exceptions import *
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
import json
from wordapp.models import Contact,Membership,Savefile

# Create your views here.
def userIsKnown(request):
    infoDist = dict()
    if request.user.is_anonymous:
        infoDist['user'] = False
        return infoDist
    else:
        infoDist['user'] = True
        infoDist['username'] = request.user.username

        return infoDist

def getPlanDetails(request):
    infoDist = userIsKnown(request)
    planDetails = dict()
    if  infoDist['user'] and Membership.objects.filter(username=infoDist['username']):
        getPlan = Membership.objects.get(username=userIsKnown(request)['username'])
        planDetails['isMember'] = True
        planDetails['plan_name'] = getPlan.plan_name
        planDetails['total_file_remaining'] = getPlan.total_file_remaining
        planDetails['old_file_number'] = getPlan.old_file_number
        planDetails['join_date'] = getPlan.join_date
        planDetails['expiry_date'] = getPlan.expiry_date
    else:
        planDetails['isMember'] = False

    return planDetails

def home(request):
    infoDist = userIsKnown(request)
    infoDist.update(getPlanDetails(request)) 
    return render(request,'home.html',infoDist)

def membership(request):
    infoDist = userIsKnown(request)
    planDetails = getPlanDetails(request)
    infoDist.update(planDetails)
    if request.GET.get('plan'):
        plan = int(request.GET.get('plan'))
        if not planDetails['isMember']:
            if plan == 49:
                total_remaining_file = 250
            elif plan == 99:
                total_remaining_file = 500
            else:
                total_remaining_file = -1
            getMembership = Membership(username = infoDist['username'],plan_name=plan,total_file_remaining=total_remaining_file)
            getMembership.save()
            messages.success(request,'Congratulations🥳 our plane is ready now!')
            return redirect('/')
        else:
            messages.error(request,'Your Plane is not expire!')
            return redirect('/membership')
        
    return render(request,'membership.html',infoDist)

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
            return redirect('/login')
        except Exception as ee:
            print(str(ee))
            if "Duplicate entry" in str(ee):
                messages.error(request,"User already exist goto login page !")
            else:
                messages.error(request,"Internal server error")
    if userIsKnown(request)['user']:
        messages.success(request,'You are already login please logout and try again')
        return redirect('/')

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
    if userIsKnown(request)['user']:
        messages.success(request,'You are already login')
        return redirect('/')

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


# for api
@csrf_exempt
def saveFile(request):
    infoDist = userIsKnown(request)
    planDetails = getPlanDetails(request) 
    if request.method == "POST":
        if planDetails['isMember']:
            POST_Data = json.loads(request.body.decode('utf-8'))
            username = infoDist['username']
            fileContent = POST_Data['fileData']
            fileNumber = POST_Data['fileNumber']
            print(fileNumber,fileContent)
            if Savefile.objects.filter(username=username,file_number=fileNumber):
                filesave = Savefile.objects.get(username=username,file_number=fileNumber)
                filesave.file_content = fileContent
                filesave.date = timezone.now()
                filesave.time = timezone.now()
                filesave.save()
            else:
                filesave = Savefile(username=username,file_content=fileContent,file_number=fileNumber)
                filesave.save()

            return JsonResponse({'success':True,'reason':'Text save successfully!','file_number':filesave.file_number})

        else:
            return JsonResponse({'success':False,'reason':'Please get membership first and try again!'})

    if request.GET.get('update-file') == 'true':
        pass
    
    return JsonResponse({'ram':'ram'})
