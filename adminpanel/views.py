from django.shortcuts import render, redirect
from django.apps import apps
from django.contrib.auth import authenticate,login,logout
from wordapp.models import *
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


modelDist = {'User':User,'Membership': Membership,
             'Savefile': Savefile, 'Contact': Contact}


fieldDist = {'EmailField': 'email', 'CharField': 'text',
                 'TextField': 'textarea', 'DateField': 'date', 'TimeField': 'time', 'IntegerField': 'number','AutoField':'hidden','BigAutoField':'hidden','DateTimeField':'dateTime'}

def userIsKnown(request):
    infoDist = dict()
    if request.user.is_anonymous:
        infoDist['user'] = False
        return infoDist
    else:
        infoDist['user'] = True
        infoDist['username'] = request.user.username

        return infoDist

# views here.
@login_required(login_url='/adminpanel/loginU')
def index(request):
    if request.method == 'POST':
        postData = dict(request.POST)
        tbName = postData.pop('TableName')[0]
        postData.pop('csrfmiddlewaretoken')
        postData = {k:v[0] for k,v in postData.items()}
        if request.POST.get('add') == "True":
            postData.pop('id')
            postData.pop('add')
            modelDist.get(tbName).objects.create(**postData)
        else:
            modelDist.get(request.POST.get('TableName')).objects.filter(id=postData['id']).update(**postData)

        return redirect(f'/adminpanel?table={tbName}')
        # modelDist.get(request.POST.get('TableName')).objects.create(request.POST)

    info = dict()
    info['tableNames'] = [i.__name__ for i in list(
        apps.get_app_config('wordapp').get_models())]
    info['tableNames'].insert(0,('User'))
    if request.GET.get('table'):
        table_name = request.GET.get('table')
        info['tableValues'] = modelDist.get(table_name).objects.values()
        try:
            info['tableKeys'] = info['tableValues'][0].keys
        except Exception as ee:
            pass
        info['tablename'] = table_name

    if request.GET.get('tablename'):
        tableName = request.GET.get('tablename')
        if request.GET.get('delete'):
            aId = request.GET.get('delete')
            modelDist.get(tableName).objects.filter(id=aId).delete()
            return redirect(f'/adminpanel?table={tableName}')
        elif request.GET.get('edit'):
            aId = request.GET.get('edit')
            qValues = modelDist.get(tableName).objects.values().filter(id=aId)
            qType = [fieldDist.get(i.get_internal_type())
                     for i in modelDist.get(tableName)._meta.fields]
            qFinal = dict()
            i = 0
            for key,values in dict(qValues[0]).items():
                if key == 'time':
                    qFinal[key] = [values.strftime("%H:%M"),qType[i]]
                elif key == 'date':
                    qFinal[key] = [values.strftime("%Y-%m-%d"),qType[i]]
                else:
                    qFinal[key] = [values,qType[i]]
                i+=1

            info['qValues'] = qFinal
            info['edit'] = True
            info['formTableName'] = tableName
        elif request.GET.get('add'):
            qValues = modelDist.get(tableName).objects.values()
            qType = [fieldDist.get(i.get_internal_type())
                     for i in modelDist.get(tableName)._meta.fields]
            qFinal = dict()
            i = 0
            for key,values in dict(qValues[0]).items():
                if key == 'time':
                    qFinal[key] = ['',qType[i]]
                elif key == 'date':
                    qFinal[key] = ['',qType[i]]
                else:
                    qFinal[key] = ['',qType[i]]
                i+=1

            info['qValues'] = qFinal
            info['edit'] = True
            info['add'] = True
            info['formTableName'] = tableName

    return render(request, 'adminpanel/index.html', info)


def loginUser(request):
    if userIsKnown(request)['user']:
        return redirect('/adminpanel')
    info = dict()
    if request.method == "POST":
        if userIsKnown(request)['user']:
            return redirect('/')
        
        try:
            username = request.POST.get("username")
            password = request.POST.get("password")
            user = authenticate(username=username,password=password)
            if user is not None and user.is_superuser:
                login(request,user)
                return redirect('/adminpanel')
            else:
                info['fail'] = 'Please Enter Correct username and password'
                return render(request,'adminpanel/login.html',info)
        except Exception as ee:
            print(ee)
    return render(request,'adminpanel/login.html',info)


def logoutUser(request):
    loginUser(request)
    redirect('loginU')