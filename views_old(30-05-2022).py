import json
import math
import os
import random
from datetime import date, datetime, timedelta
from io import BytesIO
from types import NoneType
from unicodedata import name
from urllib.parse import urlencode
from django.template import RequestContext
import qrcode
from cal.models import *
from core.settings import EMAIL_HOST_USER
from django.conf import settings
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.core.files import File
from django.core.files.storage import FileSystemStorage
from django.core.mail import send_mail
from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.template.loader import get_template
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from num2words import num2words
from xhtml2pdf import pisa
from base_app.models import *

# Create your views here.


def login(request):
    des = designation.objects.get(designation='trainingmanager')
    des1 = designation.objects.get(designation='trainer')
    des2 = designation.objects.get(designation='trainee')
    des3 = designation.objects.get(designation='account')
    manag = designation.objects.get(designation="manager")
    Adm1 = designation.objects.get(designation="Admin")
    design2 = designation.objects.get(designation="tester")
    design = designation.objects.get(designation="team leader")
    design1 = designation.objects.get(designation="project manager")
    design3 = designation.objects.get(designation="developer")

    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(username=email, password=password)
        if user is not None:
                request.session['SAdm_id'] = user.id
                Num1 = project.objects.count()
                Num = user_registration.objects.count()
                Trainer = designation.objects.get(designation='trainer')
                trcount = user_registration.objects.filter(
                    designation=Trainer).count()
                return redirect('SuperAdmin_dashboard')
        elif user_registration.objects.filter(email=email, password=password, designation_id=des.id, status="active").exists():
            member = user_registration.objects.get(
            email=request.POST['email'], password=request.POST['password'])
            request.session['usernametm'] = member.designation_id
            request.session['usernametm1'] = member.fullname
            request.session['usernametm2'] = member.id
            # request.session['usernamehr2'] = member.branch
            return render(request, 'dashsec.html', {'member': member})
        elif user_registration.objects.filter(email=email, password=password, designation_id=des1.id, status="active").exists():
                member = user_registration.objects.get(
                email=request.POST['email'], password=request.POST['password'])
                request.session['usernametrnr'] = member.designation_id
                request.session['usernametrnr1'] = member.fullname
                request.session['usernametrnr2'] = member.team_id
                request.session['usernametrnr2'] = member.id
                return render(request, 'trainersec.html', {'member': member})
        elif user_registration.objects.filter(email=request.POST['email'], password=password, designation_id=des2.id, status="active").exists():
                member = user_registration.objects.get(
                email=request.POST['email'], password=request.POST['password'])
                request.session['usernametrns'] = member.designation_id
                request.session['usernametrns1'] = member.fullname
                request.session['usernametrns2'] = member.id
                request.session['usernametrns3'] = member.team_id
                return render(request, 'traineesec.html', {'member': member})
        elif user_registration.objects.filter(email=request.POST['email'], password=request.POST['password'], designation_id=des3.id, status="active").exists():
                member = user_registration.objects.get(
                email=request.POST['email'], password=request.POST['password'])
                request.session['usernameacnt'] = member.designation_id
                request.session['usernameacnt1'] = member.fullname
                request.session['usernameacnt2'] = member.id
                return render(request, 'accountsec.html', {'member': member})
        elif user_registration.objects.filter(email=request.POST['email'], password=request.POST['password'], designation=manag.id, status="active").exists():
                member = user_registration.objects.get(
                    email=request.POST['email'], password=request.POST['password'])
                request.session['m_id'] = member.designation_id
                request.session['usernamets1'] = member.fullname
                request.session['usernamehr2'] = member.branch_id
                request.session['m_id'] = member.id
                mem = user_registration.objects.filter(id=member.id)
                Num = user_registration.objects.count()
                Num1 = project.objects.count()
                Trainer = designation.objects.get(designation='trainer')
                trcount = user_registration.objects.filter(
                    designation=Trainer).count()
                return render(request, 'MAN_profiledash.html', {'mem': mem, 'num': Num, 'Num1': Num1, 'trcount': trcount})
        elif user_registration.objects.filter(email=request.POST['email'], password=request.POST['password'], designation=Adm1.id, status="active").exists():
                member = user_registration.objects.get(
                    email=request.POST['email'], password=request.POST['password'])
                request.session['Adm_id'] = member.designation_id
                request.session['usernamets1'] = member.fullname
                request.session['usernamehr2'] = member.branch_id
                request.session['Adm_id'] = member.id
                Adm = user_registration.objects.filter(id=member.id)
                Num = user_registration.objects.count()
                Num1 = project.objects.count()
                Trainer = designation.objects.get(designation='trainer')
                trcount = user_registration.objects.filter(
                    designation=Trainer).count()
                return render(request, 'BRadmin_profiledash.html', {'num': Num, 'Num1': Num1, 'Adm': Adm, 'trcount': trcount})
        elif user_registration.objects.filter(email=request.POST['email'], password=request.POST['password'], designation_id=design2.id, status="active").exists():
                member = user_registration.objects.get(
                    email=request.POST['email'], password=request.POST['password'])
                request.session['usernamets'] = member.designation_id
                request.session['usernamets1'] = member.fullname
                request.session['usernamehr2'] = member.branch_id
                request.session['usernametsid'] = member.id
                if request.session.has_key('usernamets'):
                    usernamets = request.session['usernamets']
                if request.session.has_key('usernamets1'):
                    usernamets1 = request.session['usernamets1']
                else:
                   return redirect('/')
                mem = user_registration.objects.filter(
                    designation_id=usernamets) .filter(fullname=usernamets1)
                return render(request, 'TSdashboard.html', {'mem': mem})
        elif user_registration.objects.filter(email=request.POST['email'], password=request.POST['password'], designation=design.id, status="active").exists():
                member = user_registration.objects.get(
                     email=request.POST['email'], password=request.POST['password'])
                request.session['tlid'] = member.id
                if request.session.has_key('tlid'):
                    tlid = request.session['tlid']
                else:
                    return redirect('/')
                    
                return redirect( 'TLdashboard')
              
            
        elif user_registration.objects.filter(email=request.POST['email'], password=request.POST['password'],designation=design1.id,status="active").exists():
                member=user_registration.objects.get(email=request.POST['email'], password=request.POST['password'])
                request.session['prid'] = member.id
               
                if request.session.has_key('prid'):
                    prid = request.session['prid']
                else:
                   return redirect('/')
                return redirect( 'pmanager_dash')
            
            
        elif user_registration.objects.filter(email=request.POST['email'], password=request.POST['password'],designation=design3.id,status="active").exists():
                member=user_registration.objects.get(email=request.POST['email'], password=request.POST['password'])
                request.session['devid'] = member.id
               
                if request.session.has_key('devid'):
                    devid = request.session['devid']
                else:
                   return redirect('/')
                return redirect('devdashboard')
            
        else:
                context = {'msg_error': 'Invalid data'}
                return render(request, 'login.html', context)

       
    return render(request,'login.html')

#######################################################   training Manager   ##############################################
def Dashboard(request):
    if 'usernametm2' in request.session:

        if request.session.has_key('usernametm2'):
            usernametm2 = request.session['usernametm2']

        mem = user_registration.objects.filter(id=usernametm2)
        des = designation.objects.get(designation="trainer")
        des1 = designation.objects.get(designation="trainee")
        le = leave.objects.filter(Q(designation_id=des.id) | Q(
            designation_id=des1.id)).filter(leaveapprovedstatus=0)

        labels = []
        data = []
        queryset = user_registration.objects.filter(id=usernametm2)
        for i in queryset:
            labels = [i.workperformance, i.attitude, i.creativity]
            data = [i.workperformance, i.attitude, i.creativity]
        return render(request, 'Dashboard.html', {'mem': mem, 'labels': labels, 'data': data, 'le': le})
    else:
        return redirect('/')
        
        
def Newtrainees(request):
    if 'usernametm2' in request.session:
        if request.session.has_key('usernametm'):
            usernametm = request.session['usernametm']
        if request.session.has_key('usernametm1'):
            usernametm1 = request.session['usernametm1']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(
            designation_id=usernametm).filter(fullname=usernametm1)
        des = course.objects.all()
        dept = department.objects.all()
        team = create_team.objects.filter(~Q(team_status=1))
        mem1 = designation.objects.get(designation="trainee")
        memm = user_registration.objects.filter(designation_id=mem1).order_by('-id')
        return render(request, 'Newtrainees.html', {'mem': mem, 'memm': memm, 'des': des, 'dept': dept, 'team': team})
    else:
        return redirect('/')

def newtraineeesteam(request):
    if 'usernametm2' in request.session:
        if request.session.has_key('usernametm'):
            usernametm = request.session['usernametm']
        if request.session.has_key('usernametm1'):
            usernametm1 = request.session['usernametm1']
        else:
            usernametm1 = "dummy"
        mem = user_registration.objects.filter(
            designation_id=usernametm).filter(fullname=usernametm1)
        tid = request.GET.get('tid')
        register = user_registration()
        des  = course.objects.all()
        dept = department.objects.all()
        team = create_team.objects.filter(team_status = 0)
        mem1 = designation.objects.get(designation="trainee").order_by('id')
        memm = user_registration.objects.filter(designation_id=mem1)
        print(memm)
        if request.method == 'POST':
            register = user_registration.objects.get(id=tid)
            register.course =course.objects.get(id=int(request.POST['cou']))
            register.team =create_team.objects.get(id=int(request.POST['team']))
            register.department =department.objects.get(id=int(request.POST['dept']))
            users =  previousTeam()
            users.teamname = create_team.objects.get(id=int(request.POST['team']))
            users.user = user_registration.objects.get(id=tid)
            users.pstatus = 0
            users.save()
            register.save()
            return redirect('Dashboard')
        return render(request, 'Newtrainees.html', {'memm': memm, 'des': des, 'dept': dept, 'team': team, })
    else:
        return redirect('/')



def new_team(request):
    if 'usernametm2' in request.session:
        if request.session.has_key('usernametm'):
            usernametm = request.session['usernametm']
        if request.session.has_key('usernametm1'):
            usernametm1 = request.session['usernametm1']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(
            designation_id=usernametm) .filter(fullname=usernametm1)
        var = create_team.objects.filter(team_status=0).order_by('-id')
        des = designation.objects.get(designation='trainer')
        var1 = user_registration.objects.filter(designation_id=des.id)
        return render(request, 'new_team.html', {'mem': mem, 'var': var, 'var1': var1})
    else:
        return redirect('/')
        
def new_team1(request):
    if 'usernametm2' in request.session:
        if request.session.has_key('usernametm'):
            usernametm = request.session['usernametm']
        if request.session.has_key('usernametm1'):
            usernametm1 = request.session['usernametm1']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(designation_id=usernametm) .filter(fullname=usernametm1)
        des = designation.objects.get(designation='trainer')
        var = user_registration.objects.filter(designation_id=des.id)
        return render(request, 'new_team1.html', {'mem': mem, 'var': var})
    else:
        return redirect('/')
        
        
# def newteamcreate(request):
    
#     if request.session.has_key('usernametm'):
#         usernametm = request.session['usernametm']
#     if request.session.has_key('usernametm1'):
#         usernametm1 = request.session['usernametm1']
#     else:
#         return redirect('/')
#     if request.method == 'POST':
#         team = request.POST['team']
#         trainer = request.POST.get('trainer')
#         tra= user_registration.objects.get(id=trainer)
#         try:
#             user = create_team.objects.get(name=team)
#             mem = user_registration.objects.filter(
#                 designation_id=usernametm) .filter(fullname=usernametm1)
#             context = {
#                 'msg': 'Team already exists!!!....  Try another name', 'mem': mem}
#             return render(request, 'new_team1.html', context)
#         except:
#             user = create_team(name=team, trainer=tra.fullname, progress=0,trainer_id=trainer)
#             user.save()
#     return redirect('new_team')


def newteamcreate(request):

    if request.session.has_key('usernametm'):
        usernametm = request.session['usernametm']
    if request.session.has_key('usernametm1'):
        usernametm1 = request.session['usernametm1']
    else:
        return redirect('/')
    if request.method == 'POST':
        team = request.POST['team']
        startdate=request.POST['startdate']
        enddate=request.POST['enddate']
        trainer = request.POST.get('trainer')
        tra= user_registration.objects.get(id=trainer)
        try:
            user = create_team.objects.get(name=team)
            mem = user_registration.objects.filter(
                designation_id=usernametm) .filter(fullname=usernametm1)
            context = {
                'msg': 'Team already exists!!!....  Try another name', 'mem': mem}
            return render(request, 'new_team1.html', context)
        except:
            user = create_team(name=team, trainer=tra.fullname, progress=0,trainer_id=trainer,startdate=startdate,enddate=enddate)
            user.save()
    return redirect('new_team')
    
    

def trainer_trainees_details(request, id):
    if 'usernametrnr2' in request.session:

        if request.session.has_key('usernametrnr2'):
            usernametrnr2 = request.session['usernametrnr2']

        z = user_registration.objects.filter(id=usernametrnr2)
        vars = user_registration.objects.get(id=id)
        tre = create_team.objects.get(id=vars.team.id)
        k=user_registration.objects.get(id=tre.trainer_id)
        labels = []
        data = []
        queryset = user_registration.objects.filter(id=vars.id)
        for i in queryset:
            labels = [i.workperformance, i.attitude, i.creativity]

            data = [i.workperformance, i.attitude, i.creativity]
        return render(request, 'trainer_trainees_details.html', {'vars': vars, 'tre': tre,  'z': z, 'labels': labels, 'data': data,'k':k })
    else:
        return redirect('/')
        
        
        
def teamdelete(request):
    if request.session.has_key('usernametm'):
        usernametm = request.session['usernametm']
    if request.session.has_key('usernametm1'):
        usernametm1 = request.session['usernametm1']
    else:
        return redirect('/')

    tid = request.GET.get('tid')
    var = create_team.objects.filter(id=tid)
    
    var.delete()
    return redirect("new_team")

def submit(request):
    if request.session.has_key('usernametm'):
        usernametm = request.session['usernametm']
    if request.session.has_key('usernametm1'):
        usernametm1 = request.session['usernametm1']
    else:
        return redirect('/')
    tid = request.GET.get('tid')
    if request.method == 'POST':
        var1 = create_team.objects.get(id=tid)
        var1.team_status = 1
        print(var1)
        var1.save()
    return redirect("new_team")

# def teamupdate(request):
#     if request.session.has_key('usernametm'):
#         usernametm = request.session['usernametm']
#     if request.session.has_key('usernametm1'):
#         usernametm1 = request.session['usernametm1']
#     else:
#         return redirect('/')
#     if request.method == 'POST':
#         tid = request.GET.get('tid')
#         a= request.POST.get('trainer')
#         abc = create_team.objects.get(id=tid)
#         abc.name = request.POST.get('teams')
#         abc.trainer_id = request.POST.get('trainer')
#         tra= user_registration.objects.get(id=a)
#         abc.trainer = tra.fullname

#         abc.save()
#         return redirect('new_team')
#     else:
#         pass

def teamupdate(request):
    if request.session.has_key('usernametm'):
        usernametm = request.session['usernametm']
    if request.session.has_key('usernametm1'):
        usernametm1 = request.session['usernametm1']
    else:
        return redirect('/')
    if request.method == 'POST':
        tid = request.GET.get('tid')
        a= request.POST.get('trainer')
        
        abc = create_team.objects.get(id=tid)
        abc.name = request.POST.get('teams')
        abc.trainer_id = request.POST.get('trainer')
        abc.startdate = request.POST.get('startdate')
        abc.enddate = request.POST.get('enddate')
        tra= user_registration.objects.get(id=a)
        abc.trainer = tra.fullname

        abc.save()
        return redirect('new_team')
    else:
        pass

def attendance_tm(request):
    if 'usernametm2' in request.session:
        if request.session.has_key('usernametm'):
            usernametm = request.session['usernametm']
        if request.session.has_key('usernametm1'):
            usernametm1 = request.session['usernametm1']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(
            designation_id=usernametm) .filter(fullname=usernametm1)
        
        des = designation.objects.get(designation='trainee')
        vars = user_registration.objects.filter(designation=des.id)
    
        return render(request, 'attendance_tm.html',{'mem':mem})
    else:
        return redirect('/')
def Trainees_Calendar(request):
    if 'usernametm2' in request.session:
        if request.session.has_key('usernametm'):
            usernametm = request.session['usernametm']
        if request.session.has_key('usernametm1'):
            usernametm1 = request.session['usernametm1']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(
            designation_id=usernametm) .filter(fullname=usernametm1)
    
        des = designation.objects.get(designation='trainee')
        vars = user_registration.objects.filter(designation=des.id)
        
        return render(request, 'Trainees_Calendar.html',{'mem':mem, 'vars':vars})
    else:
        return redirect('/')

def Trainees_Attendancetable(request):
    if 'usernametm2' in request.session:
        if request.session.has_key('usernametm'):
            usernametm = request.session['usernametm']
        if request.session.has_key('usernametm1'):
            usernametm1 = request.session['usernametm1']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(
            designation_id=usernametm) .filter(fullname=usernametm1)   
        if request.method == 'POST':
            start=request.POST['startdate']
            end=request.POST['enddate']
            user = request.POST['trainee']
            attend=attendance.objects.filter(date__gte=start,date__lte=end,user_id=user)
        return render(request, 'Trainees_Attendancetable.html',{'mem':mem,'vars':attend})
    else:
        return redirect('/')
def Trainers_Calendar(request):
    if 'usernametm2' in request.session:
        if request.session.has_key('usernametm'):
            usernametm = request.session['usernametm']
        if request.session.has_key('usernametm1'):
            usernametm1 = request.session['usernametm1']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(
            designation_id=usernametm) .filter(fullname=usernametm1)
        des = designation.objects.get(designation='trainer')
        vars = user_registration.objects.filter(designation=des.id)
        return render(request,'Trainers_Calendar.html',{'mem':mem, 'vars':vars})
    else:
        return redirect('/')
def Trainers_Attendancetable(request):
    if 'usernametm2' in request.session:
        if request.session.has_key('usernametm'):
            usernametm = request.session['usernametm']
        if request.session.has_key('usernametm1'):
            usernametm1 = request.session['usernametm1']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(
            designation_id=usernametm) .filter(fullname=usernametm1)
        if request.method == 'POST':
            start=request.POST['startdate']
            end=request.POST['enddate']
            user = request.POST['trainer']
            attend=attendance.objects.filter(date__gte=start,date__lte=end,user_id=user).order_by('-id')  
    
        return render(request, 'Trainers_Attendancetable.html',{'mem':mem,'vars':attend})
    else:
        return redirect('/')
def Trainee(request):
    if 'usernametm2' in request.session:
        if request.session.has_key('usernametm'):
            usernametm = request.session['usernametm']
        if request.session.has_key('usernametm1'):
            usernametm1 = request.session['usernametm1']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(designation_id=usernametm).filter(fullname=usernametm1)
        des = designation.objects.get(designation='trainee')
        tre = user_registration.objects.filter(designation=des.id).all().order_by('-id')
    
        return render(request, 'traineetable.html', {'tre': tre, 'vars': vars,'mem':mem})
    else:
        return redirect('/')
def reportedissue(request):
    if 'usernametm2' in request.session:
        if request.session.has_key('usernametm'):
            usernametm = request.session['usernametm']
        if request.session.has_key('usernametm1'):
            usernametm1 = request.session['usernametm1']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(designation_id=usernametm).filter(fullname=usernametm1)
        return render(request, 'reportedissue.html', {'mem': mem})
    else:
        return redirect('/')
def reportissuetrainers(request):
    if 'usernametm2' in request.session:
        if request.session.has_key('usernametm'):
            usernametm = request.session['usernametm']
        if request.session.has_key('usernametm1'):
            usernametm1 = request.session['usernametm1']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(
            designation_id=usernametm).filter(fullname=usernametm1)
        return render(request, 'reportissuetrainers.html', {'mem': mem})
    else:
        return redirect('/')
def trainerunsolvedissue(request):
    if 'usernametm2' in request.session:
        if request.session.has_key('usernametm'):
            usernametm = request.session['usernametm']
        if request.session.has_key('usernametm1'):
            usernametm1 = request.session['usernametm1']
        if request.session.has_key('usernametm2'):
            usernametm2 = request.session['usernametm2']
        else:
            return redirect('/')
    
        mem = user_registration.objects.filter(
            designation_id=usernametm) .filter(fullname=usernametm1)
        des = designation.objects.get(designation='trainer')
       
        cut = reported_issue.objects.filter(reported_to_id=usernametm2,designation_id=des.id,issuestatus=0)
        a=cut.count()
        
        context = {'cut': cut, 'vars': vars, 'mem': mem,'a':a}
        return render(request,'trainerunsolvedissue.html',context)
    else:
        return redirect('/')
def savetmreplaytrnr(request):
    if 'usernametm2' in request.session:
        if request.session.has_key('usernametm'):
            usernametm = request.session['usernametm']
        if request.session.has_key('usernametm1'):
            usernametm1 = request.session['usernametm1']
        else:
            return redirect('/')
    
        mem = user_registration.objects.filter(
            designation_id=usernametm) .filter(fullname=usernametm1)
        id = request.GET.get('id')
        if request.method == 'POST':
            vars = reported_issue.objects.get(id=id)
            
            print(vars.reply)
            vars.reply = request.POST['review']
            
            vars.issuestatus = 1
           
            
            vars.save()
        return redirect('reportissuetrainers')
    else:
        return redirect('/')
def trainersolvedissue(request):
    if 'usernametm2' in request.session:
        if request.session.has_key('usernametm'):
            usernametm = request.session['usernametm']
        if request.session.has_key('usernametm1'):
            usernametm1 = request.session['usernametm1']
        if request.session.has_key('usernametm2'):
            usernametm2 = request.session['usernametm2']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(
            designation_id=usernametm) .filter(fullname=usernametm1)
        des = designation.objects.get(designation='trainer')
        print(des.id)
        cut = reported_issue.objects.filter(reported_to_id=usernametm2).filter(
            designation_id=des.id).filter(issuestatus=1)
        context = {'cut': cut, 'vars': vars, 'mem': mem}
        return render(request,'trainersolvedissue.html',context)
    else:
        return redirect('/')
def reportissuetrainees(request):
    if 'usernametm2' in request.session:
        if request.session.has_key('usernametm'):
            usernametm = request.session['usernametm']
        if request.session.has_key('usernametm1'):
            usernametm1 = request.session['usernametm1']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(
            designation_id=usernametm) .filter(fullname=usernametm1)
        return render(request,'reportissuetrainees.html', {'mem': mem})
    else:
        return redirect('/')
def traineesunsolved(request):
    if 'usernametm2' in request.session:
        if request.session.has_key('usernametm'):
            usernametm = request.session['usernametm']
        if request.session.has_key('usernametm1'):
            usernametm1 = request.session['usernametm1']
        if request.session.has_key('usernametm2'):
            usernametm2 = request.session['usernametm2']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(
            designation_id=usernametm) .filter(fullname=usernametm1)
        des = designation.objects.get(designation='trainee')
        # print(des.id)
        cut = reported_issue.objects.filter(reported_to_id=usernametm2).filter(
            designation_id=des.id).filter(issuestatus=0)
        context = {'cut': cut, 'vars': vars, 'mem': mem}
        return render(request,'traineesunsolved.html', context)
    else:
        return redirect('/')

def savetmreplytrns(request):
    if 'usernametm2' in request.session:
        if request.session.has_key('usernametm'):
            usernametm = request.session['usernametm']
        if request.session.has_key('usernametm1'):
            usernametm1 = request.session['usernametm1']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(
            designation_id=usernametm) .filter(fullname=usernametm1)
        id = request.GET.get('id')
        if request.method == 'POST':
            vars = reported_issue.objects.get(id=id)
            print(vars.reply)
            vars.reply = request.POST['reply']
            
            vars.issuestatus = 1
           
            vars.save()
        return redirect('reportissuetrainees')
    else:
        return redirect('/')
def traineessolved(request):
    if 'usernametm2' in request.session:
        if request.session.has_key('usernametm'):
            usernametm = request.session['usernametm']
        if request.session.has_key('usernametm1'):
            usernametm1 = request.session['usernametm1']
        if request.session.has_key('usernametm2'):
            usernametm2 = request.session['usernametm2']
        else:
            return redirect('/')
    
        mem = user_registration.objects.filter(
            designation_id=usernametm) .filter(fullname=usernametm1)
        des = designation.objects.get(designation='trainee')
        print(des.id)
        cut = reported_issue.objects.filter(reported_to_id=usernametm2).filter(
            designation_id=des.id).filter(issuestatus=1)
        context = {'cut': cut, 'vars': vars, 'mem': mem}
        return render(request,'traineessolved.html', context)
    else:
        return redirect('/')
def reportissue(request):
    if 'usernametm2' in request.session:
        if request.session.has_key('usernametm'):
            usernametm = request.session['usernametm']
        if request.session.has_key('usernametm1'):
            usernametm1 = request.session['usernametm1']
        if request.session.has_key('usernametm2'):
            usernametm2 = request.session['usernametm2']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(
            designation_id=usernametm) .filter(fullname=usernametm1)
        
        des = designation.objects.get(designation='manager')
        des1 = designation.objects.get(designation='trainingmanager')
        # cut = user_registration.objects.get(designation_id=usernametm2)
        ree = user_registration.objects.get(designation_id=des.id)
        # ree1 = user_registration.objects.get(designation_id=usernametm)
    
        if request.method == 'POST':
          
            vars = reported_issue()
            # print(vars.reply)
            vars.issue = request.POST['issue']
            
            vars.issuestatus = 0
            vars.reporter_id = usernametm2
            vars.designation_id = des1.id
            vars.reported_to = ree
            vars.reported_date = datetime.now()
            vars.save()
            return redirect('reportedissue')
    
        return render(request, 'reportissue.html', {'mem': mem})
    else:
        return redirect('/')
def reportedissuesub(request):
    if 'usernametm2' in request.session:
        if request.session.has_key('usernametm'):
            usernametm = request.session['usernametm']
        if request.session.has_key('usernametm1'):
            usernametm1 = request.session['usernametm1']
        if request.session.has_key('usernametm2'):
            usernametm2 = request.session['usernametm2']
        else:
            return redirect('/')
    
        mem = user_registration.objects.filter(
            designation_id=usernametm) .filter(fullname=usernametm1)
     
        cut = reported_issue.objects.filter(reporter=usernametm2).order_by('-id')
        context = {'cut': cut, 'vars': vars, 'mem': mem}
        return render(request,'reportedissuesub.html', context)

    else:
        return redirect('/')
def Applyleave(request):
    if 'usernametm2' in request.session:
        if request.session.has_key('usernametm'):
            usernametm = request.session['usernametm']
        if request.session.has_key('usernametm1'):
            usernametm1 = request.session['usernametm1']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(
            designation_id=usernametm) .filter(fullname=usernametm1)
        return render(request, 'Applyleave.html', {'mem': mem})
    else:
        return redirect('/')
def trainers_leave(request):
    if 'usernametm2' in request.session:
        if request.session.has_key('usernametm'):
            usernametm = request.session['usernametm']
        if request.session.has_key('usernametm1'):
            usernametm1 = request.session['usernametm1']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(
            designation_id=usernametm) .filter(fullname=usernametm1)
        return render(request, 'trainers_leave.html', {'mem': mem})
    else:
        return redirect('/')
def trainees_leave(request):
    if 'usernametm2' in request.session:
        if request.session.has_key('usernametm'):
            usernametm = request.session['usernametm']
        if request.session.has_key('usernametm1'):
            usernametm1 = request.session['usernametm1']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(
            designation_id=usernametm) .filter(fullname=usernametm1)
        return render(request, 'trainees_leave.html', {'mem': mem})
    else:
        return redirect('/')
def trainees_leavestatus(request):
    if 'usernametm2' in request.session:
        if request.session.has_key('usernametm'):
            usernametm = request.session['usernametm']
        if request.session.has_key('usernametm1'):
            usernametm1 = request.session['usernametm1']
        if request.session.has_key('usernametm2'):
            usernametm2 = request.session['usernametm2']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(
            designation_id=usernametm) .filter(fullname=usernametm1)
    
        des = designation.objects.get(designation='trainee')
        n = leave.objects.filter(designation_id=des.id).order_by('-id')
        return render(request, 'trainees_leavestatus.html', {'mem': mem,'n':n})
    else:
        return redirect('/')
def trainer_leavestatus(request):
    if 'usernametm2' in request.session:
        if request.session.has_key('usernametm'):
            usernametm = request.session['usernametm']
        if request.session.has_key('usernametm1'):
            usernametm1 = request.session['usernametm1']
        if request.session.has_key('usernametm2'):
            usernametm2 = request.session['usernametm2']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(
            designation_id=usernametm) .filter(fullname=usernametm1)
    
        des = designation.objects.get(designation='trainer')
        n = leave.objects.filter(designation_id=des.id).order_by('-id')
        
    
        return render(request, 'trainer_leavestatus.html', {'mem': mem ,'n': n})
    else:
        return redirect('/')
def Leave_rejected(request):
    if 'usernametm2' in request.session:
        if request.session.has_key('usernametm'):
            usernametm = request.session['usernametm']
        if request.session.has_key('usernametm1'):
            usernametm1 = request.session['usernametm1']
        else:
            return redirect('/')
    
        mem = user_registration.objects.filter(
            designation_id=usernametm) .filter(fullname=usernametm1)
        id = request.GET.get('id')
        if request.method == 'POST':
            vars = leave.objects.get(id=id)       
            
            vars.leave_rejected_reason = request.POST['review']
            print(vars.leave_rejected_reason)
            vars.leaveapprovedstatus = 2
           
            
            vars.save()
        return redirect('trainers_leave')
    else:
        return redirect('/')
def Trainee_Leave_rejected(request):
    if 'usernametm2' in request.session:
        if request.session.has_key('usernametm'):
            usernametm = request.session['usernametm']
        if request.session.has_key('usernametm1'):
            usernametm1 = request.session['usernametm1']
        else:
            return redirect('/')
    
        mem = user_registration.objects.filter(
            designation_id=usernametm) .filter(fullname=usernametm1)
        id = request.GET.get('id')
        if request.method == 'POST':
            vars = leave.objects.get(id=id)       
            
            vars.leave_rejected_reason = request.POST['review']
            print(vars.leave_rejected_reason)
            vars.leaveapprovedstatus = 2
           
            
            vars.save()
        return redirect('trainees_leave')
    else:
        return redirect('/')

def applyleavesub(request):
    if 'usernametm2' in request.session:
        if request.session.has_key('usernametm'):
            usernametm = request.session['usernametm']
        if request.session.has_key('usernametm1'):
            usernametm1 = request.session['usernametm1']
        if request.session.has_key('usernametm2'):
            usernametm2 = request.session['usernametm2']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(
            designation_id=usernametm) .filter(fullname=usernametm1)
        des = designation.objects.get(designation='manager')
        des1 = designation.objects.get(designation='trainingmanager')
        cut = user_registration.objects.get(id=usernametm2)
        ree = user_registration.objects.get(designation_id=des.id)
        ree1 = user_registration.objects.get(designation_id=usernametm)
        if request.method == 'POST':
            vars = leave()
            vars.from_date = request.POST['from']
            vars.to_date = request.POST['to']
            vars.reason = request.POST['reason']
            vars.leave_status = request.POST['haful']
            vars.leaveapprovedstatus = 0
            vars.user = cut
            vars.designation_id = des1.id


            start = datetime.strptime(vars.from_date, '%Y-%m-%d').date() 
            end = datetime.strptime(vars.to_date, '%Y-%m-%d').date()

            diff = (end  - start).days
            
            cnt =  Event.objects.filter(start_time__range=(start,end)).count()
            
            if diff == 0:
                vars.days = 1
            else:
                vars.days = diff - cnt
     
            vars.save()
            return redirect('Applyleave')
    
    
        return render(request,'applyleavesub.html', {'mem': mem})
    else:
        return redirect('/')

def Requestedleave(request):
    if 'usernametm2' in request.session:
        if request.session.has_key('usernametm'):
            usernametm = request.session['usernametm']
        if request.session.has_key('usernametm1'):
            usernametm1 = request.session['usernametm1']
        if request.session.has_key('usernametm2'):
            usernametm2 = request.session['usernametm2']
        else:
            return redirect('/')
    
        mem = user_registration.objects.filter(
            designation_id=usernametm) .filter(fullname=usernametm1)
        des = designation.objects.get(designation='trainingmanager')
        print(des.id)
        cut = leave.objects.filter(designation_id=des.id).order_by('-id')
        context = {'cut': cut, 'vars': vars, 'mem': mem}
        return render(request,'Requestedleave.html', context)

    else:
        return redirect('/')
def trainers_leavelist(request):
    if 'usernametm2' in request.session:
        if request.session.has_key('usernametm'):
            usernametm = request.session['usernametm']
        if request.session.has_key('usernametm1'):
            usernametm1 = request.session['usernametm1']
        if request.session.has_key('usernametm2'):
            usernametm2 = request.session['usernametm2']
        else:
            return redirect('/')
        
    
        mem = user_registration.objects.filter(designation_id=usernametm) .filter(fullname=usernametm1)
        des = designation.objects.get(designation='trainer')
        cut = leave.objects.filter(designation_id=des.id).filter(leaveapprovedstatus=0).order_by('-id')
        
        
        
        context = {'cut': cut, 'vars': vars, 'mem': mem}
        return render(request,'trainers_leavelist.html', context)
    else:
        return redirect('/')

       
def approvedstatus(request,id):
    a=leave.objects.get(id=id)
    a.leaveapprovedstatus=1
    a.save()
    return redirect('trainers_leave')

def approvedstatus_trainee(request,id):
    a=leave.objects.get(id=id)
    a.leaveapprovedstatus=1
    a.save()
    return redirect('trainees_leave')



def trainees_leavelist(request):
    if 'usernametm2' in request.session:
        if request.session.has_key('usernametm'):
            usernametm = request.session['usernametm']
        if request.session.has_key('usernametm1'):
            usernametm1 = request.session['usernametm1']
        if request.session.has_key('usernametm2'):
            usernametm2 = request.session['usernametm2']
        else:
            return redirect('/')
    
        mem = user_registration.objects.filter(
            designation_id=usernametm) .filter(fullname=usernametm1)
        # .objects.filter(reported_to_id=usernametm2)
        des = designation.objects.get(designation='trainee')
       
        cut = leave.objects.filter(designation_id=des.id).filter(leaveapprovedstatus=0).order_by('-id')
        context = {'cut': cut, 'vars': vars, 'mem': mem}
        return render(request,'trainees_leavelist.html', context)

    else:
        return redirect('/')
def trainer(request):
    if 'usernametm2' in request.session:
        
        if request.session.has_key('usernametm2'):
            usernametm2 = request.session['usernametm2']
        
        mem = user_registration.objects.filter(
            id=usernametm2)
        des = designation.objects.get(designation='trainer')
        vars = user_registration.objects.filter(designation=des.id).all().order_by('-id')
        context = {'vars': vars, 'mem': mem}
        return render(request,'trainer.html', context)
    else:
        return redirect('/')

def team1(request, id):
    if 'usernametm2' in request.session:
        if request.session.has_key('usernametm'):
            usernametm = request.session['usernametm']
        if request.session.has_key('usernametm1'):
            usernametm1 = request.session['usernametm1']
        else:
            return redirect('/')
    
        mem = user_registration.objects.filter(
            designation_id=usernametm) .filter(fullname=usernametm1)
        d = user_registration.objects.get(id=id)
        return render(request, 'Trainer_Team_manager.html', {'d': d, 'mem': mem})

    return redirect('/')
    
    
def current(request, id):
    if 'usernametm2' in request.session:
        if request.session.has_key('usernametm'):
            usernametm = request.session['usernametm']
        if request.session.has_key('usernametm1'):
            usernametm1 = request.session['usernametm1']
        else:
            return redirect('/')

        mem = user_registration.objects.filter(
            designation_id=usernametm) .filter(fullname=usernametm1)
        d = user_registration.objects.get(id=id)
        tm = create_team.objects.filter(trainer_id=d.id).filter(team_status=0).order_by('-id')
        des = designation.objects.get(designation='trainer')
        cut = user_registration.objects.filter(designation_id=des.id)
        vars = user_registration.objects.filter(
            designation_id=usernametm).filter(fullname=usernametm1)
        return render(request, 'Trainer_Current_Team.html', {'vars': vars, 'des': des, 'tm': tm, 'cut': cut, 'mem': mem})
    else:
        return redirect('/')

def task(request, id):
    if 'usernametm2' in request.session:
        
        if request.session.has_key('usernametm2'):
            usernametm2 = request.session['usernametm2']
        
        mem = user_registration.objects.filter(id=usernametm2)
        d = create_team.objects.get(id=id)
        return render(request,'Trainer_Current_task.html',{'d': d, 'mem': mem})
    else:
        return redirect('/')

def Trainer_Current_Assigned(request, id):
    if 'usernametm2' in request.session:
        
        if request.session.has_key('usernametm2'):
            usernametm2 = request.session['usernametm2']
      
    
        mem = user_registration.objects.filter(id=usernametm2)
        d = create_team.objects.get(id=id)
        vars = topic.objects.filter(team_id=d.id).order_by('-id')
        return render(request, 'Trainer_Current_Assigned.html', {'vars': vars, 'mem': mem})

    else:
        return redirect('/')
def Trainer_Currenttrainee(request, id):
    if 'usernametm2' in request.session:
        if request.session.has_key('usernametm'):
            usernametm = request.session['usernametm']
        if request.session.has_key('usernametm1'):
            usernametm1 = request.session['usernametm1']
        else:
            return redirect('/')
    
        mem = user_registration.objects.filter(
            designation_id=usernametm) .filter(fullname=usernametm1)
        d = create_team.objects.get(id=id)
        des = designation.objects.get(designation='trainee')
        vars = user_registration.objects.filter(team=d.id,designation=des.id).order_by('-id')
        
        return render(request, 'Trainer_Currenttrainees.html', {'vars': vars, 'mem': mem})
    else:
        return redirect('/')

def Empdetails(request, id):
    if 'usernametm2' in request.session:
        if request.session.has_key('usernametm'):
            usernametm = request.session['usernametm']
        if request.session.has_key('usernametm1'):
            usernametm1 = request.session['usernametm1']
        else:
            return redirect('/')

        mem = user_registration.objects.filter(
            designation_id=usernametm) .filter(fullname=usernametm1)
        vars = user_registration.objects.get(id=id)
        tre = create_team.objects.get(id=vars.team.id)
        k=user_registration.objects.get(id=tre.trainer_id)
        labels = []

        data = []
        queryset = user_registration.objects.filter(id=vars.id)
        for i in queryset:
            labels = [i.workperformance, i.attitude, i.creativity]

            data = [i.workperformance, i.attitude, i.creativity]

        return render(request, 'Trainer_Current_Empdetails.html', {'vars': vars, 'tre': tre, 'mem': mem, 'labels': labels, 'data': data,'k':k})
    else:
        return redirect('/')

def Trainer_Previousattendance(request,id):
    if 'usernametm2' in request.session:
        if request.session.has_key('usernametm'):
            usernametm = request.session['usernametm']
        if request.session.has_key('usernametm1'):
            usernametm1 = request.session['usernametm1']
        else:
            return redirect('/')
    
        mem = user_registration.objects.filter(
            designation_id=usernametm) .filter(fullname=usernametm1)
    
        vars = user_registration.objects.get(id=id)
    
        return render(request, 'Trainer_Previousattendance.html', {'vars':vars,'mem': mem})
    else:
        return redirect('/')
def List(request,id):
    if 'usernametm2' in request.session:
        if request.session.has_key('usernametm'):
            usernametm = request.session['usernametm']
        if request.session.has_key('usernametm1'):
            usernametm1 = request.session['usernametm1']
        else:
            return redirect('/')
    
        mem = user_registration.objects.filter(
            designation_id=usernametm) .filter(fullname=usernametm1)
    
        vars = user_registration.objects.get(id=id)
        if request.method == 'POST':
            std = request.POST['startdate']
            edd = request.POST['enddate']
            user=vars
            atten = attendance.objects.filter(date__gte=std,date__lte=edd,user_id=user)
            
        return render(request,'Trainer_Current_AttendanceList.html',{'mem':mem,'vars': vars, 'atten':atten})

    else:
        return redirect('/')
def task1(request, id):
    if 'usernametm2' in request.session:
        if request.session.has_key('usernametm'):
            usernametm = request.session['usernametm']
        if request.session.has_key('usernametm1'):
            usernametm1 = request.session['usernametm1']
        else:
            return redirect('/')
    
        mem = user_registration.objects.filter(
            designation_id=usernametm) .filter(fullname=usernametm1)
        d = user_registration.objects.get(id=id)
        tsk = trainer_task.objects.filter(user_id=d.id).order_by('-id')
    
        return render(request, 'Trainer_Current_task1.html', {'tsk': tsk, 'mem': mem})

    else:
        return redirect('/')
def tdetails(request, id):
    if 'usernametm2' in request.session:
        if request.session.has_key('usernametm'):
            usernametm = request.session['usernametm']
        if request.session.has_key('usernametm1'):
            usernametm1 = request.session['usernametm1']
        else:
            return redirect('/')
    
        mem = user_registration.objects.filter(
            designation_id=usernametm) .filter(fullname=usernametm1)
        d = user_registration.objects.get(id=id)
        tsk = trainer_task.objects.get(id=d.id)
        return render(request, 'Trainer_Current_Taskdetails.html', {'tsk': tsk, 'mem': mem})
    else:
        return redirect('/')

def Previous(request, id):
    if 'usernametm2' in request.session:
        if request.session.has_key('usernametm'):
            usernametm = request.session['usernametm']
        if request.session.has_key('usernametm1'):
            usernametm1 = request.session['usernametm1']
        else:
            return redirect('/')

        mem = user_registration.objects.filter(
            designation_id=usernametm) .filter(fullname=usernametm1)
        d = user_registration.objects.get(id=id)
        tm = create_team.objects.filter(trainer_id=d.id).filter(team_status=1)
        des = designation.objects.get(designation='trainer')
        cut = user_registration.objects.filter(designation_id=des.id)
        vars = user_registration.objects.filter(
            designation_id=usernametm).filter(fullname=usernametm1)
        return render(request, 'Trainer_Previous_Team.html', {'vars': vars, 'des': des, 'tm': tm, 'cut': cut, 'mem': mem})
    else:
        return redirect('/')

def Previous_Task(request, id):
    if 'usernametm2' in request.session:
        if request.session.has_key('usernametm'):
            usernametm = request.session['usernametm']
        if request.session.has_key('usernametm1'):
            usernametm1 = request.session['usernametm1']
        else:
            return redirect('/')
    
        mem = user_registration.objects.filter(
            designation_id=usernametm) .filter(fullname=usernametm1)
        d = create_team.objects.get(id=id)
        return render(request, 'Trainer_Previous_Task.html', {'d': d, 'mem': mem})

    return redirect('/')
def Previous_Assigned(request, id):
    if 'usernametm2' in request.session:
        if request.session.has_key('usernametm'):
            usernametm = request.session['usernametm']
        if request.session.has_key('usernametm1'):
            usernametm1 = request.session['usernametm1']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(
            designation_id=usernametm) .filter(fullname=usernametm1)
        d = create_team.objects.get(id=id)
        vars = trainer_task.objects. filter(id=d.id)
        return render(request, 'Trainer_Previous_Assigned.html', {'vars': vars, 'mem': mem})

    else:
        return redirect('/')
def Trainer_Previous_Trainees(request, id):
    if 'usernametm2' in request.session:
        if request.session.has_key('usernametm'):
            usernametm = request.session['usernametm']
        if request.session.has_key('usernametm1'):
            usernametm1 = request.session['usernametm1']
        else:
            usernametm1 = "dummy"
    
        mem = user_registration.objects.filter(
            designation_id=usernametm) .filter(fullname=usernametm1)
        d = create_team.objects.get(id=id)
        des = designation.objects.get(designation='trainee')
        vars = user_registration.objects.filter(
            team=d.id).filter(designation=des.id).order_by('-id')
        vars1 = previousTeam.objects.filter(teamname=id)
        return render(request, 'Trainer_Previous_Trainees_manager.html', {'vars': vars, 'mem': mem,'vars1':vars1})

    else:
        return redirect('/')
def PEmpdetails(request, id):
    if 'usernametm2' in request.session:
        if request.session.has_key('usernametm'):
            usernametm = request.session['usernametm']
        if request.session.has_key('usernametm1'):
            usernametm1 = request.session['usernametm1']
        else:
            return redirect('/')

        mem = user_registration.objects.filter(
            designation_id=usernametm) .filter(fullname=usernametm1)
        vars = user_registration.objects.get(id=id)
        tre = create_team.objects.get(id=vars.team.id)
        k=user_registration.objects.get(id=tre.trainer_id)
        labels = []

        data = []
        queryset = user_registration.objects.filter(id=vars.id)
        for i in queryset:
            labels = [i.workperformance, i.attitude, i.creativity]

            data = [i.workperformance, i.attitude, i.creativity]

        return render(request, 'Trainer_Previous_Empdetails.html', {'vars': vars, 'tre': tre, 'mem': mem, 'labels': labels, 'data': data,'k':k})
    else:
        return redirect('/')

def PAttendance(request,id):
    if 'usernametm2' in request.session:
        if request.session.has_key('usernametm'):
            usernametm = request.session['usernametm']
        if request.session.has_key('usernametm1'):
            usernametm1 = request.session['usernametm1']
        else:
            return redirect('/')
    
        mem = user_registration.objects.filter(
            designation_id=usernametm) .filter(fullname=usernametm1)
        vars = user_registration.objects.get(id=id)
    
        return render(request, 'Trainer_Previous_Attendance.html',{'mem':mem, 'vars':vars})
    else:
        return redirect('/')
def PList(request,id):
    if 'usernametm2' in request.session:
        if request.session.has_key('usernametm'):
            usernametm = request.session['usernametm']
        if request.session.has_key('usernametm1'):
            usernametm1 = request.session['usernametm1']
        else:
            return redirect('/')
    
        mem = user_registration.objects.filter(
            designation_id=usernametm) .filter(fullname=usernametm1)
    
        vars = user_registration.objects.get(id=id)
        if request.method == 'POST':
            std = request.POST['startdate']
            edd = request.POST['enddate']
            user=vars
            atten = attendance.objects.filter(date__gte=std,date__lte=edd,user_id=user).order_by('-id')
        return render(request, 'Trainer_Previous_Attendance_List.html',{'mem':mem,'vars': vars, 'atten':atten})
    else:
        return redirect('/')
def Ptask1(request, id):
    if 'usernametm2' in request.session:
        if request.session.has_key('usernametm'):
            usernametm = request.session['usernametm']
        if request.session.has_key('usernametm1'):
            usernametm1 = request.session['usernametm1']
        else:
            return redirect('/')
    
        mem = user_registration.objects.filter(
            designation_id=usernametm) .filter(fullname=usernametm1)
        d = user_registration.objects.get(id=id)
        tsk = trainer_task.objects.filter(user=d.id)
        return render(request, 'Trainer_Previous_Task1.html', {'tsk': tsk, 'mem': mem})
    else:
        return redirect('/')

def Ptdetails(request, id):
    if 'usernametm2' in request.session:
        if request.session.has_key('usernametm'):
            usernametm = request.session['usernametm']
        if request.session.has_key('usernametm1'):
            usernametm1 = request.session['usernametm1']
        else:
            return redirect('/')
    
        mem = user_registration.objects.filter(
            designation_id=usernametm) .filter(fullname=usernametm1)
        tsk = trainer_task.objects.get(id=id)
        return render(request, 'Trainer_Previous_Taskdetails.html', {'tsk': tsk, 'mem': mem})
    else:
        return redirect('/')
        
        
def traineedetails(request,id):
    if 'usernametm2' in request.session:
        if request.session.has_key('usernametm'):
            usernametm = request.session['usernametm']
        if request.session.has_key('usernametm1'):
            usernametm1 = request.session['usernametm1']
        else:
            return redirect('/')

        mem = user_registration.objects.filter(
            designation_id=usernametm) .filter(fullname=usernametm1)

        vars = user_registration.objects.get(id=id)
        tre = create_team.objects.get(id=vars.team.id)
        k=user_registration.objects.get(id=tre.trainer_id)
        labels = []
        data = []
        queryset = user_registration.objects.filter(id=vars.id)
        for i in queryset:
            labels = [i.workperformance, i.attitude, i.creativity]

            data = [i.workperformance, i.attitude, i.creativity]
        return render(request, 'traineedetails.html', {'mem': mem, 'vars': vars, 'tre': tre, 'labels': labels, 'data': data,'k':k})
    else:
        return redirect('/')
        
        
        
        
def statusTable(request,id):
    if 'usernametm2' in request.session:
        if request.session.has_key('usernametm'):
            usernametm = request.session['usernametm']
        if request.session.has_key('usernametm1'):
            usernametm1 = request.session['usernametm1']
        else:
            return redirect('/')
    
        mem = user_registration.objects.filter(
            designation_id=usernametm) .filter(fullname=usernametm1)
    
        vars= user_registration.objects.get(id=id)
        if request.method == 'POST':
            std = request.POST['startdate']
            edd = request.POST['enddate']
            user=vars
            atten = attendance.objects.filter(date__gte=std,date__lte=edd,user_id=user)
        
        return render(request,'trainee_statustable.html',{'mem':mem,'vars':vars, 'atten':atten})
    else:
        return redirect('/')
########################################################   trainers      ###############################################


def trainer_dashboard(request):
    if 'usernametrnr2' in request.session:

        if request.session.has_key('usernametrnr2'):
            usernametrnr2 = request.session['usernametrnr2']

        z = user_registration.objects.filter(id=usernametrnr2)
        des = designation.objects.get(designation='trainee')
        le = leave.objects.filter(
            designation_id=des.id, leaveapprovedstatus=0).all()

        labels = []
        data = []
        queryset = user_registration.objects.filter(id=usernametrnr2)
        for i in queryset:
            labels = [i.workperformance, i.attitude, i.creativity]

            data = [i.workperformance, i.attitude, i.creativity]
        return render(request, 'trainer_dashboard.html', {'z': z, 'labels': labels, 'data': data, 'le': le})
    else:
        return redirect('/')


def trainer_applyleave(request):
    if 'usernametrnr2' in request.session:
        
        if request.session.has_key('usernametrnr2'):
            usernametrnr2 = request.session['usernametrnr2']
        
        z = user_registration.objects.filter(id=usernametrnr2) 
        return render(request, 'trainer_applyleave.html', {'z': z})
    else:
        return redirect('/')

def trainer_applyleave_form(request):
    if request.session.has_key('usernametrnr2'):
            usernametrnr2 = request.session['usernametrnr2']
    z = user_registration.objects.filter(id=usernametrnr2)
    le = user_registration.objects.get(id=usernametrnr2)
    des1 = designation.objects.get(designation='trainer')
    
    if request.method == 'POST':
        mem = leave()
        mem.from_date = request.POST['from']
        mem.to_date = request.POST['to']
        mem.leave_status = request.POST['haful']
        mem.reason = request.POST['reason']
        mem.user = le
        mem.designation_id = des1.id
        mem.leaveapprovedstatus=0       

        start = datetime.strptime(mem.from_date, '%Y-%m-%d').date() 
        end = datetime.strptime(mem.to_date, '%Y-%m-%d').date()

        diff = (end  - start).days
        
        cnt =  Event.objects.filter(start_time__range=(start,end)).count()
        
        if diff == 0:
            mem.days = 1
        else:
            mem.days = diff - cnt
        mem.save()
        return render(request, 'trainer_applyleave.html', {'z': z})
    return render(request, 'trainer_applyleave_form.html', {'z': z})
    

def trainer_traineesleave_table(request):
    if 'usernametrnr2' in request.session:
        
            
        if request.session.has_key('usernametrnr2'):
            usernametrnr2 = request.session['usernametrnr2']
       
    
        z = user_registration.objects.filter(id=usernametrnr2)
        des = designation.objects.get(designation='trainee')
        tm = leave.objects.filter(designation_id=des.id) .all().order_by('-id')
        return render(request, 'trainer_traineesleave_table.html', {'tm': tm, 'z': z})
    else:
        return redirect('/')

def trainer_reportissue(request):
    if 'usernametrnr2' in request.session:
        
        if request.session.has_key('usernametrnr2'):
            usernametrnr2 = request.session['usernametrnr2']
        
        z = user_registration.objects.filter(id=usernametrnr2)
    
        return render(request, 'trainer_reportissue.html', {'z': z})
    else:
        return redirect('/')


def trainer_reportissue_form(request):
    if 'usernametrnr2' in request.session:
        
        if request.session.has_key('usernametrnr2'):
            usernametrnr2 = request.session['usernametrnr2']
        
        z = user_registration.objects.filter(id=usernametrnr2)
    
        mem = reported_issue()
        des = designation.objects.get(designation='trainingmanager')
        cut = user_registration.objects.get(designation_id=des.id)
        mem1 = user_registration.objects.get(id=usernametrnr2)
        des1 = designation.objects.get(designation='trainer')
        print(mem1)
        if request.method == "POST":
            mem.issue = request.POST['issues']
            mem.reported_date = datetime.now()
            mem.reported_to = cut
            mem.reporter = mem1
            mem.designation_id = des1.id
            mem.issuestatus =0
            mem.save()
            return render(request, 'trainer_reportissue.html', {'z': z})
        return render(request, 'trainer_reportissue_form.html', {'mem': mem, 'z': z})
    else:
        return redirect('/')

def trainer_reportedissue_table(request):
    if 'usernametrnr2' in request.session:
        
        if request.session.has_key('usernametrnr2'):
            usernametrnr2 = request.session['usernametrnr2']
       
        z = user_registration.objects.filter(id=usernametrnr2)
    
        des = designation.objects.get(designation='trainee')
        print(des)
        cut = reported_issue.objects.filter(reported_to_id=usernametrnr2).filter(
            designation_id=des.id).filter(issuestatus=0).order_by('-id')
    
        return render(request, 'trainer_reportedissue_table.html', {'cut': cut, 'vars': vars,  'z': z})
    else:
        return redirect('/')

def savereplaytnee(request, id):
    if request.method == 'POST':
        vars = reported_issue.objects.get(id=id)
        print(vars.reply)
        vars.reply = request.POST['reply']
        print('hello')
        vars.issuestatus = 1
        vars.save()
    return redirect('trainer_reportedissue_table')


def trainer_myreportissue_table(request):
    if 'usernametrnr2' in request.session:
       
        if request.session.has_key('usernametrnr2'):
            usernametrnr2 = request.session['usernametrnr2']
        
        z = user_registration.objects.filter(id=usernametrnr2)
        rm = reported_issue.objects.filter(reporter_id=usernametrnr2).order_by('-id')
    
        return render(request, 'trainer_myreportissue_table.html', {'rm': rm, 'z': z})


    else:
        return redirect('/')
def trainer_topic(request):
    if 'usernametrnr2' in request.session:
        if request.session.has_key('usernametrnr2'):
            usernametrnr2 = request.session['usernametrnr2']
        else:
            return redirect('/')
    
        z = user_registration.objects.filter(id=usernametrnr2)
        return render(request, 'trainer_topic.html', {'z': z})
    else:
        return redirect('/')

def trainer_addtopic(request):
    if 'usernametrnr2' in request.session:

        if request.session.has_key('usernametrnr2'):
            usernametrnr2 = request.session['usernametrnr2']

        z = user_registration.objects.filter(id=usernametrnr2)
        uname = user_registration.objects.get(id=usernametrnr2)
        crt = create_team.objects.filter(trainer_id=uname.id,team_status=0)
        mem = topic()
        if request.method == 'POST':
            # mem = user_registration()
            mem.team_id = request.POST['select']
            mem.topic = request.POST['topic']
            mem.startdate = request.POST['start']
            mem.enddate = request.POST['end']
            mem.topic_status = 0
            mem.trainer_id = uname.id
            mem.save()
            return render(request, 'trainer_addtopic.html', {'mem': mem, 'crt': crt, 'z': z})
        return render(request, 'trainer_addtopic.html', {'mem': mem, 'crt': crt, 'z': z})
    else:
        return redirect('/')

def trainer_viewtopic(request):
    if 'usernametrnr2' in request.session:
        if request.session.has_key('usernametrnr2'):
            usernametrnr2 = request.session['usernametrnr2']
            
        if request.method=="POST":
            uid = request.POST.get('sts')
            tem_id = topic.objects.get(id=uid)
            tem_id.topic_status = 1
            tem_id.save()
            return redirect('trainer_viewtopic')
        else:      
            z = user_registration.objects.filter(id=usernametrnr2)
            mem = topic.objects.filter(trainer_id=usernametrnr2).order_by('-id')
            return render(request, 'trainer_viewtopic.html', {'mem': mem, 'z': z})
    else:
        return redirect('/')
def trainer_attendance(request):
    if 'usernametrnr2' in request.session:
       
        if request.session.has_key('usernametrnr2'):
            usernametrnr2 = request.session['usernametrnr2']
       
        z = user_registration.objects.filter(id=usernametrnr2)
        return render(request, 'trainer_attendance.html',{'z':z})
    else:
        return redirect('/')

def trainer_attendance_trainees(request):
    if 'usernametrnr2' in request.session:
        
        if request.session.has_key('usernametrnr2'):
            usernametrnr2 = request.session['usernametrnr2']
       
        z = user_registration.objects.filter(id=usernametrnr2)
        return render(request, 'trainer_attendance_trainees.html',{'z':z})
    else:
        return redirect('/')

def trainer_attendance_trainer(request):
    if 'usernametrnr2' in request.session:
        
        if request.session.has_key('usernametrnr2'):
            usernametrnr2 = request.session['usernametrnr2']
        z = user_registration.objects.filter(id=usernametrnr2)
        return render(request, 'trainer_attendance_trainer.html',{'z':z})
    else:
        return redirect('/')

def trainer_attendance_trainer_viewattendance(request):
    if 'usernametrnr2' in request.session:
        
        if request.session.has_key('usernametrnr2'):
            usernametrnr2 = request.session['usernametrnr2']
       
        z = user_registration.objects.filter(id=usernametrnr2)
        return render(request, 'trainer_attendance_trainer_viewattendance.html',{'z':z})
    else:
        return redirect('/')

def trainer_attendance_trainer_viewattendancelist(request):
    if 'usernametrnr2' in request.session:
       
        if request.session.has_key('usernametrnr2'):
            usernametrnr2 = request.session['usernametrnr2']
       
        
        z = user_registration.objects.filter(id=usernametrnr2)
        if request.method == 'POST':
            std = request.POST['startdate']
            edd = request.POST['enddate']
            
            atten = attendance.objects.filter(date__gte=std,date__lte=edd,user_id=usernametrnr2).order_by('-id')
        return render(request, 'trainer_attendance_trainer_viewattendancelist.html',{'z':z,'atten':atten})
    else:
        return redirect('/')



def trainer_team(request):
    if 'usernametrnr2' in request.session:
       
        if request.session.has_key('usernametrnr2'):
            usernametrnr2 = request.session['usernametrnr2']
       
        z = user_registration.objects.filter(id=usernametrnr2)
        return render(request, 'trainer_team.html', {'z': z})
    else:
        return redirect('/')

def trainer_currentteam(request):
    if 'usernametrnr2' in request.session:
        if request.session.has_key('usernametrnr1'):
            usernametrnr1 = request.session['usernametrnr1']
        if request.session.has_key('usernametrnr2'):
            usernametrnr2 = request.session['usernametrnr2']
        else:
            return redirect('/')

        z = user_registration.objects.filter(
            fullname=usernametrnr1) .filter(id=usernametrnr2)

        tm = create_team.objects.filter(trainer_id=usernametrnr2).filter(
            team_status=0).order_by('-id')
        return render(request, 'trainer_current_team_list.html', {'tm': tm, 'z': z})
    else:
        return redirect('/')



def attenperform(request):
    if request.method == 'POST':
        id = request.GET.get('id')
        abc = create_team.objects.get(id=id)
        abc.progress = request.POST['sele']
        abc.save()
        return redirect('trainer_currentteam')
    else:
         return render(request,'trainer_current_team_list.html')


def trainer_currenttrainees(request, id):
    if 'usernametrnr2' in request.session:
        
        if request.session.has_key('usernametrnr2'):
            usernametrnr2 = request.session['usernametrnr2']
       
        z = user_registration.objects.filter(id=usernametrnr2)
    
        d = create_team.objects.get(id=id)
        des = designation.objects.get(designation='trainee')
        mem = user_registration.objects.filter(
            designation_id=des.id).filter(team_id=d).order_by('-id')
        return render(request, 'trainer_current_trainees_list.html', {'mem': mem, 'z': z})
    else:
        return redirect('/')

def trainer_currenttraineesdetails(request, id):
    if 'usernametrnr2' in request.session:

        if request.session.has_key('usernametrnr2'):
            usernametrnr2 = request.session['usernametrnr2']

        z = user_registration.objects.filter(id=usernametrnr2)
        mem = user_registration.objects.get(id=id)
        tre = create_team.objects.get(id=mem.team.id)
        k=user_registration.objects.get(id=tre.trainer_id)
        labels = []
        data = []
        queryset = user_registration.objects.filter(id=mem.id)
        for i in queryset:
            labels = [i.workperformance, i.attitude, i.creativity]

            data = [i.workperformance, i.attitude, i.creativity]
        return render(request, 'trainer_current_tainees_details.html', {'mem': mem, 'tre': tre, 'z': z, 'labels': labels, 'data': data, 'k':k})
    else:
        return redirect('/')


def trainer_currentattentable(request, id):
    if 'usernametrnr2' in request.session:
   
        if request.session.has_key('usernametrnr2'):
            usernametrnr2 = request.session['usernametrnr2']
       
        z = user_registration.objects.filter(id=usernametrnr2)
        mem = user_registration.objects.get(id=id)
        if request.method == 'POST':
            std = request.POST['startdate']
            edd = request.POST['enddate']
            user=mem
            atten = attendance.objects.filter(date__gte=std,date__lte=edd,user_id=user).order_by('-id')
        return render(request, 'trainer_current_atten_table.html', {'mem': mem, 'z': z,'atten':atten})

    else:
        return render('/')
def trainer_currentperform(request, id):
    if 'usernametrnr2' in request.session:
   
        
        if request.session.has_key('usernametrnr2'):
            usernametrnr2 = request.session['usernametrnr2']
        
        z = user_registration.objects.filter(id=usernametrnr2)
        mem = user_registration.objects.get(id=id)
        if request.method == 'POST':
            mem.attitude = request.POST['sele1']
            mem.creativity = request.POST['sele2']
            mem.workperformance = request.POST['sele3']
            mem.save()
            return render(request, 'trainer_current_perform.html', {'mem': mem, 'z': z})
        return render(request, 'trainer_current_perform.html', {'mem': mem, 'z': z})
    else:
        return render('/')
        
        


def trainer_currentattenadd(request, id):
    if 'usernametrnr2' in request.session:
        
        if request.session.has_key('usernametrnr2'):
            usernametrnr2 = request.session['usernametrnr2']
       
        z = user_registration.objects.filter(id=usernametrnr2)
        mem = user_registration.objects.get(id=id)
        atten = attendance()
        if request.method == 'POST':
            atten.date = request.POST['date']
            atten.user = mem
            atten.attendance_status = request.POST['pres']
            atten.save()
            return render(request, 'trainer_current_tainees_details.html', {'mem': mem, 'atten': atten, 'z': z})
        return render(request, 'trainer_current_atten_add.html', {'mem': mem, 'z': z})
    else:
        return redirect('/')

def trainer_previousteam(request):
    if 'usernametrnr2' in request.session:

        if request.session.has_key('usernametrnr1'):
            usernametrnr1 = request.session['usernametrnr1']
        if request.session.has_key('usernametrnr2'):
            usernametrnr2 = request.session['usernametrnr2']
        else:
            return redirect('/')

        z = user_registration.objects.filter(
            fullname=usernametrnr1) .filter(id=usernametrnr2)

        tm = create_team.objects.filter(trainer_id=usernametrnr2).filter(team_status=1).order_by('-id')
        return render(request, 'trainer_previous_team_list.html', {'tm': tm, 'z': z})
    else:
        return redirect('/')

def trainer_previoustrainees(request, id):
    if 'usernametrnr2' in request.session:
        
        if request.session.has_key('usernametrnr2'):
            usernametrnr2 = request.session['usernametrnr2']
        
        z = user_registration.objects.filter(id=usernametrnr2)
        d = create_team.objects.get(id=id)
        des = designation.objects.get(designation='trainee')
        mem = user_registration.objects.filter(designation_id=des.id).filter(team_id=d)
        memm=previousTeam.objects.filter(teamname=d)
        return render(request, 'trainer_previous_trainess_list.html', {'mem': mem, 'z': z,'memm': memm})

    else:
        return redirect('/')
        
def trainer_previoustraineesdetails(request, id):
    if 'usernametrnr2' in request.session:

        if request.session.has_key('usernametrnr2'):
            usernametrnr2 = request.session['usernametrnr2']
        z = user_registration.objects.filter(id=usernametrnr2)
        mem = user_registration.objects.get(id=id)

        tre = create_team.objects.get(id=mem.team.id)
        k=user_registration.objects.get(id=tre.trainer_id)
        labels = []
        data = []
        queryset = user_registration.objects.filter(id=mem.id)
        for i in queryset:
            labels = [i.workperformance, i.attitude, i.creativity]

            data = [i.workperformance, i.attitude, i.creativity]

        return render(request, 'trainer_previous_trainees_details.html', {'mem': mem, 'tre': tre, 'z': z, 'labels': labels, 'data': data,'k':k })

    else:
        return redirect('/')
        
        
        
def trainer_previousattentable(request, id):
    if 'usernametrnr2' in request.session:
        
        if  request.session.has_key('usernametrnr2'): 
             usernametrnr2 = request.session['usernametrnr2']
       
        z = user_registration.objects.filter(id=usernametrnr2)
    
    
        mem = user_registration.objects.get(id=id)
        att = attendance.objects.filter(user_id=mem.id).order_by('-id')
        return render(request, 'trainer_previous_atten_table.html', {'mem': mem, 'att': att, 'z': z})
    else:
        return redirect('/')

def trainer_previousperfomtable(request, id):
    if 'usernametrnr2' in request.session:
        
        if request.session.has_key('usernametrnr2'):
            usernametrnr2 = request.session['usernametrnr2']
      
        z = user_registration.objects.filter(id=usernametrnr2)
        num = user_registration.objects.get(id=id)
        return render(request, 'trainer_previous_performtable.html', {'num': num, 'z': z})
    else:
        return redirect('/')

def trainer_current_attendance(request, id):
    if 'usernametrnr2' in request.session:
        
        if request.session.has_key('usernametrnr2'):
            usernametrnr2 = request.session['usernametrnr2']
       
        z = user_registration.objects.filter(id=usernametrnr2)
        mem = user_registration.objects.get(id=id)
        return render(request, 'trainer_current_attendance.html', {'mem': mem, 'z': z})
    else:
        return redirect('/')


def trainer_Task(request):
    if 'usernametrnr2' in request.session:
        
        if request.session.has_key('usernametrnr2'):
            usernametrnr2 = request.session['usernametrnr2']
        
        z = user_registration.objects.filter(id=usernametrnr2)
        return render(request, 'trainer_task.html', {'z': z})
    else:
        return redirect('/')

def trainer_teamlistpage(request):
    if 'usernametrnr2' in request.session:

        if request.session.has_key('usernametrnr1'):
            usernametrnr1 = request.session['usernametrnr1']
        if request.session.has_key('usernametrnr2'):
            usernametrnr2 = request.session['usernametrnr2']
        else:
            return redirect('/')
        z = user_registration.objects.filter(
            fullname=usernametrnr1) .filter(id=usernametrnr2)

        tam = create_team.objects.filter(trainer_id=usernametrnr2, team_status=0).order_by('-id')
        des = designation.objects.get(designation='trainee')
        cut = user_registration.objects.filter(designation_id=des.id)

        return render(request, 'trainer_teamlist.html', {'tam': tam, 'cut': cut, 'z': z})
    else:
        return redirect('/')

def trainer_taskpage(request, id):
    if 'usernametrnr2' in request.session:
        
        if request.session.has_key('usernametrnr2'):
            usernametrnr2 = request.session['usernametrnr2']
       
        z = user_registration.objects.filter(id=usernametrnr2)
    
        d = create_team.objects.get(id=id)
    
        return render(request, 'trainer_taskfor.html', {'d': d, 'z': z})
    else:
        return redirect('/')

def trainer_givetask(request, id):
    if 'usernametrnr2' in request.session:
        
        if request.session.has_key('usernametrnr2'):
            usernametrnr2 = request.session['usernametrnr2']
       
        z = user_registration.objects.filter(id=usernametrnr2)
    
        d = create_team.objects.get(id=id)
        des = designation.objects.get(designation='trainee')
        var = user_registration.objects.filter(team_id=d).filter(designation_id=des.id)
        print(var)
    
        
        if request.method == 'POST':
            list= request.POST.get('trainee_list')
            name = request.POST.get('taskname')
            desc = request.POST.get('description')
            files= request.FILES['files']
            start= request.POST.get('start')
            end = request.POST.get('end')
            task_status = 0
            team_name_id = d.id
            
    
            vars = trainer_task(user_id=list,taskname=name,description=desc,files=files,startdate=start,
                    enddate=end,task_status=task_status, team_name_id=team_name_id)
            vars.save()
            return render(request, 'trainer_givetask.html', {'z': z, 'var': var})
        else:
            return render(request, 'trainer_givetask.html', {'z': z, 'var': var})

    else:
        return redirect('/')
def trainer_taskgivenpage(request, id):
    if 'usernametrnr2' in request.session:
       
        if request.session.has_key('usernametrnr2'):
            usernametrnr2 = request.session['usernametrnr2']
       
        z = user_registration.objects.filter(id=usernametrnr2)
    
        
        d = create_team.objects.get(id=id)
        c = trainer_task.objects.filter(team_name_id=d.id)
        des = designation.objects.get(designation='trainee')
        mem1 = user_registration.objects.filter(designation_id=des.id).filter(team_id=d).order_by('-id')
        mem = user_registration.objects.filter(designation_id=des.id).filter(team_id=d).values_list('id')
        tsk = trainer_task.objects.filter(team_name_id=d.id).filter(user_id__in=mem).order_by('-id')
        
        return render(request, 'trainer_taskgiven.html', {'mem': mem,'mem1': mem1, 'tsk': tsk, 'z': z})
    else:
        return redirect('/')

def trainer_taska(request):
    if 'usernametrnr2' in request.session:
        
        if request.session.has_key('usernametrnr2'):
            usernametrnr2 = request.session['usernametrnr2']
        
        z = user_registration.objects.filter(id=usernametrnr2)
        return render(request, 'trainer_taska.html', {'z': z})
    else:
        return redirect('/')

def trainer_task_completed_teamlist(request):
    if 'usernametrnr2' in request.session:
        
        if request.session.has_key('usernametrnr1'):
            usernametrnr1 = request.session['usernametrnr1']
        if request.session.has_key('usernametrnr2'):
            usernametrnr2 = request.session['usernametrnr2']
        else:
            return redirect('/')
        z = user_registration.objects.filter(fullname=usernametrnr1).filter(id=usernametrnr2)
    
        tam = create_team.objects.filter(trainer=usernametrnr1,team_status = 1).order_by('-id')
        des = designation.objects.get(designation='trainee')
        cut = user_registration.objects.filter(designation_id=des.id)
        
        return render(request, 'trainer_task_completed_teamlist.html',  {'z': z, 'cut':cut, 'tam':tam})
    else:
        return redirect('/')

def trainer_task_completed_team_tasklist(request, id):
    if 'usernametrnr2' in request.session:
        if request.session.has_key('usernametrnr'):
            usernametrnr = request.session['usernametrnr']
        if request.session.has_key('usernametrnr1'):
            usernametrnr1 = request.session['usernametrnr1']
        if request.session.has_key('usernametrnr2'):
            usernametrnr2 = request.session['usernametrnr2']
        else:
            return redirect('/')
        z = user_registration.objects.filter(designation_id=usernametrnr) .filter(
            fullname=usernametrnr1) .filter(id=usernametrnr2)
    
        d = create_team.objects.get(id=id)
    
        d=create_team.objects.get(id=id)
        tsk = trainer_task.objects.filter(team_name_id=d.id).order_by('-id')
        return render(request, 'trainer_task_completed_team_tasklist.html', {'z': z, 'tsk':tsk})
    else:
        return redirect('/')

def trainer_task_previous_teamlist(request):
    if 'usernametrnr2' in request.session:

        if request.session.has_key('usernametrnr1'):
            usernametrnr1 = request.session['usernametrnr1']
        if request.session.has_key('usernametrnr2'):
            usernametrnr2 = request.session['usernametrnr2']
        else:
            return redirect('/')
        z = user_registration.objects.filter(
            fullname=usernametrnr1) .filter(id=usernametrnr2)

        tam = create_team.objects.filter(trainer_id=usernametrnr2, team_status=1).order_by('-id')
        des = designation.objects.get(designation='trainee')
        cut = user_registration.objects.filter(designation_id=des.id)

        return render(request, 'trainer_task_previous_teamlist.html', {'z': z, 'cut': cut, 'tam': tam})
    else:
        return redirect('/')

def trainer_task_previous_team_tasklist(request, id):
    if 'usernametrnr2' in request.session:
       
        if request.session.has_key('usernametrnr2'):
            usernametrnr2 = request.session['usernametrnr2']
       
        z = user_registration.objects.filter(id=usernametrnr2)
        
        d=create_team.objects.get(id=id)
        tsk = trainer_task.objects.filter(team_name_id=d.id).order_by('-id')
    
        return render(request, 'trainer_task_previous_team_tasklist.html', {'z': z, 'tsk':tsk})

    else:
        return redirect('/')
def trainer_trainees(request):
    if 'usernametrnr2' in request.session:
        
        if request.session.has_key('usernametrnr2'):
            usernametrnr2 = request.session['usernametrnr2']
       
        z = user_registration.objects.filter(id=usernametrnr2)
    
        return render(request, 'trainer_trainees.html', {'z': z})
    else:
        return redirect('/')

def trainer_current_trainees(request):
    if 'usernametrnr2' in request.session:
        
        if request.session.has_key('usernametrnr1'):
            usernametrnr1 = request.session['usernametrnr1']
        if request.session.has_key('usernametrnr2'):
            usernametrnr2 = request.session['usernametrnr2']
        else:
            return redirect('/')
    
     
        
        z = user_registration.objects.filter(fullname=usernametrnr1,id=usernametrnr2) 
        cut = create_team.objects.filter(trainer=usernametrnr1).values_list('id',flat=True)
        print(cut)
        des = designation.objects.get(designation='trainee')
        user = user_registration.objects.filter(designation_id=des.id,team_id__in=cut)
        
        return render(request, 'trainer_current_trainees.html', {'z': z, 'n': user})
    else:
        return redirect('/')
################################   NEW    ####################################

def trainer_paymentlist(request):
    if 'usernametrnr2' in request.session:
        if request.session.has_key('usernametrnr'):
            usernametrnr = request.session['usernametrnr']
        if request.session.has_key('usernametrnr1'):
            usernametrnr1 = request.session['usernametrnr1']
        if request.session.has_key('usernametrnr2'):
            usernametrnr2 = request.session['usernametrnr2']
        else:
            return redirect('/')
        z = user_registration.objects.filter(designation_id=usernametrnr) .filter(
            fullname=usernametrnr1) .filter(id=usernametrnr2)
        mem=acntspayslip.objects.filter(user_id=usernametrnr2).all().order_by('-id')
        
        return render(request, 'trainer_paymentlist.html', {'z': z,'mem':mem})
    else:
        return redirect('/')

def trainer_payment_viewslip(request,id,tid):
    if 'usernametrnr2' in request.session:
        if request.session.has_key('usernametrnr'):
            usernametrnr = request.session['usernametrnr']
        if request.session.has_key('usernametrnr1'):
            usernametrnr1 = request.session['usernametrnr1']
        if request.session.has_key('usernametrnr2'):
            usernametrnr2 = request.session['usernametrnr2']
        else:
            return redirect('/')
        z = user_registration.objects.filter(designation_id=usernametrnr) .filter(
            fullname=usernametrnr1) .filter(id=usernametrnr2)
        user = user_registration.objects.get(id=tid)
        acc = acntspayslip.objects.get(id=id)
        names = acntspayslip.objects.all()
        
        
        return render(request, 'trainer_payment_viewslip.html', {'z': z,'user':user,'acc':acc})
    else:
        return redirect('/')

def trainer_payment_print(request,id,tid):
    if 'usernametrnr2' in request.session:
        if request.session.has_key('usernametrnr'):
            usernametrnr = request.session['usernametrnr']
        if request.session.has_key('usernametrnr1'):
            usernametrnr1 = request.session['usernametrnr1']
        if request.session.has_key('usernametrnr2'):
            usernametrnr2 = request.session['usernametrnr2']
        else:
            return redirect('/')
        z = user_registration.objects.filter(designation_id=usernametrnr) .filter(
            fullname=usernametrnr1) .filter(id=usernametrnr2)
        z = user_registration.objects.filter(id=usernametrnr2)   
        user = user_registration.objects.get(id=tid)
        acc = acntspayslip.objects.get(id=id)
        
        
        return render(request, 'trainer_payment_print.html', {'z': z,'user':user,'acc':acc})
    else:
        return redirect('/')

def trainer_current_attendance_view(request, id):
    if 'usernametrnr2' in request.session:
        
        if request.session.has_key('usernametrnr2'):
            usernametrnr2 = request.session['usernametrnr2']
        
        z = user_registration.objects.filter(id=usernametrnr2)
        mem = user_registration.objects.get(id=id)
        return render(request, 'trainer_current_attendance_view.html', {'mem': mem, 'z': z})

    else:
        return redirect('/')

def trainer_attendance_trainees_viewattendance(request):
    if 'usernametrnr2' in request.session:
       
        if request.session.has_key('usernametrnr1'):
            usernametrnr1 = request.session['usernametrnr1']
        if request.session.has_key('usernametrnr2'):
            usernametrnr2 = request.session['usernametrnr2']
        else:
            return redirect('/')
        z = user_registration.objects.filter(fullname=usernametrnr1) .filter(id=usernametrnr2)
        cut=create_team.objects.filter(trainer=usernametrnr1).values_list('id',flat=True)
        des = designation.objects.get(designation='trainee')
        vars = user_registration.objects.filter(designation=des.id,team_id__in=cut)
        return render(request, 'trainer_attendance_trainees_viewattendance.html',{'z':z,'vars':vars})
    else:
        return redirect('/')

def trainer_attendance_trainees_viewattendancelist(request):
    if 'usernametrnr2' in request.session:
        
        if request.session.has_key('usernametrnr2'):
            usernametrnr2 = request.session['usernametrnr2']
       
        z = user_registration.objects.filter(id=usernametrnr2)
        if request.method == 'POST':
            start=request.POST['startdate']
            end=request.POST['enddate']
            user = request.POST['trainee']
            attend=attendance.objects.filter(date__gte=start,date__lte=end,user_id=user)
        return render(request, 'trainer_attendance_trainees_viewattendancelist.html',{'z':z,'attend':attend})
    else:
        return redirect('/')

def trainer_attendance_trainees_addattendance(request):
    if 'usernametrnr2' in request.session:
        
        if request.session.has_key('usernametrnr1'):
            usernametrnr1 = request.session['usernametrnr1']
        if request.session.has_key('usernametrnr2'):
            usernametrnr2 = request.session['usernametrnr2']
        else:
            return redirect('/')
        z = user_registration.objects.filter(fullname=usernametrnr1) .filter(id=usernametrnr2)
        cut=create_team.objects.filter(trainer=usernametrnr1).values_list('id',flat=True)
        des = designation.objects.get(designation='trainee')
        vars = user_registration.objects.filter(designation=des.id,team_id__in=cut)
       
    
        if request.method == 'POST':
            atten = attendance()
            atten.date = request.POST['date']
            atten.user_id =request.POST['sele']
            atten.attendance_status = request.POST['pres']
    
            atten.save()
        return render(request, 'trainer_attendance_trainees_addattendance.html',{'z':z,'vars':vars})
    else:
        return redirect('/')
    
########################################################   trainees       ###############################################
def trainee_dashboard_trainee(request):
    if 'usernametrns2' in request.session:
        
        if request.session.has_key('usernametrns2'):
            usernametrns2 = request.session['usernametrns2']
       
        z = user_registration.objects.filter(id=usernametrns2)
        labels = []
        data = []
        queryset = user_registration.objects.filter(id=usernametrns2)
        for i in queryset:
            labels=[i.workperformance,i.attitude,i.creativity]
            
            
            data=[i.workperformance,i.attitude,i.creativity]
    
        
        return render(request, 'trainee_dashboard_trainee.html', {'z': z , 'labels': labels,'data': data,})
    else:
        return redirect('/')

def trainee_topic(request):
    if 'usernametrns2' in request.session:
        
        if request.session.has_key('usernametrns2'):
            usernametrns2 = request.session['usernametrns2']
        
        z = user_registration.objects.filter(id=usernametrns2)
        return render(request, 'trainee_topic.html', {'z': z})
    else:
        return redirect('/')

def trainee_currentTopic(request):
    if 'usernametrns2' in request.session:
        
        if request.session.has_key('usernametrns2'):
            usernametrns2 = request.session['usernametrns2']
        if request.session.has_key('usernametrns3'):
            usernametrns3 = request.session['usernametrns3']
       
        z = user_registration.objects.filter(id=usernametrns2)
        mem = topic.objects.filter(team_id=usernametrns3) .filter(topic_status=0).order_by('-id')
        return render(request, 'trainee_currentTopic.html', {'mem': mem, 'z': z})
    else:
        return redirect('/')

def save_trainee_review(request):
    if 'usernametrns2' in request.session:
        
        if request.session.has_key('usernametrns2'):
            usernametrns2 = request.session['usernametrns2']
        
        tid = request.GET.get('tid')
        vars = topic.objects.get(id=tid)
        print(vars.id)
        vars.review = request.POST.get('review')
        vars.topic_status = 1
        print('hello')
        vars.save()
        return redirect('trainee_currentTopic')
    else:
        return redirect('/')

def trainee_previousTopic(request):
    if 'usernametrns2' in request.session:
        
        if request.session.has_key('usernametrns2'):
            usernametrns2 = request.session['usernametrns2']
        if request.session.has_key('usernametrns3'):
            usernametrns3 = request.session['usernametrns3']
        else:
            return redirect('/')
        z = user_registration.objects.filter(id=usernametrns2)
        mem = topic.objects.filter(team_id=usernametrns3).filter(topic_status=1)
        return render(request, 'trainee_previousTopic.html', {'mem': mem, 'z': z})
    else:
        return redirect('/')

def trainee_task(request):
    if 'usernametrns2' in request.session:
        
        if request.session.has_key('usernametrns2'):
            usernametrns2 = request.session['usernametrns2']
        
        z = user_registration.objects.filter(id=usernametrns2)
        return render(request, 'trainee_task.html', {'z': z})
    else:
        return redirect('/')

def trainee_task_list(request):
    if 'usernametrns2' in request.session:
       
        if request.session.has_key('usernametrns2'):
            usernametrns2 = request.session['usernametrns2']
        
        z = user_registration.objects.filter(id=usernametrns2)
        mem = trainer_task.objects.filter(user_id=usernametrns2).filter(task_status=0).order_by('-id')
        return render(request, 'trainee_task_list.html', {'mem': mem, 'z': z})
    else:
        return redirect('/')

# def trainee_task_details(request,id):
#     if 'usernametrns2' in request.session:
        
#         if request.session.has_key('usernametrns2'):
#             usernametrns2 = request.session['usernametrns2']
        
#         z = user_registration.objects.filter(id=usernametrns2)
#         tid = request.GET.get('tid')
#         mem = trainer_task.objects.get(id=id)
#         if request.method == 'POST':
#             mem.user_description = request.POST['description']
#             mem.user_files = request.FILES['files']
#             mem.submitteddate = datetime.now()
#             mem.task_status=1
#             mem.save()
#             return render(request, 'trainee_task_details.html', {'mem': mem, 'z': z})
#         return render(request, 'trainee_task_details.html', {'mem': mem, 'z': z})
#     else:
#         return redirect('/')

def trainee_task_details(request, id):
    if 'usernametrns2' in request.session:

        if request.session.has_key('usernametrns2'):
            usernametrns2 = request.session['usernametrns2']

        z = user_registration.objects.filter(id=usernametrns2)
        tid = request.GET.get('tid')
        mem = trainer_task.objects.get(id=id)
        de = mem.enddate
        if request.method == 'POST':
            akm = datetime.now().date()
            mem.user_description = request.POST['description']
            mem.user_files = request.FILES['files']
            mem.submitteddate = datetime.now()
            
            dee = (akm-de).days
            if dee <= 0:
                mem.delay=0
                mem.task_status = 1
                mem.save()
            else:
                mem.delay=(akm-de).days
                mem.task_status = 1
                mem.save()
            mem.task_status = 1
            mem.save()
            return render(request, 'trainee_task_details.html', {'mem': mem, 'z': z})
        return render(request, 'trainee_task_details.html', {'mem': mem, 'z': z})
    else:
        return redirect('/')

def trainee_completed_taskList(request):
    if 'usernametrns2' in request.session:
        
        if request.session.has_key('usernametrns2'):
            usernametrns2 = request.session['usernametrns2']
        
        z = user_registration.objects.filter(id=usernametrns2)
        mem = trainer_task.objects.filter(user_id=usernametrns2).filter(task_status='1').order_by('-id')
        return render(request, 'trainee_completed_taskList.html', {'mem': mem, 'z': z})
    else:
        return redirect('/')

def trainee_reported_issue(request):
    if 'usernametrns2' in request.session:
        
        if request.session.has_key('usernametrns2'):
            usernametrns2 = request.session['usernametrns2']
        
        z = user_registration.objects.filter(id=usernametrns2)
        n = reported_issue.objects.filter(reporter_id=usernametrns2).order_by('-id')
        return render(request, 'trainee_reported_issue.html', {'n': n, 'z': z})
    else:
        return redirect('/')

def trainee_report_reported(request):
    if 'usernametrns2' in request.session:
        if request.session.has_key('usernametrns'):
            usernametrns = request.session['usernametrns']
        
        if request.session.has_key('usernametrns2'):
            usernametrns2 = request.session['usernametrns2']
        
    
        
    
        z=user_registration.objects.filter(designation_id=usernametrns).filter(id=usernametrns2)
        var = reported_issue()
        if request.method == 'POST':
         
    
            
            # ree= user_registration.objects.get(designation_id=mem1)
            var.designation_id=usernametrns
            var.reported_to = user_registration.objects.get(id=int(request.POST['reportto']))
            var.issue = request.POST['report']
            var.reporter_id = usernametrns2
            var.reported_date = datetime.now()
            var.issuestatus=0
            var.save()
            
            
        return render(request, 'trainee_report_reported.html', {'z':z})
    else:
        return redirect('/')

def trainee_report_issue(request):
    if 'usernametrns2' in request.session:
        
        if request.session.has_key('usernametrns2'):
            usernametrns2 = request.session['usernametrns2']
        
        z = user_registration.objects.filter(id=usernametrns2)
    
        desi = designation.objects.get(designation='trainingmanager')
        mem3 = user_registration.objects.filter(designation_id=desi.id)
    
        
    
        team = create_team.objects.all()
        print(team)
        tre = designation.objects.get(designation='trainer')
        use = user_registration.objects.filter(designation_id=tre.id)
        
        print(use)
        
        
        return render(request, 'trainee_report_issue.html', {'list': mem3, 'memteam': use, 'z': z})
    else:
        return redirect('/')

def trainee_applyleave_form(request):
    if 'usernametrns2' in request.session:
        if request.session.has_key('usernametrns'):
            usernametrns = request.session['usernametrns']
        if request.session.has_key('usernametrns1'):
            usernametrns1 = request.session['usernametrns1']
        if request.session.has_key('usernametrns2'):
            usernametrns2 = request.session['usernametrns2']
        
        else:
            return redirect('/')
        z = user_registration.objects.filter(id=usernametrns2)
        le = user_registration.objects.get(id=usernametrns2)
        if request.method == 'POST':
            mem = leave()
            mem.from_date = request.POST['from']
            mem.to_date = request.POST['to']
            mem.leave_status = request.POST['haful']
            mem.reason = request.POST['reason']
            mem.user = le
            mem.designation_id=usernametrns
            mem.leaveapprovedstatus=0

            start = datetime.strptime(mem.from_date, '%Y-%m-%d').date() 
            end = datetime.strptime(mem.to_date, '%Y-%m-%d').date()

            diff = (end  - start).days
            
            cnt =  Event.objects.filter(start_time__range=(start,end)).count()
            
            if diff == 0:
                mem.days = 1
            else:
                mem.days = diff - cnt
            mem.save()
            return render(request, 'trainee_applyleave_form.html', {'z': z})
        return render(request, 'trainee_applyleave_form.html', {'z': z})
    else:
        return redirect('/')



def trainer_applyleave_cards(request):
   
    if 'usernametrnr2' in request.session:
       
        if request.session.has_key('usernametrnr2'):
            usernametrnr2 = request.session['usernametrnr2']
       
        z = user_registration.objects.filter(id=usernametrnr2)
    
        
        return render(request, 'trainer_applyleave_cards.html',{'z' : z})
    else:
        return redirect('/')

def trainer_appliedleave(request):
    if 'usernametrnr2' in request.session:
       
        if request.session.has_key('usernametrnr2'):
            usernametrnr2 = request.session['usernametrnr2']
        
        z = user_registration.objects.filter(id=usernametrnr2)
        des = designation.objects.get(designation='trainer')
        tm = leave.objects.filter(user_id=usernametrnr2).order_by('-id')
        
        return render(request, 'trainer_appliedleave.html',{'tm': tm, 'z': z})
    else:
        return redirect('/')

def logout4(request):
    if 'usernametrns2' in request.session:  
        request.session.flush()
        return redirect('/')
    else:
        return redirect('/') 
def logout2(request):
    if 'usernametrnr2' in request.session:  
        request.session.flush()
        return redirect('/')
    else:
        return redirect('/') 

def logout3(request):
    if 'usernametm2' in request.session:  
        request.session.flush()
        return redirect('/')
    else:
        return redirect('/') 
 ############ attendence #############

def trainee_applyleave_cards(request):
    if 'usernametrns2' in request.session:
        
        if request.session.has_key('usernametrns2'):
            usernametrns2 = request.session['usernametrns2']
        
        z = user_registration.objects.filter(id=usernametrns2)
    
        
        return render(request, 'trainee_applyleave_cards.html',{'z' : z})
    else:
        return redirect('/')
def trainee_appliedleave(request):
    if 'usernametrns2' in request.session:
       
        if request.session.has_key('usernametrns2'):
            usernametrns2 = request.session['usernametrns2']
       
        z = user_registration.objects.filter(id=usernametrns2)
        lee = user_registration.objects.get(id=usernametrns2)
    
        des = designation.objects.get(designation='trainee')
        n = leave.objects.filter(user_id=lee.id) .all().order_by('-id')
        
        return render(request, 'trainee_appliedleave.html',{'z' : z,'n' : n})
    else:
        return redirect('/')

def Attendance(request):
    if 'usernametrns2' in request.session:
        
        if request.session.has_key('usernametrns2'):
            usernametrns2 = request.session['usernametrns2']
        
        z = user_registration.objects.filter(id=usernametrns2)
        return render(request,'trainees_attendance.html',{'z':z})
    else:
        return redirect('/')
def trainees_attendance_viewattendance(request):
    if 'usernametrns2' in request.session:
        
        if request.session.has_key('usernametrns2'):
            usernametrns2 = request.session['usernametrns2']
        
        z = user_registration.objects.filter(id=usernametrns2)
        return render(request,'trainees_attendance_viewattendance.html',{'z':z})
    else:
        return redirect('/')
def trainees_attendance_viewattendancelist(request):
    if 'usernametrns2' in request.session:
       
        if request.session.has_key('usernametrns2'):
            usernametrns2 = request.session['usernametrns2']
       
        z = user_registration.objects.filter(id=usernametrns2) 
        
        if request.method == 'POST':
            start=request.POST['startdate']
            end=request.POST['enddate']
            user=usernametrns2
            vars=attendance.objects.filter(date__gte=start,date__lte=end,user_id=user)
           
        return render(request,'trainees_attendance_viewattendancelist.html',{'z':z,'vars':vars})
    else:
        return redirect('/')
    ##########################  Account ############################################
def account_tr_mg(request):
    if 'usernametm2' in request.session:
        
        if request.session.has_key('usernametm2'):
            usernametm2 = request.session['usernametm2']
        
        mem = user_registration.objects.filter(id=usernametm2)
    
    
        return render(request, 'account_tr_mg.html', {'mem': mem})
    else:
        return redirect('/')
def imagechange_tr(request):
  
    if request.method == 'POST':
        id = request.GET.get('id')
        abc = user_registration.objects.get(id=id)
        abc.photo = request.FILES['filename']
        
        abc.save()
        return redirect('account_tr_mg')
    return render(request, 'account_tr_mg.html')

    





def account_trainer(request):
    if 'usernametrnr2' in request.session:
        
        if request.session.has_key('usernametrnr2'):
            usernametrnr2 = request.session['usernametrnr2']
    
        z = user_registration.objects.filter(id=usernametrnr2)
    
    
        return render(request, 'account_trainer.html', {'z': z})
    else:
        return redirect('/')
def imagechange(request):
    
    if request.method == 'POST':
        id = request.GET.get('id')
        abc = user_registration.objects.get(id=id)
        abc.photo = request.FILES['filenamees']
        abc.save()
        return redirect('account_trainer')
    return render(request, 'account_trainer.html' )



def account_trainees(request):
    if 'usernametrns2' in request.session:
        
        if request.session.has_key('usernametrns2'):
            usernametrns2 = request.session['usernametrns2']
        
        z = user_registration.objects.filter(id=usernametrns2)
    
    
        return render(request, 'account_trainees.html', {'z': z})
    else:
        return redirect('/')

def imagechange_trainees(request):
    
    if request.method == 'POST':
        id = request.GET.get('id')
        abc = user_registration.objects.get(id=id)
        abc.photo = request.FILES['filenamees']
        abc.save()
        return redirect('account_trainees')
    return render(request, 'account_trainees.html' )






###################################  change password ################################  

def changepassword_trainer(request):
    if 'usernametrnr2' in request.session:
        
        if request.session.has_key('usernametrnr2'):
            usernametrnr2 = request.session['usernametrnr2']
    
        z = user_registration.objects.filter(id=usernametrnr2)
    
        
        if request.method == 'POST':
            abc = user_registration.objects.get(id=usernametrnr2)
    
            oldps = request.POST['currentPassword']
            newps = request.POST['newPassword']
            cmps = request.POST.get('confirmPassword')
            if oldps != newps:
                if newps == cmps:
                    abc.password = request.POST.get('confirmPassword')
                    abc.save()
                    return render(request, 'trainer_dashboard.html', {'z': z})
    
            elif oldps == newps:
                messages.add_message(request, messages.INFO, 'Current and New password same')
            else:
                messages.info(request, 'Incorrect password same')
    
            return render(request, 'changepassword_trainer.html', {'z': z})
    
        return render(request, 'changepassword_trainer.html', {'z': z})
    
    else:
        return redirect('/')
        

def changepassword_tr_mg(request):
    if 'usernametm2' in request.session:
       
        if request.session.has_key('usernametm2'):
            usernametm2 = request.session['usernametm2']
       
        mem = user_registration.objects.filter(id=usernametm2)
    
        if request.method == 'POST':
            abc = user_registration.objects.get(id=usernametm2)
    
            oldps = request.POST['currentPassword']
            newps = request.POST['newPassword']
            cmps = request.POST.get('confirmPassword')
            if oldps != newps:
                if newps == cmps:
                    abc.password = request.POST.get('confirmPassword')
                    abc.save()
                    return render(request, 'Dashboard.html', {'mem': mem})
            elif oldps == newps:
                messages.add_message(request, messages.INFO, 'Current and New password same')
            else:
                messages.info(request, 'Incorrect password same')
    
            return render(request, 'changepassword_tr_mg.html', {'mem': mem})
    
        return render(request, 'changepassword_tr_mg.html', {'mem': mem})

    else:
        return redirect('/')

def changepassword_trainees(request):
    if 'usernametrns2' in request.session:
       
        if request.session.has_key('usernametrns2'):
            usernametrns2 = request.session['usernametrns2']
        
    
        z = user_registration.objects.filter(id=usernametrns2)
    
        if request.method == 'POST':
            abc = user_registration.objects.get(id=usernametrns2)
    
            oldps = request.POST['currentPassword']
            newps = request.POST['newPassword']
            cmps = request.POST.get('confirmPassword')
            if oldps != newps:
                if newps == cmps:
                    abc.password = request.POST.get('confirmPassword')
                    abc.save()
                    return render(request, 'trainee_dashboard_trainee.html', {'z': z})
            elif oldps == newps:
                messages.add_message(request, messages.INFO, 'Current and New password same')
            else:
                messages.info(request, 'Incorrect password same')
                
    
            return render(request, 'changepassword_trainees.html', {'z': z})
    
        return render(request, 'changepassword_trainees.html', {'z': z})
    else:
        return redirect('/')

############################################# Amal ###########################################################
def Admlogout(request):
    if 'Adm_id' in request.session:  
        request.session.flush()
        return redirect('/')
    else:
        return redirect('/') 

def Mnlogout(request):
    if 'm_id' in request.session:  
        request.session.flush()
        return redirect('/')
    else:
        return redirect('/')
        
@csrf_exempt
def BRadmin_emp_ajax(request):
    if 'Adm_id' in request.session:
        if request.session.has_key('Adm_id'):
            Adm_id = request.session['Adm_id']
        else:
            return redirect('/')
        Adm = user_registration.objects.filter(id=Adm_id)

        dept_id = request.GET.get('dept_id')
        desigId = request.GET.get('desigId')
        br_id = department.objects.get(id=dept_id)
        Desig = user_registration.objects.filter(branch_id=br_id.branch_id, designation=desigId)

        return render(request,'BRadmin_emp_ajax.html',{'Adm': Adm,'Desig': Desig,})
    else:
        return redirect('/')
        
@csrf_exempt
def BRadmin_designations(request):
    if 'Adm_id' in request.session:
        if request.session.has_key('Adm_id'):
            Adm_id = request.session['Adm_id']
        else:
            return redirect('/')
        Adm = user_registration.objects.filter(id=Adm_id)

        dept_id = request.GET.get('dept_id')
        
        br_id = department.objects.get(id=dept_id)
        print('haii')
        print(br_id)
        Desig = designation.objects.filter(~Q(designation="admin"),~Q(designation="manager"),~Q(designation="project manager"),~Q(designation="tester"),~Q(designation="trainingmanager"),~Q(designation="trainer"),~Q(designation="trainee"),~Q(designation="account")).filter(branch_id=br_id.branch_id)
        return render(request,'BRadmin_designations.html',{'Adm': Adm,'Desig': Desig, })
    else:
        return redirect('/')

# ********************Admin account setting****************************
def BRadmin_accsetting(request):
    if 'Adm_id' in request.session:
        
        if request.session.has_key('Adm_id'):
            Adm_id = request.session['Adm_id']
        
        Adm = user_registration.objects.filter(id=Adm_id)
        return render(request,'BRadmin_accsetting.html', {'Adm': Adm})
    else:
        return redirect('/')

def BRadmin_accsettingimagechange(request,id):
    if 'Adm_id' in request.session:
        
        if request.session.has_key('Adm_id'):
            Adm_id = request.session['Adm_id']
        
        Adm = user_registration.objects.filter(id=Adm_id)
        if request.method == 'POST':
            abc = user_registration.objects.get(id=id)
            abc.photo = request.FILES['filename']
            abc.save()
            return redirect('BRadmin_accsetting')
        return render(request, 'BRadmin_accsetting.html',{'Adm':Adm})
    else:
        return redirect('/')

# ********************Manager account setting****************************

def MAN_accsetting(request):
    if 'm_id' in request.session:
        if request.session.has_key('m_id'):
            m_id = request.session['m_id']
        
        mem = user_registration.objects.filter(id=m_id)
        return render(request,'MAN_accsetting.html', {'mem': mem})
    else:
        return redirect('/')

def MAN_accsettingimagechange(request,id):
    if 'm_id' in request.session:
        
        if request.session.has_key('m_id'):
            m_id = request.session['m_id']
        
        mem = user_registration.objects.filter(id=m_id)
        if request.method == 'POST':
            abc = user_registration.objects.get(id=id)
            abc.photo = request.FILES['filename']
            abc.save()
            return redirect('MAN_accsetting')
        return render(request, 'MAN_accsetting.html',{'mem':mem})
    else:
        return redirect('/')


# ***************Admin change password*****************
def BRadmin_changepwd(request):
    
    if 'Adm_id' in request.session:
        
        if request.session.has_key('Adm_id'):
            Adm_id = request.session['Adm_id']     
        Adm = user_registration.objects.filter(id=Adm_id)     
        if request.method == 'POST':
            abc = user_registration.objects.get(id=Adm_id)
            cur = abc.password
            oldps = request.POST["currentPassword"]
            newps = request.POST["newPassword"]
            cmps = request.POST["confirmPassword"]
            if oldps == cur:
                if oldps != newps:
                    if newps == cmps:
                        abc.password = request.POST.get('confirmPassword')
                        abc.save()
                        return render(request, 'BRadmin_profiledash.html', {'Adm': Adm})
                elif oldps == newps:
                    messages.add_message(request, messages.INFO, 'Current and New password same')
                else:
                    messages.info(request, 'Incorrect password same')

                return render(request, 'BRadmin_profiledash.html', {'Adm': Adm})
            else:
                messages.add_message(request, messages.INFO, 'old password wrong')
                return render(request, 'BRadmin_changepwd.html', {'Adm': Adm})
        return render(request, 'BRadmin_changepwd.html', {'Adm': Adm})         
    else:
        return redirect('/')

# ***************Manager change password*****************

def MAN_changepwd(request):
    if 'm_id' in request.session:
        
        if request.session.has_key('m_id'):
            m_id = request.session['m_id']
        
        mem = user_registration.objects.filter(id=m_id)
    
        
        if request.method == 'POST':
            abc = user_registration.objects.get(id=m_id)
    
            oldps = request.POST['currentPassword']
            newps = request.POST['newPassword']
            cmps = request.POST.get('confirmPassword')
            if oldps != newps:
                if newps == cmps:
                    abc.password = request.POST.get('confirmPassword')
                    abc.save()
                    return render(request, 'MAN_profiledash.html', {'mem': mem})
    
            elif oldps == newps:
                messages.add_message(request, messages.INFO, 'Current and New password same')
            else:
                messages.info(request, 'Incorrect password same')
    
            return render(request, 'MAN_changepwd.html', {'mem': mem})
    
        return render(request, 'MAN_changepwd.html', {'mem': mem})
    
    else:
        return redirect('/')


# ***********************anandu*****************************************
def MAN_index(request):
    if 'm_id' in request.session:
        if request.session.has_key('m_id'):
            m_id = request.session['m_id']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(id=m_id)
        return render(request,'MAN_index.html',{'mem':mem})
    else:
        return redirect('/') 

def MAN_profiledash(request):
    if 'm_id' in request.session:
        if request.session.has_key('m_id'):
            m_id = request.session['m_id']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(id=m_id)
        Num = user_registration.objects.count()
        Num1 = project.objects.count()
        Trainer = designation.objects.get(designation='Trainer')
        trcount=user_registration.objects.filter(designation=Trainer).count()
        Man1 = designation.objects.get(designation='Manager')
        Man2 = user_registration.objects.filter(designation = Man1)
        labels = []
        data = []
        queryset = user_registration.objects.filter(id=m_id)
        for i in queryset:
                labels=[i.workperformance,i.attitude,i.creativity]
                data=[i.workperformance,i.attitude,i.creativity]
        return render(request,'MAN_profiledash.html',{'labels':labels,'data':data,'Man1':Man2,'mem':mem,'num':Num,'trcount':trcount,'Num1':Num1})   
    else:
        return redirect('/') 
        
def MAN_employees(request):
    if 'm_id' in request.session:
        if request.session.has_key('m_id'):
            m_id = request.session['m_id']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(id=m_id)
        Dept = department.objects.all()
        return render(request,'MAN_employees.html',{'mem':mem,'Dept':Dept})
    else:
        return redirect('/')
        
def MAN_python(request,id):
    if 'm_id' in request.session:
        if request.session.has_key('m_id'):
            m_id = request.session['m_id']
        else:
            return redirect('/')
        Dept = department.objects.get(id = id)
        deptid=id
        mem = user_registration.objects.filter(id=m_id)
        Desig = designation.objects.all()
        return render(request,'MAN_python.html',{'mem':mem,'Desig':Desig,'Dept':Dept,'dept_id':deptid})
    else:
        return redirect('/')

def MAN_projectman(request,id,did):
    if 'm_id' in request.session:
        if request.session.has_key('m_id'):
            m_id = request.session['m_id']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(id=m_id)
        Project_man= designation.objects.get(id = id)
        project_name = project.objects.filter(designation=Project_man).filter(department=did)
        Project_man_data=user_registration.objects.filter(designation=Project_man).filter(department=did).order_by("-id")
        return render(request,'MAN_projectman.html',{'pro_man_data':Project_man_data,'mem':mem,'project_name':project_name,'Project_man':Project_man})
    else:
        return redirect('/')
        
def MAN_proname(request,id):
    if 'm_id' in request.session:
        if request.session.has_key('m_id'):
            m_id = request.session['m_id']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(id=m_id)
        Project_man_data = user_registration.objects.get(id = id)
        labels = []
        data = []
        queryset = user_registration.objects.filter(id=id)
        for i in queryset:
            labels=[i.workperformance,i.attitude,i.creativity]
            
            
            data=[i.workperformance,i.attitude,i.creativity]
        return render(request,'MAN_proname.html',{'labels':labels,'data':data,'pro_man_data':Project_man_data,'mem':mem})
    else:
        return redirect('/')
        
def MAN_proinvolve(request,id):
    if 'm_id' in request.session:
        if request.session.has_key('m_id'):
            m_id = request.session['m_id']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(id=m_id)
        Pro_data = project.objects.filter(projectmanager_id = id).order_by("-id")
        return render(request,'MAN_proinvolve.html',{'pro_data':Pro_data,'mem':mem})
    else:
        return redirect('/')
        
def MAN_promanatten(request,id):
    if 'm_id' in request.session:
        if request.session.has_key('m_id'):
            m_id = request.session['m_id']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(id=m_id)
        id = id
        return render(request, 'MAN_promanatten.html',{'mem':mem,'id':id})
    else:
        return redirect('/')

def MAN_promanattendsort(request,id):
    if 'm_id' in request.session:
        if request.session.has_key('m_id'):
            m_id = request.session['m_id']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(id=m_id)
        id = id
        if request.method == "POST":
            fromdate = request.POST.get('fromdate')
            todate = request.POST.get('todate') 
            # mem1 = attendance.objects.raw('select * from app_attendance where user_id and date between "'+fromdate+'" and "'+todate+'"')
            mem1 = attendance.objects.filter(date__range=[fromdate, todate]).filter(user_id = id)
        return render(request, 'MAN_promanattendsort.html',{'mem1':mem1,'mem':mem,'id':id})
    else:
        return redirect('/')     


def BRadmin_index(request):
    if 'Adm_id' in request.session:
        if request.session.has_key('Adm_id'):
            Adm_id = request.session['Adm_id']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(id=Adm_id)
        return render(request,'BRadmin_index.html',{'mem':mem})
    else:
        return redirect('/')
    
def BRadmin_profiledash(request):
    if 'Adm_id' in request.session:
        if request.session.has_key('Adm_id'):
            Adm_id = request.session['Adm_id']
        else:
            variable = "dummy"
        Adm = user_registration.objects.filter(id=Adm_id)
        Num = user_registration.objects.count()
        Num1 = project.objects.count()
        Trainer = designation.objects.get(designation='Trainer')
        trcount = user_registration.objects.filter(designation=Trainer).count()
        Man1 = designation.objects.get(designation='Manager')
        Man2 = user_registration.objects.filter(designation=Man1)
        des = designation.objects.get(designation="trainee")
        le = leave.objects.filter(
            leaveapprovedstatus=0).exclude(designation_id=des.id)
        labels = []
        data = []
        queryset = user_registration.objects.filter(id=Adm_id)

        for i in queryset:
            labels = [i.workperformance, i.attitude, i.creativity]
            data = [i.workperformance, i.attitude, i.creativity]
        return render(request, 'BRadmin_profiledash.html', {'labels': labels, 'data': data, 'Num1': Num1, 'Man1': Man2, 'Adm': Adm, 'num': Num, 'trcount': trcount, 'le': le})
    else:
        return redirect('/')

def BRadmin_employees(request):
    if 'Adm_id' in request.session:
        if request.session.has_key('Adm_id'):
            Adm_id = request.session['Adm_id']
        else:
            return redirect('/')
        Adm = user_registration.objects.filter(id=Adm_id)
        Dept = department.objects.all()
        return render(request,'BRadmin_employees1.html',{'Adm':Adm,'Dept':Dept})
    else:
        return redirect('/')

def BRadmin_python(request,id):
    if 'Adm_id' in request.session:
        if request.session.has_key('Adm_id'):
            Adm_id = request.session['Adm_id']
        else:
            return redirect('/')
        Dept = department.objects.get(id = id)
        deptid=id
        Adm = user_registration.objects.filter(id=Adm_id)
        Desig = designation.objects.all()
        return render(request,'BRadmin_python.html',{'Adm':Adm,'Desig':Desig,'Dept':Dept,'dept_id':deptid})
    else:
        return redirect('/')
        
def BRadmin_projectman(request,id,did):
    if 'Adm_id' in request.session:
        if request.session.has_key('Adm_id'):
            Adm_id = request.session['Adm_id']
        else:
            return redirect('/')
        Adm = user_registration.objects.filter(id=Adm_id)
        Project_man= designation.objects.get(id = id)
        project_name = project.objects.filter(designation=Project_man).filter(department=did)
        Project_man_data=user_registration.objects.filter(designation=Project_man).filter(department=did).order_by("-id")
        return render(request,'BRadmin_projectman.html',{'pro_man_data':Project_man_data,'Adm':Adm,'project_name':project_name,'Project_man':Project_man})
    else:
        return redirect('/')
        
def BRadmin_proname(request,id):
    if 'Adm_id' in request.session:
        if request.session.has_key('Adm_id'):
            Adm_id = request.session['Adm_id']
        else:
            return redirect('/')
        Adm = user_registration.objects.filter(id=Adm_id)
        Project_man_data = user_registration.objects.get(id = id)
        labels = []
        data = []
        queryset = user_registration.objects.filter(id=id)
        for i in queryset:
            labels=[i.workperformance,i.attitude,i.creativity]
            
            
            data=[i.workperformance,i.attitude,i.creativity]
        return render(request,'BRadmin_proname.html',{'labels':labels,'data':data,'pro_man_data':Project_man_data,'Adm':Adm})
    else:
        return redirect('/')
        
def BRadmin_proinvolve(request,id):
    if 'Adm_id' in request.session:
        if request.session.has_key('Adm_id'):
            Adm_id = request.session['Adm_id']
        else:
            return redirect('/')
        Adm = user_registration.objects.filter(id=Adm_id)
        Pro_data = project.objects.filter(projectmanager_id = id).order_by("-id")
        return render(request,'BRadmin_proinvolve.html',{'pro_data':Pro_data,'Adm':Adm})
    else:
        return redirect('/')
        
def BRadmin_promanatten(request,id):
    if 'Adm_id' in request.session:
        if request.session.has_key('Adm_id'):
            Adm_id = request.session['Adm_id']
        else:
            return redirect('/')
        Adm = user_registration.objects.filter(id=Adm_id)
        id = id
        return render(request, 'BRadmin_promanatten.html',{'Adm':Adm,'id':id})
    else:
        return redirect('/')

def BRadmin_promanattendsort(request,id):
    if 'Adm_id' in request.session:
        if request.session.has_key('Adm_id'):
            Adm_id = request.session['Adm_id']
        else:
            return redirect('/')
        Adm = user_registration.objects.filter(id=Adm_id)
        id = id
        if request.method == "POST":
            fromdate = request.POST.get('fromdate')
            todate = request.POST.get('todate') 
            # mem1 = attendance.objects.raw('select * from app_attendance where user_id and date between "'+fromdate+'" and "'+todate+'"')
            mem1 = attendance.objects.filter(date__range=[fromdate, todate]).filter(user_id = id)
        return render(request, 'BRadmin_promanattendsort.html',{'mem1':mem1,'Adm':Adm,'id':id})
    else:
        return redirect('/') 


# ***********************praveen************************
def BRadmin_trainerstable(request,did):
    if 'Adm_id' in request.session:
        if request.session.has_key('Adm_id'):
            Adm_id = request.session['Adm_id']
        else:
            return redirect('/')
        Dept = department.objects.get(id = did)
        deptid=did
        Adm = user_registration.objects.filter(id=Adm_id)
        Trainer = designation.objects.get(designation='Trainer')
        # Trainer = designation.objects.get(id=id)
        trainers_data=user_registration.objects.filter(designation=Trainer).filter(department=did)
        topics=topic.objects.all()
        return render(request,'BRadmin_trainerstable.html',{'Adm':Adm,'trainers_data':trainers_data,'topics':topics,'Dept':Dept,'deptid':deptid})
    else:
        return redirect('/')

    
def BRadmin_Training(request,id):
    if 'Adm_id' in request.session:
        if request.session.has_key('Adm_id'):
            Adm_id = request.session['Adm_id']
        else:
            return redirect('/')
        Adm = user_registration.objects.filter(id=Adm_id)
        # team=create_team.objects.filter(user_id=id)
        # return render(request,'BRadmin_Training.html',{'team':team})
            # team=create_team.objects.all()
        user=user_registration.objects.filter(id=id)
        team=create_team.objects.all()
        return render(request,'BRadmin_Training.html',{'team':team,'user':user,'Adm':Adm})
    else:
        return redirect('/') 
    
def BRadmin_trainingteam1(request,id):
    if 'Adm_id' in request.session:
        if request.session.has_key('Adm_id'):
            Adm_id = request.session['Adm_id']
        else:
            return redirect('/')
        Adm = user_registration.objects.filter(id=Adm_id)
        id=id
        Trainee = designation.objects.get(designation='Trainee')
        num=previousTeam.objects.filter(teamname_id=id).count()
        num1=topic.objects.filter(team=id).count()
        return render(request,'BRadmin_trainingteam1.html',{'id':id,'num':num,'num1':num1,'Adm':Adm})
    else:
        return redirect('/') 
    
def BRadmin_traineestable(request,id):
    if 'Adm_id' in request.session:
        if request.session.has_key('Adm_id'):
            Adm_id = request.session['Adm_id']
        else:
            return redirect('/')
        Adm = user_registration.objects.filter(id=Adm_id)
        Trainee = designation.objects.get(designation='Trainee')
        trainees_data=previousTeam.objects.filter(teamname_id=id)
        return render(request,'BRadmin_traineestable.html',{'trainees_data':trainees_data,'Adm':Adm}) 
    else:
        return redirect('/') 
        
def BRadmin_trainingprofile(request,id):
    if 'Adm_id' in request.session:
        if request.session.has_key('Adm_id'):
            Adm_id = request.session['Adm_id']
        else:
            return redirect('/')
        Adm = user_registration.objects.filter(id=Adm_id)
        trainees_data=user_registration.objects.get(id=id)
        # Trainee = designation.objects.get(designation='Trainee')
        # trainees_data=user_registration.objects.filter(designation=Trainee)
        user=user_registration.objects.get(id=id)
        num=trainer_task.objects.filter(user=user).filter(task_status='1').count()
        return render(request,'BRadmin_trainingprofile.html',{'trainees_data':trainees_data,'num':num,'Adm':Adm})
    else:
        return redirect('/') 
        
def BRadmin_completedtasktable(request,id):
    if 'Adm_id' in request.session:
        if request.session.has_key('Adm_id'):
            Adm_id = request.session['Adm_id']
        else:
            return redirect('/')
        Adm = user_registration.objects.filter(id=Adm_id)
        user=user_registration.objects.get(id=id)
        task=trainer_task.objects.filter(user=user)
        return render(request,'BRadmin_completedtasktable.html',{'task_data':task,'Adm':Adm})   
    else:
        return redirect('/')
        
def BRadmin_topictable(request,id):
    if 'Adm_id' in request.session:
        if request.session.has_key('Adm_id'):
            Adm_id = request.session['Adm_id']
        else:
            return redirect('/')
        Adm = user_registration.objects.filter(id=Adm_id)
        topics=topic.objects.filter(team=id).order_by("-id")
        return render(request,'BRadmin_topictable.html',{'topics':topics,'Adm':Adm})
    else:
        return redirect('/')

def MAN_trainerstable(request,id):
    if 'm_id' in request.session:
        if request.session.has_key('m_id'):
            m_id = request.session['m_id']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(id=m_id)
        departments=department.objects.get(id=id)
        Trainer = designation.objects.get(designation='Trainer')
        trainers_data=user_registration.objects.filter(designation=Trainer).filter(department=id).order_by("-id")
        topics=topic.objects.all()
        return render(request,'MAN_trainerstable.html',{'trainers_data':trainers_data,'topics':topics,'mem':mem,'departments':departments})
    else:
        return redirect('/')
        
def MAN_Training(request,id):
    if 'm_id' in request.session:
        if request.session.has_key('m_id'):
            m_id = request.session['m_id']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(id=m_id)
        # team=create_team.objects.filter(user_id=id)
        # return render(request,'BRadmin_Training.html',{'team':team})
            # team=create_team.objects.all()
        user=user_registration.objects.filter(id=id)
        team=create_team.objects.all()
        return render(request,'MAN_Training.html',{'team':team,'user':user,'mem':mem})
    else:
        return redirect('/')
        
def MAN_trainingteam1(request,id):
    if 'm_id' in request.session:
        if request.session.has_key('m_id'):
            m_id = request.session['m_id']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(id=m_id)
        id=id
        Trainee = designation.objects.get(designation='Trainee')
        num=user_registration.objects.filter(designation=Trainee).filter(team=id).count()
        num1=topic.objects.filter(team=id).count()
        return render(request,'MAN_trainingteam1.html',{'id':id,'num':num,'num1':num1,'mem':mem})
    else:
        return redirect('/')
        
def MAN_traineestable(request,id):
    if 'm_id' in request.session:
        if request.session.has_key('m_id'):
            m_id = request.session['m_id']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(id=m_id)
        Trainee = designation.objects.get(designation='Trainee')
        trainees_data=user_registration.objects.filter(designation=Trainee).filter(team=id)
        return render(request,'MAN_traineestable.html',{'trainees_data':trainees_data,'mem':mem}) 
    else:
        return redirect('/')
        
def MAN_trainingprofile(request,id):
    if 'm_id' in request.session:
        if request.session.has_key('m_id'):
            m_id = request.session['m_id']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(id=m_id)
        trainees_data=user_registration.objects.get(id=id)
        # Trainee = designation.objects.get(designation='Trainee')
        # trainees_data=user_registration.objects.filter(designation=Trainee)
        user=user_registration.objects.get(id=id)
        num=trainer_task.objects.filter(user=user).filter(status='Completed').count()
        return render(request,'MAN_trainingprofile.html',{'trainees_data':trainees_data,'num':num,'mem':mem})
    else:
        return redirect('/')
        
def MAN_completedtasktable(request,id):
    if 'm_id' in request.session:
        if request.session.has_key('m_id'):
            m_id = request.session['m_id']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(id=m_id)
        user=user_registration.objects.get(id=id)
        task=trainer_task.objects.filter(user=user)
        return render(request,'MAN_completedtasktable.html',{'task_data':task,'mem':mem})
    else:
        return redirect('/')
        
def MAN_topictable(request,id):
    if 'm_id' in request.session:
        if request.session.has_key('m_id'):
            m_id = request.session['m_id']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(id=m_id)
        topics=topic.objects.filter(team=id).order_by("-id")
        return render(request,'MAN_topictable.html',{'topics':topics,'mem':mem})
    else:
        return redirect('/')



# *******************    anwar     ****************************

def BRadmin_View_Trainers(request,id,did):
    if 'Adm_id' in request.session:
        if request.session.has_key('Adm_id'):
            Adm_id = request.session['Adm_id']
        else:
            return redirect('/')
        Adm = user_registration.objects.filter(id=Adm_id)
        
        projectname=project.objects.all()
        trainer=designation.objects.get(id=id)
        userreg=user_registration.objects.filter(designation=trainer).filter(department=did).order_by("-id")
        return render(request,'BRadmin_View_Trainers.html', {'Adm':Adm,'user_registration':userreg, 'project':projectname})
    else:
        return redirect('/')

def BRadmin_View_Trainerprofile(request,id):
    if 'Adm_id' in request.session:
        if request.session.has_key('Adm_id'):
            Adm_id = request.session['Adm_id']
        else:
            return redirect('/')
        Adm = user_registration.objects.filter(id=Adm_id)
        userreg=user_registration.objects.get(id=id)
        return render(request,'BRadmin_View_Trainerprofile.html', {'Adm':Adm,'user_registration':userreg})
    else:
        return redirect('/')

def BRadmin_View_Currenttraineesoftrainer(request,id):
    if 'Adm_id' in request.session:
        if request.session.has_key('Adm_id'):
            Adm_id = request.session['Adm_id']
        else:
            return redirect('/')
        Adm = user_registration.objects.filter(id=Adm_id)
        user=user_registration.objects.filter(id=id)
        trainee=designation.objects.get(designation='trainee')
        user2=user_registration.objects.filter(designation=trainee)
        return render(request,'BRadmin_View_Currenttraineesoftrainer.html',{'Adm':Adm,'user_registration':user,'user_registration2':user2})
    else:
        return redirect('/')
        
def BRadmin_View_Previoustraineesoftrainer(request,id):
    if 'Adm_id' in request.session:
        if request.session.has_key('Adm_id'):
            Adm_id = request.session['Adm_id']
        else:
            return redirect('/')
        Adm = user_registration.objects.filter(id=Adm_id)
        user=user_registration.objects.filter(id=id)
        trainee=designation.objects.get(designation='trainee')
        user2=user_registration.objects.filter(designation=trainee)
        return render(request,'BRadmin_View_Previoustraineesoftrainer.html',{'Adm':Adm,'user_registration':user,'user_registration2':user2})
    else:
        return redirect('/')
        
def BRadmin_View_Currenttraineeprofile(request,id):
    if 'Adm_id' in request.session:
        if request.session.has_key('Adm_id'):
            Adm_id = request.session['Adm_id']
        else:
            return redirect('/')
        Adm = user_registration.objects.filter(id=Adm_id)
        userreg=user_registration.objects.get(id=id)
        return render(request,'BRadmin_View_Currenttraineeprofile.html', {'Adm':Adm,'user_registration':userreg})
    else:
        return redirect('/')
        
def BRadmin_View_Currenttraineetasks(request,id):
    if 'Adm_id' in request.session:
        if request.session.has_key('Adm_id'):
            Adm_id = request.session['Adm_id']
        else:
            return redirect('/')
        Adm = user_registration.objects.filter(id=Adm_id)
        # user=user_registration.objects.get(id=id)
        tasks=trainer_task.objects.filter(user=id)
        return render(request,'BRadmin_View_Currenttraineetasks.html',{'Adm':Adm,'trainer_task':tasks})
    else:
        return redirect('/')
        
def BRadmin_View_Currenttraineeattendance(request,id):
    if 'Adm_id' in request.session:
        if request.session.has_key('Adm_id'):
            Adm_id = request.session['Adm_id']
        else:
            return redirect('/')
        Adm = user_registration.objects.filter(id=Adm_id)
        usr=user_registration.objects.get(id=id)
        return render(request,'BRadmin_View_Currenttraineeattendance.html', {'Adm':Adm,'user_registration':usr})
    else:
        return redirect('/')

def BRadmin_View_Previoustraineeprofile(request,id):
    if 'Adm_id' in request.session:
        if request.session.has_key('Adm_id'):
            Adm_id = request.session['Adm_id']
        else:
            return redirect('/')
        Adm = user_registration.objects.filter(id=Adm_id)
        usr=user_registration.objects.get(id=id)
        return render(request,'BRadmin_View_Previoustraineeprofile.html', {'Adm':Adm,'user_registration':usr})
    else:
        return redirect('/')

def BRadmin_View_Previoustraineetasks(request,id):
    if 'Adm_id' in request.session:
        if request.session.has_key('Adm_id'):
            Adm_id = request.session['Adm_id']
        else:
            return redirect('/')
        Adm = user_registration.objects.filter(id=Adm_id)
        user=user_registration.objects.get(id=id)
        tasks=trainer_task.objects.filter(user=user)
        return render(request,'BRadmin_View_Previoustraineetasks.html',{'Adm':Adm,'trainer_task':tasks})
    else:
        return redirect('/')

def BRadmin_View_Previoustraineeattendance(request,id):
    if 'Adm_id' in request.session:
        if request.session.has_key('Adm_id'):
            Adm_id = request.session['Adm_id']
        else:
            return redirect('/')
        Adm = user_registration.objects.filter(id=Adm_id)
        usr=user_registration.objects.get(id=id)
        return render(request,'BRadmin_View_Previoustraineeattendance.html', {'Adm':Adm,'user_registration':usr})
    else:
        return redirect('/')

def BRadmin_View_Trainerattendance(request,id):
    if 'Adm_id' in request.session:
        if request.session.has_key('Adm_id'):
            Adm_id = request.session['Adm_id']
        else:
            return redirect('/')
        Adm = user_registration.objects.filter(id=Adm_id)
        usr=user_registration.objects.get(id=id)
        return render(request,'BRadmin_View_Trainerattendance.html', {'Adm':Adm,'user_registration':usr})
    else:
        return redirect('/')

def BRadmin_ViewTrainerattendancesort(request,id):
    if 'Adm_id' in request.session:
        if request.session.has_key('Adm_id'):
            Adm_id = request.session['Adm_id']
        else:
            return redirect('/')
        Adm = user_registration.objects.filter(id=Adm_id)
        usr=user_registration.objects.get(id=id)
        if request.method == "POST":
            fromdate = request.POST.get('fromdate')
            todate = request.POST.get('todate') 
            adata =attendance.objects.filter(date__range=[fromdate,todate]).filter(user_id=id)
        return render(request,'BRadmin_View_Trainerattendanceview.html',{'Adm':Adm,'adata':adata,'user_registration':usr})
    else:
        return redirect('/')

def BRadmin_ViewCurrenttraineeattendancesort(request,id):
    if 'Adm_id' in request.session:
        if request.session.has_key('Adm_id'):
            Adm_id = request.session['Adm_id']
        else:
            return redirect('/')
        Adm = user_registration.objects.filter(id=Adm_id)
        usr=user_registration.objects.get(id=id)
        if request.method == "POST":
            fromdate = request.POST.get('fromdate')
            todate = request.POST.get('todate') 
            adata =attendance.objects.filter(date__range=[fromdate,todate]).filter(user_id=id)
        return render(request,'BRadmin_View_Currenttraineeattendanceview.html',{'Adm':Adm,'adata':adata,'user_registration':usr})
    else:
        return redirect('/')

def BRadmin_ViewPrevioustraineeattendancesort(request,id):
    if 'Adm_id' in request.session:
        if request.session.has_key('Adm_id'):
            Adm_id = request.session['Adm_id']
        else:
            return redirect('/')
        Adm = user_registration.objects.filter(id=Adm_id)
        usr=user_registration.objects.get(id=id)
        if request.method == "POST":
            fromdate = request.POST.get('fromdate')
            todate = request.POST.get('todate') 
            adata = attendance.objects.filter(date__range=[fromdate,todate]).filter(user_id=id)
        return render(request,'BRadmin_View_Previoustraineeattendanceview.html',{'Adm':Adm,'adata':adata,'user_registration':usr})
    else:
        return redirect('/')

def admin_page1(request):
    if 'Adm_id' in request.session:
        if request.session.has_key('Adm_id'):
                Adm_id = request.session['Adm_id']
        else:
            return redirect('/')
        Adm = user_registration.objects.filter(id=Adm_id)
        if request.method == "POST":
            empname1=request.POST.get('empname')
            atten=attendance.objects.filter(user_id=empname1)
            return render(request,'BRadmin_attendanceshow.html',{'Adm':Adm,'atten':atten,'empname1':empname1}) 
        dpt=department.objects.all()
        dsg=designation.objects.all()
        userreg=user_registration.objects.all()
        return render(request,'BRadmin_attendance.html', {'Adm':Adm,'department':dpt,'designation':dsg,'user_registration':userreg})  
    else:
        return redirect('/')

def admin_page3(request):
    if 'Adm_id' in request.session:
        if request.session.has_key('Adm_id'):
            Adm_id = request.session['Adm_id']
        else:
            return redirect('/')
        Adm = user_registration.objects.filter(id=Adm_id)
        
        return render(request,'BRadmin_attendanceshow.html',{'Adm':Adm}) 
    else:
        return redirect('/')

def admin_desi(request):   
    dept_id = request.GET.get('dept_id')
    departments=department.objects.all()
    Desig = designation.objects.all()
    return render(request, 'BRadmin_designation.html', {'Desig': Desig,'departments':departments})

def admin_emp(request):   
    dept_id = request.GET.get('dept_id')
    desig_id = request.GET.get('desig_id')
    dept=department.objects.filter(id=dept_id)
    desi=designation.objects        .filter(id=desig_id)
    user=user_registration.objects.filter(designation_id=desig_id).filter(department_id=dept_id)
    print(dept)
    print(desi)
    return render(request, 'BRadmin_employee.html',{'user':user,'dept':dept,'desi':desi})

def MAN_View_Trainers(request,id,did):
    if 'm_id' in request.session:
        if request.session.has_key('m_id'):
            m_id = request.session['m_id']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(id=m_id)
        projectname=project.objects.all()
        trainer=designation.objects.get(id=id)
        userreg=user_registration.objects.filter(designation=trainer).filter(department=did).order_by("-id")
        return render(request,'MAN_View_Trainers.html', {'mem':mem,'user_registration':userreg, 'project':projectname})
    else:
        return redirect('/')

def MAN_View_Trainerprofile(request,id):
    if 'm_id' in request.session:
        if request.session.has_key('m_id'):
            m_id = request.session['m_id']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(id=m_id)
        userreg=user_registration.objects.get(id=id)
        return render(request,'MAN_View_Trainerprofile.html', {'mem':mem,'user_registration':userreg})
    else:
        return redirect('/')

def MAN_View_Currenttraineesoftrainer(request,id):
    if 'm_id' in request.session:
        if request.session.has_key('m_id'):
            m_id = request.session['m_id']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(id=m_id)
       
        user=user_registration.objects.filter(id=id)
        trainee=designation.objects.get(designation='Trainee')
        user2=user_registration.objects.filter(designation=trainee)
        return render(request,'MAN_View_Currenttraineesoftrainer.html',{'mem':mem,'user_registration':user,'user_registration2':user2})
    else:
        return redirect('/')
        
def MAN_View_Previoustraineesoftrainer(request,id):
    if 'm_id' in request.session:
        if request.session.has_key('m_id'):
            m_id = request.session['m_id']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(id=m_id)
       
        user=user_registration.objects.filter(id=id)
        trainee=designation.objects.get(designation='Trainee')
        user2=user_registration.objects.filter(designation=trainee)
        return render(request,'MAN_View_Previoustraineesoftrainer.html',{'mem':mem,'user_registration':user,'user_registration2':user2})
    else:
        return redirect('/')
        
def MAN_View_Currenttraineeprofile(request,id):
    if 'm_id' in request.session:
        if request.session.has_key('m_id'):
            m_id = request.session['m_id']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(id=m_id)
        userreg=user_registration.objects.get(id=id)
        return render(request,'MAN_View_Currenttraineeprofile.html', {'mem':mem,'user_registration':userreg})
    else:
        return redirect('/')

def MAN_View_Currenttraineetasks(request,id):
    if 'm_id' in request.session:
        if request.session.has_key('m_id'):
            m_id = request.session['m_id']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(id=m_id)
        # user=user_registration.objects.get(id=id)
        tasks=trainer_task.objects.filter(user=id)
        return render(request,'MAN_View_Currenttraineetasks.html',{'mem':mem,'trainer_task':tasks})
    else:
        return redirect('/')

def MAN_View_Currenttraineeattendance(request,id):
    if 'm_id' in request.session:
        if request.session.has_key('m_id'):
            m_id = request.session['m_id']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(id=m_id)
        usr=user_registration.objects.get(id=id)
        return render(request,'MAN_View_Currenttraineeattendance.html', {'mem':mem,'user_registration':usr})
    else:
        return redirect('/')

def MAN_View_Previoustraineeprofile(request,id):
    if 'm_id' in request.session:
        if request.session.has_key('m_id'):
            m_id = request.session['m_id']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(id=m_id)
        usr=user_registration.objects.get(id=id)
        return render(request,'MAN_View_Previoustraineeprofile.html', {'mem':mem,'user_registration':usr})
    else:
        return redirect('/')

def MAN_View_Previoustraineetasks(request,id):
    if 'm_id' in request.session:
        if request.session.has_key('m_id'):
            m_id = request.session['m_id']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(id=m_id)
        user=user_registration.objects.get(id=id)
        tasks=trainer_task.objects.filter(user=user)
        return render(request,'MAN_View_Previoustraineetasks.html',{'mem':mem,'trainer_task':tasks})
    else:
        return redirect('/')

def MAN_View_Previoustraineeattendance(request,id):
    if 'm_id' in request.session:
        if request.session.has_key('m_id'):
            m_id = request.session['m_id']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(id=m_id)
        usr=user_registration.objects.get(id=id)
        return render(request,'MAN_View_Previoustraineeattendance.html', {'mem':mem,'user_registration':usr})
    else:
        return redirect('/')

def MAN_View_Trainerattendance(request,id):
    if 'm_id' in request.session:
        if request.session.has_key('m_id'):
            m_id = request.session['m_id']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(id=m_id)
        usr=user_registration.objects.get(id=id)
        return render(request,'MAN_View_Trainerattendance.html', {'mem':mem,'user_registration':usr})
    else:
        return redirect('/')

def MAN_ViewTrainerattendancesort(request,id):
    if 'm_id' in request.session:
        if request.session.has_key('m_id'):
            m_id = request.session['m_id']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(id=m_id)
        usr=user_registration.objects.get(id=id)
        if request.method == "POST":
            fromdate = request.POST.get('fromdate')
            todate = request.POST.get('todate') 
            adata =attendance.objects.filter(date__range=[fromdate,todate]).filter(user_id=id)
        return render(request,'MAN_View_Trainerattendanceview.html',{'mem':mem,'adata':adata,'user_registration':usr})
    else:
        return redirect('/')

def MAN_ViewCurrenttraineeattendancesort(request,id):
    if 'm_id' in request.session:
        if request.session.has_key('m_id'):
            m_id = request.session['m_id']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(id=m_id)
        usr=user_registration.objects.get(id=id)
        if request.method == "POST":
            fromdate = request.POST.get('fromdate')
            todate = request.POST.get('todate') 
            adata =attendance.objects.filter(date__range=[fromdate,todate]).filter(user_id=id)
        return render(request,'MAN_View_Currenttraineeattendanceview.html',{'mem':mem,'adata':adata,'user_registration':usr})
    else:
        return redirect('/')

def MAN_ViewPrevioustraineeattendancesort(request,id):
    if 'm_id' in request.session:
        if request.session.has_key('m_id'):
            m_id = request.session['m_id']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(id=m_id)
        usr=user_registration.objects.get(id=id)
        if request.method == "POST":
            fromdate = request.POST.get('fromdate')
            todate = request.POST.get('todate') 
            adata = attendance.objects.filter(date__range=[fromdate,todate]).filter(user_id=id)
        return render(request,'MAN_View_Previoustraineeattendanceview.html',{'mem':mem,'adata':adata,'user_registration':usr})
    else:
        return redirect('/')

def MAN_dev_attendance(request):
    if 'm_id' in request.session:
        if request.session.has_key('m_id'):
            m_id = request.session['m_id']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(id=m_id)
        return render(request,'MAN_dev_attendance.html') 
    else:
        return redirect('/')
       

def man_page1(request):
    if 'm_id' in request.session:
        if request.session.has_key('m_id'):
            m_id = request.session['m_id']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(id=m_id)
        if request.method == "POST":
            empname1=request.POST.get('empname')
            atten=attendance.objects.filter(user_id=empname1)
            return render(request,'MAN_attendanceshow.html',{'mem':mem,'atten':atten,'empname1':empname1}) 
        dpt=department.objects.all()
        dsg=designation.objects.all()
        userreg=user_registration.objects.all()
        return render(request,'MAN_attendance.html', {'mem':mem,'department':dpt,'designation':dsg,'user_registration':userreg}) 
    else:
        return redirect('/')

def man_page3(request):
    if 'm_id' in request.session:
        if request.session.has_key('m_id'):
            m_id = request.session['m_id']
        else:
            return redirect('/')
        # mem = user_registration.objects.filter(id=m_id)
        
        
        return render(request,'MAN_attendanceshow.html') 
    else:
        return redirect('/')
   
def man_desi(request):   
    dept_id = request.GET.get('dept_id')
    departments=department.objects.all()
    Desig = designation.objects.filter( ~Q(designation="admin"), ~Q(designation="manager"))
    return render(request, 'MAN_designation.html', {'Desig': Desig,'departments':departments})


def man_emp(request):   
    dept_id = request.GET.get('dept_id')
    desig_id = request.GET.get('desig_id')
    dept=department.objects.filter(id=dept_id)
    desi=designation.objects.filter(id=desig_id)
    user=user_registration.objects.filter(designation_id=desig_id).filter(department_id=dept_id)
    print(dept)
    print(desi)
    return render(request, 'MAN_employee.html',{'user':user,'dept':dept,'desi':desi})

# ************************  anwar end  *********************************************


 # current projects- sharon
def BRadmin_pythons(request):
    if 'Adm_id' in request.session:
        if request.session.has_key('Adm_id'):
            Adm_id = request.session['Adm_id']
        else:
            return redirect('/')
        Adm = user_registration.objects.filter(id=Adm_id)
        project_details = project.objects.all()
        return render(request,'BRadmin_projects.html',{'proj_det':project_details,'Adm':Adm})
    else:
        return redirect('/')

def BRadmin_dept(request):
    if 'Adm_id' in request.session:
        if request.session.has_key('Adm_id'):
            Adm_id = request.session['Adm_id']
        else:
            return redirect('/')
        Adm = user_registration.objects.filter(id=Adm_id)
        project_details = project.objects.all()
        depart =department.objects.all()
        return render(request,'BRadmin_dept.html',{'proj_det':project_details,'department':depart,'Adm':Adm})
    else:
        return redirect('/')
    
# def BRadmin_profiledash(request):
#     Num= project.objects.count()
#     project_details = project.objects.all()
#     return render(request,'BRadmin_profiledash.html',{'proj_det':project_details,'num':Num})

def BRadmin_projects(request,id):
    if 'Adm_id' in request.session:
        if request.session.has_key('Adm_id'):
            Adm_id = request.session['Adm_id']
        else:
            return redirect('/')
        Adm = user_registration.objects.filter(id=Adm_id)
        Num= project.objects.filter(~Q(status='Completed'),~Q(status='Rejected')).filter(department=id).count()
        num= project.objects.filter(status='Completed').filter(department=id).count()
        project_details = project.objects.all()
        depart =department.objects.get(id=id)
        id=id
        return render(request,'BRadmin_projects.html',{'proj_det':project_details,'num':Num,'Num':num,'department':depart,'id':id,'Adm':Adm})
    else:
        return redirect('/')

def BRadmin_proj_list(request,id):
    if 'Adm_id' in request.session:
        if request.session.has_key('Adm_id'):
            Adm_id = request.session['Adm_id']
        else:
            return redirect('/')
        Adm = user_registration.objects.filter(id=Adm_id)
        project_details = project.objects.filter(~Q(status='Completed'),department_id=id)
        return render(request,'BRadmin_proj_list.html',{'proj_det':project_details,'Adm':Adm})
    else:
        return redirect('/')

def BRadmin_proj_det(request,id):
    if 'Adm_id' in request.session:
        if request.session.has_key('Adm_id'):
            Adm_id = request.session['Adm_id']
        else:
            return redirect('/')
        Adm = user_registration.objects.filter(id=Adm_id)
        project_details = project.objects.get(id=id)
        return render(request,'BRadmin_proj_det.html',{'proj_det':project_details,'Adm':Adm})
    else:
        return redirect('/')

def BRadmin_proj_mngrs(request,id):
    if 'Adm_id' in request.session:
        if request.session.has_key('Adm_id'):
            Adm_id = request.session['Adm_id']
        else:
            return redirect('/')
        Adm = user_registration.objects.filter(id=Adm_id)
        project_details = project.objects.get(id=id)
        return render(request,'BRadmin_proj_mngrs.html',{'proj_det':project_details,'Adm':Adm})
    else:
        return redirect('/')

def BRadmin_proj_mangrs1(request,id):
    if 'Adm_id' in request.session:
        if request.session.has_key('Adm_id'):
            Adm_id = request.session['Adm_id']
        else:
            return redirect('/')
        Adm = user_registration.objects.filter(id=Adm_id)
        project_details = project.objects.get(id=id) 
        proj1=project_details.projectmanager_id
        dept_id=project_details.department_id
        user_det=user_registration.objects.filter(id=proj1)
        return render(request,'BRadmin_proj_mangrs1.html',{'proj1':proj1,'user_det':user_det,'proj_det':project_details,'Adm':Adm})
    else:
        return redirect('/')

def BRadmin_proj_mangrs2(request,id):
    if 'Adm_id' in request.session:
        if request.session.has_key('Adm_id'):
            Adm_id = request.session['Adm_id']
        else:
            return redirect('/')
        Adm = user_registration.objects.filter(id=Adm_id)
        project_details = project_taskassign.objects.filter(project_id=id)
        # proj1=project_details.designation_id
        # dept_id=project_details.department_id
        # user_det=user_registration.objects.filter(designation_id=proj1).order_by("-id")
        return render(request,'BRadmin_proj_mangrs2.html',{'project_details':project_details,'Adm':Adm})
    else:
        return redirect('/')

def BRadmin_daily_report(request,id):
    if 'Adm_id' in request.session:
        if request.session.has_key('Adm_id'):
            Adm_id = request.session['Adm_id']
        else:
            return redirect('/')
        Adm = user_registration.objects.filter(id=Adm_id) 
        proj_name =  project_taskassign.objects.all()
        tester_name = user_registration.objects.all()
        tester = tester_status.objects.filter(user_id=id)
        return render(request,'BRadmin_daily_report.html',{'Adm':Adm,'test':tester, 'tester_name':tester_name, 'proj_name':proj_name})
    else:
        return redirect('/')

def BRadmin_developers(request,id):
    if 'Adm_id' in request.session:
        if request.session.has_key('Adm_id'):
            Adm_id = request.session['Adm_id']
        else:
            return redirect('/')
        Adm = user_registration.objects.filter(id=Adm_id)
        project_details = project.objects.filter(id=id)
        project_task = project_taskassign.objects.filter(project_id = project_details).filter(tl_id=id)
        user_det=user_registration.objects.filter(tl_id=id).order_by("-id")
        progress_bar= tester_status.objects.all()
        return render(request,'BRadmin_developers.html',{'Adm':Adm,'proj_task':project_task,'proj_det':project_details,'prog_status':progress_bar,'user_det':user_det})
    else:
        return redirect('/')

# completed projects- subeesh
 
def BRadmin_proj_cmpltd_new(request, id):
    if 'Adm_id' in request.session:
        if request.session.has_key('Adm_id'):
            Adm_id = request.session['Adm_id']
        else:
            return redirect('/')
        Adm = user_registration.objects.filter(id=Adm_id)
        project_details=project.objects.filter(department=id)
        print (project_details.count())
        return render(request,'BRadmin_proj_cmpltd_show.html',{'project': project_details,'Adm':Adm})
    else:
        return redirect('/')

def BRadmin_cmpltd_proj_det_new(request, id):
    if 'Adm_id' in request.session:
        if request.session.has_key('Adm_id'):
            Adm_id = request.session['Adm_id']
        else:
            return redirect('/')
        Adm = user_registration.objects.filter(id=Adm_id)
        project_details = project.objects.get(id=id)
        return render(request,'BRadmin_cmpltd_proj_det_show.html',{'project': project_details,'Adm':Adm})
    else:
        return redirect('/')

def BRadmin_proj_mngrs_new(request, id):
    if 'Adm_id' in request.session:
        if request.session.has_key('Adm_id'):
            Adm_id = request.session['Adm_id']
        else:
            return redirect('/')
        Adm = user_registration.objects.filter(id=Adm_id)
        project_details = project.objects.get(id=id)
        return render(request,'BRadmin_proj_mngrs_show.html', {'project': project_details,'Adm':Adm})
    else:
        return redirect('/')

def BRadmin_proj_mangrs1_new(request,id):
    if 'Adm_id' in request.session:
        if request.session.has_key('Adm_id'):
            Adm_id = request.session['Adm_id']
        else:
            return redirect('/')
        Adm = user_registration.objects.filter(id=Adm_id)
        project_details = project.objects.get(id=id) 
        proj1=project_details.projectmanager_id
        dept_id=project_details.department_id
        user_det=user_registration.objects.filter(id=proj1).order_by("-id")
        return render(request,'BRadmin_proj_mangrs1_show.html',{'proj1':proj1,'user_det':user_det,'proj_det':project_details,'Adm':Adm})
        
    else:
        return redirect('/')

def BRadmin_proj_mangrs2_new(request, id):
    if 'Adm_id' in request.session:
        if request.session.has_key('Adm_id'):
            Adm_id = request.session['Adm_id']
        else:
            return redirect('/')
        Adm = user_registration.objects.filter(id=Adm_id)
        project_details = project.objects.get(id=id) 
        proj1=project_details.designation_id
        dept_id=project_details.department_id
        user_det=user_registration.objects.filter(designation_id=proj1).order_by("-id")
        return render(request,'BRadmin_proj_mangrs2_show.html',{'proj1':proj1,'user_det':user_det,'proj_det':project_details,'Adm':Adm})
        
    else:
        return redirect('/')

def BRadmin_developers_new(request, id):
    if 'Adm_id' in request.session:
        if request.session.has_key('Adm_id'):
            Adm_id = request.session['Adm_id']
        else:
            return redirect('/')
        Adm = user_registration.objects.filter(id=Adm_id)
        project_details = project.objects.get(id=id)
        project_task = project_taskassign.objects.filter(tl_id = id)
        progress_bar= tester_status.objects.all()
        return render(request,'BRadmin_developers_show.html', {'project':project_details,'project_taskassign':project_task,'prog_status':progress_bar,'Adm':Adm})
    else:
        return redirect('/')

def BRadmin_daily_report_new(request, id):
    if 'Adm_id' in request.session:
        if request.session.has_key('Adm_id'):
            Adm_id = request.session['Adm_id']
        else:
            return redirect('/')
        Adm = user_registration.objects.filter(id=Adm_id)
        project_task = project_taskassign.objects.get(user_id=id)
        tester = tester_status.objects.all()
        return render(request,'BRadmin_daily_report_show.html', {'project':project_task,'tester_status':tester,'Adm':Adm})
    else:
        return redirect('/')

 # current projects-sharon -manager module
def MAN_pythons(request):
    if 'm_id' in request.session:
        if request.session.has_key('m_id'):
            m_id = request.session['m_id']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(id=m_id)
        project_details = project.objects.all()
        return render(request,'MAN_projects.html',{'proj_det':project_details,'mem':mem})
    else:
        return redirect('/')

def MAN_dept(request):
    if 'm_id' in request.session:
        if request.session.has_key('m_id'):
            m_id = request.session['m_id']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(id=m_id)
        project_details = project.objects.all()
        depart =department.objects.all()
        return render(request,'MAN_dept.html',{'proj_det':project_details,'department':depart,'mem':mem})
    else:
        return redirect('/')
    
# def MAN_profiledash(request):
#     Num= project.objects.count()
#     project_details = project.objects.all()
#     return render(request,'MAN_profiledash.html',{'proj_det':project_details,'num':Num})

def MAN_projects(request,id):
    if 'm_id' in request.session:
        if request.session.has_key('m_id'):
            m_id = request.session['m_id']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(id=m_id)
        Num= project.objects.filter(status='accepted').filter(department=id).count()
        num= project.objects.filter(status='completed').filter(department=id).count()
        project_details = project.objects.all()
        depart =department.objects.get(id=id)
        id=id
        return render(request,'MAN_projects.html',{'proj_det':project_details,'num':Num,'Num':num,'department':depart,'id':id,'mem':mem})
    else:
        return redirect('/')

def MAN_proj_list(request,id):
    if 'm_id' in request.session:
        if request.session.has_key('m_id'):
            m_id = request.session['m_id']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(id=m_id)
        project_details = project.objects.filter(department=id)
        print (project_details.count())
        return render(request,'MAN_proj_list.html',{'proj_det':project_details,'mem':mem})
    else:
        return redirect('/')

def MAN_proj_det(request,id):
    if 'm_id' in request.session:
        if request.session.has_key('m_id'):
            m_id = request.session['m_id']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(id=m_id)
        project_details = project.objects.get(id=id)
        return render(request,'MAN_proj_det.html',{'proj_det':project_details,'mem':mem})
    else:
        return redirect('/')

def MAN_proj_mngrs(request,id):
    if 'm_id' in request.session:
        if request.session.has_key('m_id'):
            m_id = request.session['m_id']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(id=m_id)
        project_details = project.objects.get(id=id)
        return render(request,'MAN_proj_mngrs.html',{'proj_det':project_details,'mem':mem})
    else:
        return redirect('/')

def MAN_proj_mangrs1(request,id):
    if 'm_id' in request.session:
        if request.session.has_key('m_id'):
            m_id = request.session['m_id']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(id=m_id)
        project_details = project.objects.get(id=id) 
        proj1=project_details.projectmanager_id
        dept_id=project_details.department_id
        user_det=user_registration.objects.filter(id=proj1)
        return render(request,'MAN_proj_mangrs1.html',{'user_det':user_det,'proj_det':project_details,'mem':mem,'proj1':proj1})
    else:
        return redirect('/')

def MAN_proj_mangrs2(request,id):
    if 'm_id' in request.session:
        if request.session.has_key('m_id'):
            m_id = request.session['m_id']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(id=m_id)
        project_details = project.objects.get(id=id) 
        proj1=project_details.designation_id
        dept_id=project_details.department_id
        user_det=user_registration.objects.filter(designation_id=proj1).order_by("-id")
        return render(request,'MAN_proj_mangrs2.html',{'user_det':user_det,'proj_det':project_details,'mem':mem,'proj1':proj1})
    else:
        return redirect('/')

def MAN_daily_report(request,id): 
    if 'm_id' in request.session:
        if request.session.has_key('m_id'):
            m_id = request.session['m_id']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(id=m_id)
        proj_name =  project_taskassign.objects.all()
        tester_name = user_registration.objects.all()
        tester = tester_status.objects.filter(user_id=id)
        return render(request,'MAN_daily_report.html',{'proj_name':proj_name,'test':tester,'mem':mem,'tester_name':tester_name})
    else:
        return redirect('/')

def MAN_developers(request,id):
    if 'm_id' in request.session:
        if request.session.has_key('m_id'):
            m_id = request.session['m_id']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(id=m_id)
        project_details = project.objects.filter(id=id) 
        project_task = project_taskassign.objects.filter(project_id = project_details).filter(tl_id = id)
        user_det=user_registration.objects.filter(tl_id=id).order_by("-id")
        progress_bar= tester_status.objects.all()
        return render(request,'MAN_developers.html',{'user_det':user_det,'proj_task':project_task,'proj_det':project_details,'prog_status':progress_bar,'mem':mem})
    else:
        return redirect('/')

# completed projects- subeesh -manager module
  
def MAN_proj_cmpltd_new(request, id):
    if 'm_id' in request.session:
        if request.session.has_key('m_id'):
            m_id = request.session['m_id']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(id=m_id)
        project_details=project.objects.filter(department=id)
        print (project_details.count())
        return render(request,'MAN_proj_cmpltd_show.html',{'project': project_details,'mem':mem})
    else:
        return redirect('/')

def MAN_cmpltd_proj_det_new(request, id):
    if 'm_id' in request.session:
        if request.session.has_key('m_id'):
            m_id = request.session['m_id']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(id=m_id)
        project_details = project.objects.get(id=id)
        return render(request,'MAN_cmpltd_proj_det_show.html',{'project': project_details,'mem':mem})
    else:
        return redirect('/')

def MAN_proj_mngrs_new(request, id):
    if 'm_id' in request.session:
        if request.session.has_key('m_id'):
            m_id = request.session['m_id']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(id=m_id)
        project_details = project.objects.get(id=id)
        return render(request,'MAN_proj_mngrs_show.html', {'project': project_details,'mem':mem})
    else:
        return redirect('/')

def MAN_proj_mangrs1_new(request,id):
    if 'm_id' in request.session:
        if request.session.has_key('m_id'):
            m_id = request.session['m_id']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(id=m_id)
        project_details = project.objects.get(id=id) 
        proj1=project_details.projectmanager_id
        dept_id=project_details.department_id
        user_det=user_registration.objects.filter(id=proj1).order_by("-id")
        return render(request,'MAN_proj_mangrs1_show.html',{'proj1':proj1,'user_det':user_det,'proj_det':project_details,'mem':mem})
        
    else:
        return redirect('/')

def MAN_proj_mangrs2_new(request, id):
    if 'm_id' in request.session:
        if request.session.has_key('m_id'):
            m_id = request.session['m_id']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(id=m_id)
        project_details = project.objects.get(id=id) 
        proj1=project_details.designation_id
        dept_id=project_details.department_id
        user_det=user_registration.objects.filter(designation_id=proj1).order_by("-id")
        return render(request,'MAN_proj_mangrs2_show.html',{'proj1':proj1,'user_det':user_det,'proj_det':project_details,'mem':mem})
        
    else:
        return redirect('/')

def MAN_developers_new(request, id):
    if 'm_id' in request.session:
        if request.session.has_key('m_id'):
            m_id = request.session['m_id']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(id=m_id)
        project_details = project.objects.get(id=id)
        project_task = project_taskassign.objects.filter(tl_id = id)
        progress_bar= tester_status.objects.all()
        return render(request,'MAN_developers_show.html', {'project':project_details,'project_taskassign':project_task,'prog_status':progress_bar,'mem':mem})
    else:
        return redirect('/')

def MAN_daily_report_new(request, id):
    if 'm_id' in request.session:
        if request.session.has_key('m_id'):
            m_id = request.session['m_id']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(id=m_id)
        project_task = project_taskassign.objects.get(user_id=id)
        tester = tester_status.objects.all()
        return render(request,'MAN_daily_report_show.html', {'project':project_task,'tester_status':tester,'mem':mem})
    else:
        return redirect('/')
        
def MAN_training_department(request):
    if 'm_id' in request.session:
        if request.session.has_key('m_id'):
            m_id = request.session['m_id']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(id=m_id)
        departments=department.objects.all()
        return render(request, 'MAN_training_department.html',{'department':departments,'mem':mem})
    else:
        return redirect('/')
############## end ##########


# reported issue- akhil-admin mod

def BRadmin_Reportedissue_department(request):
    if 'Adm_id' in request.session:
        if request.session.has_key('Adm_id'):
            Adm_id = request.session['Adm_id']
        else:
            return redirect('/')
        Adm = user_registration.objects.filter(id=Adm_id)
        departments=department.objects.all()
        return render(request, 'BRadmin_Reportedissue_department.html',{'department':departments,'Adm':Adm})
    else:
        return redirect('/')

def BRadmin_Reportedissue(request,id):
    if 'Adm_id' in request.session:
        if request.session.has_key('Adm_id'):
            Adm_id = request.session['Adm_id']
        else:
            return redirect('/')
        Adm = user_registration.objects.filter(id=Adm_id)
        departments=department.objects.get(id=id)
        deptid=id
        designations=designation.objects.filter(~Q(designation="admin"))
        return render(request, 'BRadmin_Reportedissue.html',{'Adm':Adm,'department':departments,'designation':designations,'dept_id':deptid})
    else:
        return redirect('/')

def BRadmin_ReportedissueShow(request,id,did):
    if 'Adm_id' in request.session:
        if request.session.has_key('Adm_id'):
            Adm_id = request.session['Adm_id']
        else:
            return redirect('/')
        Adm = user_registration.objects.filter(id=Adm_id)
        reported_issues=reported_issue.objects.all()
        designations=designation.objects.get(id=id)
        user=user_registration.objects.filter(designation=designations).filter(department=did).order_by("-id")
        return render(request,'BRadmin_ReportedissueShow.html',{'Adm':Adm,'designation':designations,'reported_issue':reported_issues,'user_registration':user})
    else:
        return redirect('/')

def BRadmin_ReportedissueShow1(request,id):
    if 'Adm_id' in request.session:
        if request.session.has_key('Adm_id'):
            Adm_id = request.session['Adm_id']
        else:
            return redirect('/')
        Adm = user_registration.objects.filter(id=Adm_id)
        reported_issues=reported_issue.objects.get(id=id)
        return render(request,'BRadmin_ReportedissueShow1.html',{'reported_issue':reported_issues,'Adm':Adm})
    else:
        return redirect('/')

# reported issue- akhil-man mod

def MAN_Reportedissue_department(request):
    if 'm_id' in request.session:
        if request.session.has_key('m_id'):
            m_id = request.session['m_id']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(id=m_id)
        departments=department.objects.all()
        return render(request, 'MAN_Reportedissue_department.html',{'department':departments,'mem':mem})
    else:
        return redirect('/')

def MAN_Reportedissue(request,id):
    if 'm_id' in request.session:
        if request.session.has_key('m_id'):
            m_id = request.session['m_id']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(id=m_id)
        departments=department.objects.get(id=id)
        deptid=id
        designations=designation.objects.filter(~Q(designation='admin'),~Q(designation='manager'))
        return render(request, 'MAN_Reportedissue.html',{'mem':mem,'department':departments,'designation':designations,'dept_id':deptid})
    else:
        return redirect('/')

def MAN_ReportedissueShow(request,id,did):
    if 'm_id' in request.session:
        if request.session.has_key('m_id'):
            m_id = request.session['m_id']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(id=m_id)
        reported_issues=reported_issue.objects.all()
        designations=designation.objects.get(id=id)
        user=user_registration.objects.filter(designation=designations).filter(department=did).order_by("-id")
        return render(request,'MAN_ReportedissueShow.html',{'mem':mem,'designation':designations,'reported_issue':reported_issues,'user_registration':user})
    else:
        return redirect('/')


def MAN_reported(request,id):
        
        if request.method == 'POST':
            vars = reported_issue.objects.get(id=id)
            
            print(vars.reply)
            vars.reply = request.POST['review']
            
            vars.issuestatus = 1
           
            
            vars.save()
        return redirect('MAN_Reportedissue_department')

def MAN_ReportedissueShow1(request,id):
    if 'm_id' in request.session:
        if request.session.has_key('m_id'):
            m_id = request.session['m_id']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(id=m_id)
        reported_issues=reported_issue.objects.get(id=id)
        return render(request,'MAN_ReportedissueShow1.html',{'reported_issue':reported_issues,'mem':mem}) 
    else:
        return redirect('/')

############## end ##########


# task section-nimisha- man mod

def MAN_tasks(request):
    if 'm_id' in request.session:
        if request.session.has_key('m_id'):
            m_id = request.session['m_id']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(id=m_id)
        return render(request,'MAN_tasks.html',{'mem':mem})
    else:
        return redirect('/')

def MAN_givetask(request):
    if 'm_id' in request.session:
        if request.session.has_key('m_id'):
            m_id = request.session['m_id']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(id=m_id)
        if request.method == 'POST':
            sc1 = request.POST['Department']
            sc2 = request.POST['designation']
            sc3 = request.POST['projectname']
            sc4 = request.POST['task']
            sc7 = request.POST['discrip']
            sc5 = request.POST['start']
            sc6 = request.POST['end']
            ogo = request.FILES['img[]']
            print(sc1,sc2)
            catry = tasks(tasks=sc4,files=ogo,description=sc7,startdate=sc5, enddate=sc6,department_id = sc1,designation_id = sc2,user_id = sc3)
            catry.save()
        dept = department.objects.all()
        desig = designation.objects.all()
        proj = project.objects.all()
        emp = user_registration.objects.all()
        return render(request,'MAN_givetask.html',{'desig':desig,'dept':dept,'project':proj,'emp':emp,'mem':mem})
    else:
        return redirect('/')

def MAN_taskdesignation(request):
    if 'm_id' in request.session:
        if request.session.has_key('m_id'):
            m_id = request.session['m_id']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(id=m_id)   
        dept_id = request.GET.get('dept_id')
        Desig = designation.objects.all()
        print(Desig)
        return render(request, 'MAN_taskdesignation.html', {'Desig': Desig,'mem':mem})
    else:
        return redirect('/')

def MAN_taskemployee(request):   
    if 'm_id' in request.session:
        if request.session.has_key('m_id'):
            m_id = request.session['m_id']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(id=m_id)
        dept_id = request.GET.get('dept_id')
        desig_id = request.GET.get('desig_id')
        emp = user_registration.objects.filter(designation_id=desig_id).filter(department_id=dept_id)
        print(emp)
        return render(request, 'MAN_taskemployee.html', {'emp': emp,'mem':mem})
    else:
        return redirect('/')
        
def MAN_currenttasks(request):
    if 'm_id' in request.session:
        if request.session.has_key('m_id'):
            m_id = request.session['m_id']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(id=m_id)  
        names =tasks.objects.all().order_by("-id")
        return render(request,'MAN_currenttask.html',{'names': names,'mem':mem})
    else:
        return redirect('/')

def MAN_previoustasks(request):
    if 'm_id' in request.session:
        if request.session.has_key('m_id'):
            m_id = request.session['m_id']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(id=m_id)  
        names =tasks.objects.all().order_by("-id")
        return render(request,'MAN_previoustasks.html',{'names': names,'mem':mem})
    else:
        return redirect('/')

# task section-nimisha- admin mod

def BRadmin_tasks(request):
    if 'Adm_id' in request.session:
        if request.session.has_key('Adm_id'):
            Adm_id = request.session['Adm_id']
        else:
            return redirect('/')
        Adm = user_registration.objects.filter(id=Adm_id)
        return render(request,'BRadmin_tasks.html',{'Adm':Adm})
    else:
        return redirect('/')

def BRadmin_givetask(request):
    if 'Adm_id' in request.session:
        if request.session.has_key('Adm_id'):
                Adm_id = request.session['Adm_id']
        else:
            return redirect('/')
        Adm = user_registration.objects.filter(id=Adm_id)
        if request.method == 'POST':
            sc1 = request.POST['Department']
            sc2 = request.POST['designation']
            sc3 = request.POST['projectname']
            sc4 = request.POST['task']
            sc7 = request.POST['discrip']
            sc5 = request.POST['start']
            sc6 = request.POST['end']
            ogo = request.FILES['img[]']
            print(sc4)
            catry = tasks(tasks=sc4,files=ogo,description=sc7,startdate=sc5, enddate=sc6,department_id = sc1,designation_id = sc2,user_id = sc3)
            catry.save()
        dept = department.objects.all()
        desig = designation.objects.all()
        proj = project.objects.all()
        emp = user_registration.objects.all()
        return render(request,'BRadmin_givetask.html',{'desig':desig,'dept':dept,'project':proj,'emp':emp,'Adm':Adm})
    else:
        return redirect('/')

def BRadmin_taskdesignation(request):  
     
    dept_id = request.GET.get('dept_id')
    # Desig = designation.objects.filter(department_id=dept_id)
    Desig = designation.objects.all()
    print(Desig)
    return render(request, 'BRadmin_taskdesignation.html', {'Desig': Desig,'Adm':Adm})
    

def BRadmin_taskemployee(request): 
      
    dept_id = request.GET.get('dept_id')
    desig_id = request.GET.get('desig_id')
    emp = user_registration.objects.filter(designation_id=desig_id).filter(department_id=dept_id)
    print(emp)
    return render(request, 'BRadmin_taskemployee.html', {'emp': emp,'Adm':Adm})
  

def BRadmin_currenttasks(request):
    if 'Adm_id' in request.session:
        if request.session.has_key('Adm_id'):
            Adm_id = request.session['Adm_id']
        else:
            return redirect('/')
        Adm = user_registration.objects.filter(id=Adm_id)  
        names =tasks.objects.filter(~Q(status=1)).order_by("-id")
        return render(request,'BRadmin_currenttask.html',{'names': names,'Adm':Adm})
    else:
        return redirect('/')

def BRadmin_previoustasks(request):
    if 'Adm_id' in request.session:
        if request.session.has_key('Adm_id'):
            Adm_id = request.session['Adm_id']
        else:
            return redirect('/')
        Adm = user_registration.objects.filter(id=Adm_id)  
        names =tasks.objects.filter(status=1).order_by("-id")
        return render(request,'BRadmin_previoustasks.html',{'names': names,'Adm':Adm})
    else:
        return redirect('/')

def BRadmin_trainersdepartment(request):
    if 'Adm_id' in request.session:
        if request.session.has_key('Adm_id'):
            Adm_id = request.session['Adm_id']
        else:
            return redirect('/')
        Adm = user_registration.objects.filter(id=Adm_id)
        Dept = department.objects.all()
        Desig = designation.objects.all()
        return render(request,'BRadmin_trainersdepartment.html',{'Adm':Adm,'Dept':Dept,'Desig':Desig})
    else:
        return redirect('/')

############## end ##########

# upcoming projects -safdhar -admin mod


def BRadmin_upcoming(request):
    if 'Adm_id' in request.session:
        if request.session.has_key('Adm_id'):
            Adm_id = request.session['Adm_id']
        else:
            return redirect('/')
        Adm = user_registration.objects.filter(id=Adm_id)
        return render(request,'BRadmin_upcomingprojects.html',{'Adm':Adm})
    else:
        return redirect('/')

def BRadmin_viewprojectform(request):
    if 'Adm_id' in request.session:
        if request.session.has_key('Adm_id'):
            Adm_id = request.session['Adm_id']
        else:
            return redirect('/')
        Adm = user_registration.objects.filter(id=Adm_id)
        dept = department.objects.all()
        desig = designation.objects.all()
        proj = project.objects.all()
        if request.method == 'POST':
            sc1 = request.POST['Department']
            sc2 = request.POST['designation']
            sc3 = request.POST['projectname']
            sc4 = request.POST['discrip']
            sc5 = request.POST['start']
            sc6 = request.POST['end']
            progress=0
            catry = project_taskassign(project_id=sc3,description=sc4,startdate=sc5, enddate=sc6,extension='0')
            catry.save()
        return render(request,'BRadmin_viewprojects.html',{'Adm':Adm,'desig':desig,'dept':dept,'project':proj})
    else:
        return redirect('/')

def BRadmin_acceptedprojects(request):
    if 'Adm_id' in request.session:
        if request.session.has_key('Adm_id'):
            Adm_id = request.session['Adm_id']
        else:
            return redirect('/')
        Adm = user_registration.objects.filter(id=Adm_id)
        pro =project.objects.filter(~Q(status='Rejected')).order_by("-id")
        return render(request,'BRadmin_acceptedprojects.html',{'Adm':Adm,'projects': pro})
    else:
        return redirect('/')

def BRadmin_rejected(request):
    if 'Adm_id' in request.session:
        if request.session.has_key('Adm_id'):
            Adm_id = request.session['Adm_id']
        else:
            return redirect('/')
        Adm = user_registration.objects.filter(id=Adm_id)
        pro =project.objects.filter(status='Rejected').order_by("-id")
        return render(request,'BRadmin_rejectedprojectes.html',{'Adm':Adm,'projects': pro})
    else:
        return redirect('/')

def BRadmin_createproject(request):
    if 'Adm_id' in request.session:
        if request.session.has_key('Adm_id'):
            Adm_id = request.session['Adm_id']
        else:
            return redirect('/')
        Adm = user_registration.objects.filter(id=Adm_id)  
        if request.method == 'POST':
            sc1 = request.POST['Department']
            sc2 = request.POST['designation']
            sc3 = request.POST['projectname']
            sc4 = request.POST['discrip']
            sc5 = request.POST['start']
            sc6 = request.POST['end']
            ogo = request.FILES['img[]']
            print(sc5,sc6,ogo,sc1)
            progress=0
            catry = project(designation_id=sc2,department_id=sc1,project=sc3,
                                      description=sc4,
                                      startdate=sc5, enddate=sc6, files=ogo,progress=progress)
            catry.save()
        dept = department.objects.all()
        desig = designation.objects.all()	
        return render(request,'BRadmin_createproject.html',{'Adm':Adm,'dept':dept,'desig':desig})
    else:
        return redirect('/')
        
def BRadmin_upcomingpro(request):
    if 'Adm_id' in request.session:
        if request.session.has_key('Adm_id'):
            Adm_id = request.session['Adm_id']
        else:
            return redirect('/')
        Adm = user_registration.objects.filter(id=Adm_id)
        pro =project.objects.all().order_by("-id")
        return render(request,'BRadmin_upcomingpro.html',{'Adm':Adm,'projects': pro})
    else:
        return redirect('/')

def BRadmin_seradmintraineedesi1(request):
    if 'Adm_id' in request.session:
        if request.session.has_key('Adm_id'):
            Adm_id = request.session['Adm_id']
        else:
            return redirect('/')
        Adm = user_registration.objects.filter(id=Adm_id)
        dept_id = request.GET.get('dept_id')
        Desig = designation.objects.filter(~Q(designation='admin'), ~Q(designation='manager'), ~Q(designation='account'))
        print(Desig)
        return render(request, 'BRadmin_dropdown.html', {'Desig': Desig,'Adm':Adm})
    else:
        return redirect('/')

def BRadmin_seradmindesig(request):
	print("safdhar")
	dept_id = request.GET.get('dept_id')
	Desig = designation.objects.filter(~Q(designation="admin"), ~Q(designation="manager"), ~Q(designation="account"))
	print(Desig)
	return render(request, 'BRadmin_giveprojectdropdown.html', {'Desig': Desig})
	
def BRadmin_selectproject(request):
    
    print("safdhar")
    dept_id = request.GET.get('dept_id')
    desig_id = request.GET.get('desig_id')
    print(desig_id,dept_id)
    proj = project.objects.filter(department_id=dept_id)
    print(proj)
    return render(request, 'BRadmin_selectproject.html',{'project':proj})
    
# upcoming projects -safdhar -man mod


def MAN_upcoming(request):
    if 'm_id' in request.session:
        if request.session.has_key('m_id'):
            m_id = request.session['m_id']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(id=m_id)
        return render(request,'MAN_upcomingprojects.html',{'mem':mem})
    else:
        return redirect('/')
        
def MAN_viewprojectform(request):
    if 'm_id' in request.session:
        if request.session.has_key('m_id'):
            m_id = request.session['m_id']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(id=m_id)
        dept = department.objects.all()
        desig = designation.objects.all()
        proj = project.objects.all()
        if request.method == 'POST':
            sc1 = request.POST['Department']
            sc2 = request.POST['designation']
            sc3 = request.POST['projectname']
            sc4 = request.POST['discrip']
            sc5 = request.POST['start']
            sc6 = request.POST['end']
            print(sc1,sc2)
            progress=0
            catry = project_taskassign(project_id=sc3,description=sc4,startdate=sc5,enddate=sc6,extension='0')
            catry.save()
        return render(request,'MAN_viewprojects.html',{'desig':desig,'dept':dept,'project':proj,'mem':mem})
    else:
        return redirect('/')

def MAN_acceptedprojects(request):
    if 'm_id' in request.session:
        if request.session.has_key('m_id'):
            m_id = request.session['m_id']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(id=m_id)
        pro = project.objects.filter(status='Accepted').order_by("-id")
        return render(request,'MAN_acceptedprojects.html',{'projects':pro,'mem':mem})
    else:
        return redirect('/')

def MAN_rejected(request):
    if 'm_id' in request.session:
        if request.session.has_key('m_id'):
            m_id = request.session['m_id']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(id=m_id)
        pro = project.objects.filter(status='Rejected').order_by("-id")
        return render(request,'MAN_rejectedprojectes.html',{'projects':pro,'mem':mem})
    else:
        return redirect('/')

def MAN_createproject(request):
    if 'm_id' in request.session:
        if request.session.has_key('m_id'):
            m_id = request.session['m_id']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(id=m_id)
        if request.method == 'POST':
            sc1 = request.POST['Department']
            sc2 = request.POST['designation']
            sc3 = request.POST['projectname']
            sc4 = request.POST['discrip']
            sc5 = request.POST['start']
            sc6 = request.POST['end']
            ogo = request.FILES['img[]']
            print(sc5,sc6,ogo,sc1)
            progress=0
            catry = project(designation_id=sc2,department_id=sc1,project=sc3,
                                      description=sc4,
                                      startdate=sc5, enddate=sc6, files=ogo,progress=progress)
            catry.save()
        dept = department.objects.all()
        desig = designation.objects.all() 
        return render(request,'MAN_createproject.html',{'desig':desig,'dept':dept,'mem':mem})
    else:
        return redirect('/')

def MAN_upcomingprojectsview(request):
    if 'm_id' in request.session:
        if request.session.has_key('m_id'):
            m_id = request.session['m_id']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(id=m_id)
        pro =project.objects.all().order_by("-id")
        return render(request,'MAN_upcomingprojectsview.html',{'projects': pro,'mem':mem})
    else:
        return redirect('/')

def MAN_seradmintraineedesi1(request):
    if 'm_id' in request.session:
        if request.session.has_key('m_id'):
            m_id = request.session['m_id']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(id=m_id)
        dept_id = request.GET.get('dept_id')
        Desig = designation.objects.filter(~Q(designation="admin"), ~Q(designation="manager"), ~Q(designation="account"))
        print('safdhar')
        return render(request, 'MAN_createprojectdropdown.html', {'Desig': Desig,'mem':mem})
    else:
        return redirect('/')

def MAN_seradmindesig(request):
    if 'm_id' in request.session:
        if request.session.has_key('m_id'):
            m_id = request.session['m_id']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(id=m_id)
        print("safdhar")
        dept_id = request.GET.get('dept_id')
        Desig = designation.objects.filter(~Q(designation='admin'),~Q(designation='manager'),~Q(designation='account'))
        print(Desig)
        return render(request, 'MAN_giveprojectdropdown.html', {'Desig': Desig,'mem':mem})
    else:
        return redirect('/')
        
def Manager_selectproject(request):
    
    print("safdhar")
    dept_id = request.GET.get('dept_id')
    # desig_id = request.GET.get('desig_id')
    # print(desig_id,dept_id)
    proj = project.objects.filter(department_id=dept_id)
    print(proj)
    return render(request,'manager_selectproject.html',{'project':proj})
    
    
# *************************meenu**********************
def newdept(request):
    if 'Adm_id' in request.session:
        if request.session.has_key('Adm_id'):
            Adm_id = request.session['Adm_id']
        else:
            return redirect('/')
        Adm = user_registration.objects.filter(id=Adm_id)
        condent = department.objects.all()
        return render(request,'BRadmin_Department.html',{'condent':condent,'Adm':Adm})
    else:
        return redirect('/')

def add_dept(request):
    if 'Adm_id' in request.session:
        if request.session.has_key('Adm_id'):
            Adm_id = request.session['Adm_id']
        else:
            return redirect('/')
        Adm = user_registration.objects.filter(id=Adm_id)
        return render(request,"BRadmin_add_dept.html",{'Adm':Adm})
    else:
        return redirect('/')

def add_deptsave(request):
    if 'Adm_id' in request.session:
        if request.session.has_key('Adm_id'):
            Adm_id = request.session['Adm_id']
        else:
            return redirect('/')
        Adm = user_registration.objects.filter(id=Adm_id)
        if request.method == 'POST':
            depart = request.POST['dept']
            logo = request.FILES['logo']
            a=department(department=depart,files=logo)
            a.save()
            m="Successfully department added"
        return render(request,'BRadmin_add_dept.html',{'m':m,'Adm':Adm})
    else:
        return redirect('/')

def delete(request, id):
    m = department.objects.get(id=id)
    os.remove(m.files.path)
    m.delete()
    return redirect('newdept')

def man_newdept(request):
    if 'm_id' in request.session:
        if request.session.has_key('m_id'):
            m_id = request.session['m_id']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(id=m_id)
        condent = department.objects.all()
        return render(request,'man_Department.html',{'condent':condent,'mem':mem})
    else:
        return redirect('/')


def man_dept(request):
    if 'm_id' in request.session:
        if request.session.has_key('m_id'):
            m_id = request.session['m_id']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(id=m_id)
        return render(request,"man_add_dept.html",{'mem':mem})
    else:
        return redirect('/')

def man_add_deptsave(request):
    if 'm_id' in request.session:
        if request.session.has_key('m_id'):
            m_id = request.session['m_id']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(id=m_id)
        if request.method == 'POST':
            depart = request.POST['dept']
            newfile = request.FILES['newfile']
            a=department(department=depart,files=newfile)
            a.save()
            m="Successfully department added"
        return render(request,'man_add_dept.html',{'m':m,'mem':mem})
    else:
        return redirect('/')

def man_delete(request, id):
    
    m = department.objects.get(id=id)
    try:
        m.delete()
        return redirect('man_newdept')
    except:
        messages.success(request, "  Error Occured: It can't be deleted, it used as ForeignKey Constrain !!")
        return redirect('man_newdept')


############## end ##########


#######################################################christin########################

def logout(request):
    if 'usernametsid' in request.session:
        request.session.flush()
        return redirect('/')
    else:
        return redirect('/')

def ProMANlogout(request):
    if 'prid' in request.session:  
        request.session.flush()
        return redirect('/')
    else:
        return redirect('/')

def TLlogout(request):
    if 'tlid' in request.session:  
        request.session.flush()
        return redirect('/')
    else:
        return redirect('/')

def devlogout(request):
    if 'devid' in request.session:  
        request.session.flush()
        return redirect('/')
    else:
        return redirect('/')



def internshipform(request):
    branch = branch_registration.objects.all()
    return render(request, 'internship.html',{'branch':branch})

def internship_save(request):
    branch = branch_registration.objects.all()
    a = internship()
    if request.method == 'POST':
        try:
            a.fullname = request.POST['name']
            a.collegename = request.POST['college_name']
            a.reg_date = datetime.now()
            a.reg_no = request.POST['reg_no']
            a.course = request.POST['course']
            a.stream = request.POST['stream']
            a.platform = request.POST['platform']
            a.branch_id  =  request.POST['branch']
            a.start_date =  request.POST['start_date']
            a.end_date  =  request.POST['end_date']
            a.mobile  =  request.POST['mobile']

            a.alternative_no  =  request.POST['alternative_no']

            a.email = request.POST['email']
            a.profile_pic  =  request.FILES['profile_pic']
            if (a.end_date<a.start_date):
                return render(request,'internship.html',{'a':a})
            else:
                a.save()
                qr = qrcode.make("https://infoxcore.com/admin_code?id=" + str(a.id))
                qr.save(settings.MEDIA_ROOT + "\\" +str(a.id) + ".png")
                with open(settings.MEDIA_ROOT + "\\" + str(a.id) + ".png", "rb") as reopen:
                        djangofile = File(reopen)
                        a.qr = djangofile

                        a.save()
            return redirect('internshipform')
        except:
            message = "Enter all details !!!"
            return render(request, 'internship.html',{'message':message})
    else:
        print("not")
        return render(request, 'internship.html')



def imagechange_pr(request):
  
    if request.method == 'POST':
        id = request.GET.get('id')
        abc = user_registration.objects.get(id=id)
        abc.photo = request.FILES['filename']
        
        abc.save()
        return redirect('pr_mg')
    return render(request, 'pr_mg.html')

def leave1(request):
    return render(request, 'leave.html')

def man_registration_form(request):
    branch = branch_registration.objects.all()
    depart = department.objects.all()
    a = user_registration()
    b = qualification()
    c = extracurricular()
    des = designation.objects.get(designation="trainee")
    if request.method == 'POST':
        if  user_registration.objects.filter(email=request.POST['email']).exists():
            
            msg_error = "Mail id already exist"
            return render(request, 'man_registration_form.html',{'msg_error': msg_error})
        else:
            
            a.fullname = request.POST['fname']
            a.fathername = request.POST['fathername']
            a.mothername = request.POST['mothername']
            a.dateofbirth = request.POST['dob']
            a.gender = request.POST['gender']
            a.presentaddress1 = request.POST['address1']
            a.presentaddress2  =  request.POST['address2']
            a.presentaddress3 =  request.POST['address3']
            a.pincode = request.POST['pincode']
            a.district  =  request.POST['district']
            a.state  =  request.POST['state']
            a.country  =  request.POST['country']
            a.permanentaddress1 = request.POST['paddress1']
            a.permanentaddress2  =  request.POST['paddress2']
            a.permanentaddress3  =  request.POST['paddress3']
            a.permanentpincode = request.POST['ppincode']
            a.permanentdistrict  =  request.POST['pdistrict']
            a.permanentstate  =  request.POST['pstate']
            a.permanentcountry =  request.POST['pcountry']
            a.mobile = request.POST['mobile']
            a.alternativeno = request.POST['alternative']
            a.department_id = request.POST['department']
            a.email = request.POST['email']
            a.status = "active"
            a.designation_id = des.id
            a.password= random.SystemRandom().randint(100000, 999999)
            
            # a.branch_id = request.POST['branch']
            a.photo = request.FILES['photo']
            a.idproof = request.FILES['idproof']
            a.save()
            
            x = user_registration.objects.get(id=a.id)
            today = date.today()
            tim = today.strftime("%m%y")
            x.employee_id = "INF"+str(tim)+''+"B"+str(x.id)
            passw=x.password
            email_id=x.email
            x.save()
            y1 = user_registration.objects.get(id=a.id)
            qr = qrcode.make("https://infoxcore.com/offerletter/" + str(y1.id))
            qr.save(settings.MEDIA_ROOT + "/images"+"//" +"offer"+str(y1.id) + ".png")
            with open(settings.MEDIA_ROOT + "/images"+"//"+"offer"+ str(y1.id) +".png","rb") as reopen:
                    djangofile = File(reopen)
                    y1.offerqr = djangofile
                    y1.save()
    
            y2 = user_registration.objects.get(id=a.id)
            qr1 = qrcode.make("https://infoxcore.com/relieveletter/" + str(y2.id))
            qr1.save(settings.MEDIA_ROOT + "/images"+"//"+"re" +str(y2.id) + ".png")
            with open(settings.MEDIA_ROOT + "/images"+"//"+"re" + str(y2.id) + ".png", "rb") as reopen:
                    djangofile = File(reopen)
                    y2.relieveqr = djangofile
                    y2.save()
            y3 = user_registration.objects.get(id=a.id)
            qr2 = qrcode.make("https://infoxcore.com/experienceletter/" + str(y3.id))
            qr2.save(settings.MEDIA_ROOT + "/images"+"//"+"exp" +str(y3.id) + ".png")
            with open(settings.MEDIA_ROOT + "/images"+"//"+"exp" + str(y3.id) + ".png", "rb") as reopen:
                    djangofile = File(reopen)
                    y3.expqr = djangofile
                    y3.save()
           
    
            b.user_id = a.id
            b.plustwo = request.POST.get('plustwo')
            b.school = request.POST['school']
            b.schoolaggregate = request.POST['aggregate']
            if request.FILES.get('cupload') is not None:
                b.schoolcertificate = request.FILES['cupload']
            b.ugdegree = request.POST['degree']
            b.ugstream = request.POST['stream']
            b.ugpassoutyr = request.POST['passoutyear']
            b.ugaggregrate = request.POST['aggregate1']
            b.backlogs = request.POST['supply']
            if request.FILES.get('cupload1') is not None:
                b.ugcertificate = request.FILES['cupload1']
            b.pg = request.POST['pg']
            b.save()
    
            c.user_id = a.id
            c.internshipdetails = request.POST['details']
            c.internshipduration = request.POST['duration']
            c.internshipcertificate = request.POST['certificate']
            c.onlinetrainingdetails = request.POST['details1']
            c.onlinetrainingduration = request.POST['duration1']
            c.onlinetrainingcertificate= request.POST['certificate1']
            c.projecttitle = request.POST['title']
            c.projectduration = request.POST['duration2']
            c.projectdescription = request.POST['description']
            c.projecturl = request.POST['url']
            c.skill1 = request.POST['skill1']
            c.skill2 = request.POST['skill2']
            c.skill3 = request.POST['skill3']
            c.save()
            
            subject = 'Greetings from iNFOX TECHNOLOGIES'
            message = 'Congratulations,\nYou have successfully registered iNFOX TECHNOLOGIES.\nYour login credentials \n\nEmail :'+str(email_id)+'\nPassword :'+str(passw)+'\n\nNote: This is a system generated email, do not reply to this email id.'
            email_from = settings.EMAIL_HOST_USER
            
            recipient_list = [email_id, ]
            send_mail(subject,message , email_from, recipient_list, fail_silently=True)
            msg_success = "Registration successfully Check Your Registered Mail"
            return render(request, 'man_registration_form.html',{'msg_success': msg_success,'branch':branch})
        
    return render(request, 'man_registration_form.html',{'branch':branch,'depart':depart})

def offerletter(request,id):
    mem = user_registration.objects.filter(id=id)
    return render(request,'qrofferview.html',{'mem':mem})

def relieveletter(request,id):
    mem = user_registration.objects.filter(id=id)
    return render(request,'qrreview.html',{'mem':mem})

def experienceletter(request,id):
    mem = user_registration.objects.filter(id=id)
    skill = extracurricular.objects.get(user_id=id)
    return render(request,'qrexpview.html',{'mem':mem, 'skill':skill})
    
    
def render_pdfof_view(request,id):

    date = datetime.now()  
    con = conditions.objects.get(id=1)
    mem = user_registration.objects.get(id=id)
    br_admin = branch_registration.objects.get(id=mem.branch_id)
    template_path = 'pdfof.html'
    context = {'mem': mem,
    'con':con,
    'media_url':settings.MEDIA_URL,
    'date':date,
    'br_admin':br_admin
    }
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    # response['Content-Disposition'] = 'attachment; filename="certificate.pdf"'
    response['Content-Disposition'] = 'filename="certificate.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
       html, dest=response)
    


    # if error then show some funy view
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response

def render_pdfre_view(request,id):

    date = datetime.now()   
    mem = user_registration.objects.get(id=id)
    br_admin = branch_registration.objects.get(id=mem.branch_id)
    template_path = 'pdfre.html'
    context = {'mem': mem,
    'media_url':settings.MEDIA_URL,
    'date':date,
    'br_admin':br_admin
    }
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    # response['Content-Disposition'] = 'attachment; filename="certificate.pdf"'
    response['Content-Disposition'] = 'filename="certificate.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
       html, dest=response)
    


    # if error then show some funy view
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response

def render_pdfex_view(request,id):

    date = datetime.now()   
    mem = user_registration.objects.get(id=id)
    br_admin = branch_registration.objects.get(id=mem.branch_id)
    template_path = 'pdfex.html'
    context = {'mem': mem,
    'media_url':settings.MEDIA_URL,
    'date':date,
    'br_admin':br_admin
    }
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    # response['Content-Disposition'] = 'attachment; filename="certificate.pdf"'
    response['Content-Disposition'] = 'filename="certificate.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
       html, dest=response)
    


    # if error then show some funy view
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response
    
def render_pdfau_view(request,id):

    date = datetime.now()   
    mem = user_registration.objects.get(id=id)
    template_path = 'pdfau.html'
    context = {'mem': mem,
    'media_url':settings.MEDIA_URL,
    'date':date
    }
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    # response['Content-Disposition'] = 'attachment; filename="certificate.pdf"'
    response['Content-Disposition'] = 'filename="certificate.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
       html, dest=response)
    


    # if error then show some funy view
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response

def admin_code(request):
    id=request.GET.get('id')

    empid=internship.objects.filter(id=id)
    context = {
        'mem':empid,
        'media_url':settings.MEDIA_URL
        }
    return render(request, 'admin_code.html', context)


def promanagerindex(request):
    return render(request, 'promanagerindex.html')
    
    
def pr_mg(request):
    if 'prid' in request.session:
        if request.session.has_key('prid'):
            prid = request.session['prid']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(id=prid)
        return render(request, 'account_tr_mg.html', {'mem': mem})
    else:
        return redirect('/')

def pmanager_dash(request):
    if 'prid' in request.session:
        if request.session.has_key('prid'):
            prid = request.session['prid']
        else:
            variable = "dummy"
        pro = user_registration.objects.filter(id=prid)
        labels = []
        data = []
        queryset = user_registration.objects.filter(id=prid)
        des = designation.objects.get(designation="team leader")
        des1 = designation.objects.get(designation="developer")
        dev = user_registration.objects.filter(projectmanager_id=prid)
        ids = dev.values_list('id', flat="true")
        le = leave.objects.filter(user_id__in=ids.all()).filter(Q(designation_id=des.id) | Q(
            designation_id=des1.id)).filter(leaveapprovedstatus=0).order_by('-id')
        for i in queryset:
            labels = [i.workperformance, i.attitude, i.creativity]

            data = [i.workperformance, i.attitude, i.creativity]

        return render(request, 'pmanager_dash.html', {'pro': pro, "labels": labels, "data": data, 'le': le})
    else:
        return redirect('/')

def projectmanager_projects(request):
    if 'prid' in request.session:
        if request.session.has_key('prid'):
            prid = request.session['prid']
        else:
           return redirect('/')
        pro = user_registration.objects.filter(id=prid)
        return render(request, 'projectmanager_projects.html',{'pro':pro})
    else:
        return redirect('/')

# nirmal
def projectmanager_assignproject(request):
    if 'prid' in request.session:
        if request.session.has_key('prid'):
            prid = request.session['prid']
       
        else:
            return redirect('/')
        pro = user_registration.objects.filter(id=prid)
        desi_id = user_registration.objects.get(id=prid)
        d = designation.objects.get(designation="team leader")
        t = designation.objects.get(designation="tester")
        
        
        tes = user_registration.objects.filter(department_id = desi_id.department_id, designation_id= t.id)
        spa = user_registration.objects.filter(department_id = desi_id.department_id, designation_id= d.id)
        
        pvar = project.objects.filter(Q(status="accepted")|Q(status="assigned"))
        
        if request.method =='POST':
            
            var = project_taskassign()
            # print("hii")
            var.user_id = prid
            var.tl_id = request.POST['pname']
            var.task = request.POST['task']
            var.subtask = request.POST['task']
            var.description=request.POST.get('desc')
            var.startdate=request.POST.get('sdate')
            var.enddate=request.POST.get('edate')
            
            bb= datetime.strptime(var.startdate, '%Y-%m-%d').strftime('%d-%m-%Y')
            
            cc= datetime.strptime(var.enddate, '%Y-%m-%d').strftime('%d-%m-%Y')
            if request.FILES.get('pfile') is not None:
                var.files=request.FILES.get('pfile')
                
            var.project_id = request.POST.get('yyy')

            var.developer_id= request.POST['pname']
            var.tester_id= request.POST['tname']

            var.save()
            new = project.objects.get(id=var.project_id)
            new.status = "assigned"
            new.save()
            v = request.POST.get('pname')
            em=user_registration.objects.get(id=v)
            
            # subject = 'Greetings from iNFOX TECHNOLOGIES'
            # message = 'Congratulations,\n' \
            # 'You are assigned new project from iNFOX TECHNOLOGIES.\n' \
            # 'following is your Project Details\n'\
            # 'Project :'+str(new.project)+'\n' 'Task :'+str(var.task) +'\n' 'Description :'+str(var.description)+'\n''Start Date :'+bb+'\n' 'End Date :'+cc+'\n'\
            # '\n' 'Complete your project on or before Enddate \n'\
            #     'NOTE : THIS IS A SYSTEM GENETATED MAIL PLEASE DO NOT REPLY' 
            # recepient = str(em.email)
            # send_mail(subject, message, EMAIL_HOST_USER,
            #       [recepient], fail_silently=False)
            msg_success = "Project assigned successfully"
            
            return render(request, 'projectmanager_assignproject.html',{'pro':pro,'spa':spa,'pvar':pvar,'tes':tes, 'msg_success':msg_success})
        return render(request, 'projectmanager_assignproject.html', {'pro':pro,'spa':spa,'pvar':pvar,'tes':tes})
    else:
        return redirect('/')

def projectmanager_projectstatus(request,id):
    if 'prid' in request.session:
        if request.session.has_key('prid'):
            prid = request.session['prid']
        else:
            return redirect('/')
        pro = user_registration.objects.filter(id=prid)
        des = designation.objects.get(designation="team leader")
        dev = designation.objects.get(designation="developer")
        var = project_taskassign.objects.filter(project_id=id,subtask__isnull = True).order_by('-id')
        data = test_status.objects.filter(project_id=id).order_by('-id')
        data1 = tester_status.objects.filter(project_id=id).order_by('-id')
        newdata = project_taskassign.objects.filter(project_id=id,subtask__isnull = False).order_by('-id')
        return render(request, 'projectmanager_projectstatus.html',{'pro':pro,'var':var,'data':data,'data1':data1,'newdata':newdata})
    else:
        return redirect('/')
        
def projectmanager_projectlist(request):
    if 'prid' in request.session:
        if request.session.has_key('prid'):
            prid = request.session['prid']
        else:
            return redirect('/')
        pro = user_registration.objects.filter(id=prid)
        var=project.objects.filter(Q(status="accepted")|Q(status="assigned")|Q(status="completed")).order_by("-id")
        return render(request, 'projectmanager_projectlist.html',{'pro':pro,'var':var})
    else:
        return redirect('/')

def projectmanager_createproject(request):
    if 'prid' in request.session:
        if request.session.has_key('prid'):
            prid = request.session['prid']
      
            
        mem = user_registration.objects.filter(id=prid)  
        br_id = user_registration.objects.get(id=prid)
         
        if request.method =='POST':
            mem = user_registration.objects.filter(id=prid)
            mem2 = user_registration.objects.get(id=prid)
            var = project()
            var.projectmanager_id = prid
            var.department_id = mem2.department_id
            var.project=request.POST.get('pname')
            var.startdate=request.POST.get('sdate')
            var.enddate=request.POST.get('edate')
            var.description=request.POST.get('desc')
            var.files=request.FILES.get('pfile')
            var.branch_id=br_id.branch_id
            var.save()
            

            msg_success = "Project created successfully"
            return render(request, 'projectmanager_createproject.html',{'msg_success':msg_success})
        return render(request, 'projectmanager_createproject.html',{'pro':mem})
    else:
        return redirect('/')

def projectmanager_description(request,id):
    if 'prid' in request.session:
        if request.session.has_key('prid'):
            prid = request.session['prid']
        else:
           return redirect('/')
        pro = user_registration.objects.filter(id=prid)
        projects = project.objects.filter(id=id)  
        return render(request, 'projectmanager_description.html',{'pro':pro,'projects':projects})
    else:
        return redirect('/')

def projectmanager_table(request):
    if 'prid' in request.session:
        if request.session.has_key('prid'):
            prid = request.session['prid']
        else:
           return redirect('/')
        pro = user_registration.objects.filter(id=prid)
        projects = project.objects.filter(status__isnull = True).order_by("-id")
        return render(request, 'projectmanager_table.html',{'pro':pro,'projects':projects})
    else:
        return redirect('/')

def projectmanager_table(request):
    if 'prid' in request.session:
        if request.session.has_key('prid'):
            prid = request.session['prid']
        else:
           return redirect('/')
        pro = user_registration.objects.filter(id=prid)
        projects = project.objects.filter(status__isnull = True).order_by('-id')
        return render(request, 'projectmanager_table.html',{'pro':pro,'projects':projects})
    else:
        return redirect('/')

def proMAN_acceptproj(request,id):
    pro_sts = project.objects.filter(id=id).update(status="accepted")
    if 'prid' in request.session:
        if request.session.has_key('prid'):
            prid = request.session['prid']
        else:
           return redirect('/')
        pro = user_registration.objects.filter(id=prid)
        projects = project.objects.filter(status__isnull = True).order_by('-id')
        return render(request, 'projectmanager_table.html',{'pro':pro,'projects':projects})

def proMAN_rejectproj(request,id):
   
    if 'prid' in request.session:
        if request.session.has_key('prid'):
            prid = request.session['prid']
        else:
            return redirect('/')
        if request.method == 'POST':
            user_reason=request.POST.get('reply')
            rejectdate = datetime.now()
            pro_sts = project.objects.filter(id=id).update(user_reason= user_reason,status ='rejected',rejectdate=rejectdate)
        
        pro = user_registration.objects.filter(id=prid)
        projects = project.objects.filter(status__isnull = True).order_by('-id')
        return render(request, 'projectmanager_table.html',{'pro':pro,'projects':projects})


def projectmanager_upprojects(request):
    if 'prid' in request.session:
        if request.session.has_key('prid'):
            prid = request.session['prid']
        else:
           return redirect('/')
        pro = user_registration.objects.filter(id=prid)
        return render(request, 'projectmanager_upprojects.html',{'pro':pro})
    else:
        return redirect('/')

# praveesh

def projectmanager_accepted_projects(request):
    if 'prid' in request.session:
        if request.session.has_key('prid'):
            prid = request.session['prid']
        else:
           return redirect('/')
        projects = project.objects.filter(~Q(status="Completed"),~Q(status="completed"), ~Q(status="rejected"))
        pro = user_registration.objects.filter(id=prid).order_by("-id")
        return render(request, 'projectManager_accepted_projects.html',{'pro':pro,'projects':projects})
    else:
        return redirect('/')
        
def projectmanager_edit_assigned_projects(request):
    if 'prid' in request.session:
        if request.session.has_key('prid'):
            prid = request.session['prid']
        else:
           return redirect('/')
        
        pro = user_registration.objects.filter(id=prid).order_by("-id")
        if 'proj_date_change' in request.POST:
            uid = request.POST.get('proj_id')
            assin = project_taskassign.objects.get(id=uid)
            assin.enddate = request.POST.get('sdate')
            assin.save()
            msg_success = "Date Changed successfully"
            return render(request, 'projectManager_edit_accepted_projects.html',{'pro':pro,'msg_success':msg_success})
        elif "delete_proj" in request.POST:
            uid = request.POST.get('proj_id')
            proj = project_taskassign.objects.get(id=uid)
            proj.delete()
            msg_success = "Task deleted successfully"
            return render(request, 'projectManager_edit_accepted_projects.html',{'pro':pro,'msg_success':msg_success})
        else:
            projects = project_taskassign.objects.filter(~Q(status="submitted"), ~Q(status="Completed"),~Q(status="completed")).order_by("-id")
            
            return render(request, 'projectManager_edit_accepted_projects.html',{'pro':pro,'projects':projects})
    else:
        return redirect('/')
        
def projectManager_edit_projects_status(request):
    if 'prid' in request.session:
        if request.session.has_key('prid'):
            prid = request.session['prid']
        else:
           return redirect('/')
           
        if request.method=="POST":
            uid = request.POST.get('proj_id')
            proj = project.objects.get(id=uid)
            proj.progress = request.POST.get('progress')
            proj.save()
            msg_success = "Progress update successfully"
            return render(request, 'projectManager_edit_projects_status.html',{'msg_success':msg_success})
        else:
            projects = project.objects.filter().order_by("-id")
            pro = user_registration.objects.filter(id=prid).order_by("-id")
            return render(request, 'projectManager_edit_projects_status.html',{'pro':pro,'projects':projects})
    else:
        return redirect('/')

def projectmanager_rejected_projects(request):
    if 'prid' in request.session:
        if request.session.has_key('prid'):
            prid = request.session['prid']
        else:
           return redirect('/')
        projects = project.objects.filter(status="rejected")
        pro = user_registration.objects.filter(id=prid).order_by("-id")
        return render(request, 'projectManager_rejected_projects.html',{'pro':pro,'projects':projects})
    else:
        return redirect('/')


# bibin #amal #abin #rohit
def manindex(request):
    return render(request, 'manager_index.html')

def projectmanEmp(request):
    if 'prid' in request.session:
        if request.session.has_key('prid'):
            prid = request.session['prid']
        else:
           return redirect('/')
        pro = user_registration.objects.filter(id=prid)
        return render(request, 'projectman_emp.html', {'pro': pro})
    else:
        return redirect('/')

def projectmanDev(request):
    if 'prid' in request.session:
        if request.session.has_key('prid'):
            prid = request.session['prid']
        else:
           return redirect('/')
        pro = user_registration.objects.filter(id=prid)
        pro_dep = user_registration.objects.get(id=prid)
        des_id = designation.objects.get(designation="developer")
        man = user_registration.objects.filter(designation_id=des_id.id).filter(department_id=pro_dep.department_id,status="active").order_by("-id")
        return render(request, 'projectman_dev.html',{'pro':pro,'man':man})
    else:
        return redirect('/')

def projectmanDevDashboard(request,id):
    if 'prid' in request.session:
        if request.session.has_key('prid'):
            prid = request.session['prid']
        else:
           return redirect('/')
        pro = user_registration.objects.filter(id=prid)
        man = user_registration.objects.get(id=id)
        labels = []
        data = []
        queryset = user_registration.objects.filter(id=id)
        for i in queryset:
            labels=[i.workperformance,i.attitude,i.creativity]
            data=[i.workperformance,i.attitude,i.creativity]
        return render(request, 'projectman_dev_Dashboard.html',{'labels':labels,'data':data,'pro':pro,'man':man})
    else:
        return redirect('/')


def pro_allocatetl(request):
    if 'prid' in request.session:
        if request.session.has_key('prid'):
            prid = request.session['prid']
        else:
           return redirect('/')
            
        pro = user_registration.objects.filter(id=prid)
        des_tl = designation.objects.get(designation = "team leader")
        des_dev = designation.objects.get(designation = "developer ")
        devs = user_registration.objects.filter(designation_id=des_dev.id,status="active")
        tls = user_registration.objects.filter(designation_id=des_tl.id,status="active")
        
        tl_name = user_registration.objects.all()
        
        if request.method == "POST":
            emp_id = request.POST.get('id')
            tl_id = request.POST.get('team')
            
            alocate = user_registration.objects.get(id=emp_id)
            alocate.tl_id = tl_id
            alocate.save()
            return redirect('pro_allocatetl')
            
        return render(request, 'Pro_allocatetl.html', {'mem': tls, 'memm': devs,'pro':pro, 'tl_name':tl_name})
    else:
        return redirect('/')



def projectman_developer_attendance(request,id):
    if 'prid' in request.session:
        if request.session.has_key('prid'):
            prid = request.session['prid']
        else:
           return redirect('/')
        pro = user_registration.objects.filter(id=prid)
        return render(request, 'projectman_team_attendance.html',{'pro':pro})
    else:
        return redirect('/')

def projectman_team(request, id):
    if 'prid' in request.session:
        if request.session.has_key('prid'):
            prid = request.session['prid']
        else:
           return redirect('/')
        pro = user_registration.objects.filter(id=prid) 
        teamid = user_registration.objects.filter(tl_id=id,status="active").order_by("-id") 
        return render(request, 'projectman_team.html',{'pro': pro,'teamid': teamid})
    else:
        return redirect('/')  

def projectman_team_profile(request, id):
    if 'prid' in request.session:
        if request.session.has_key('prid'):
            prid = request.session['prid']
        else:
           return redirect('/')
        pro = user_registration.objects.filter(id=prid)  
        ind = user_registration.objects.filter(id=id)
        labels = []
        data = []
        queryset = user_registration.objects.filter(id=id)
        for i in queryset:
            labels=[i.workperformance,i.attitude,i.creativity]
            data=[i.workperformance,i.attitude,i.creativity]
        return render(request, 'projectman_team_profile.html',{'pro': pro,'ind': ind,'labels':labels,'data':data})
    else:
        return redirect('/')  

def projectman_team_attendance(request,id):
    if 'prid' in request.session:
        if request.session.has_key('prid'):
            prid = request.session['prid']
        else:
           return redirect('/')
        pro = user_registration.objects.filter(id=prid)
        man = user_registration.objects.filter(id=id)  
        return render(request,'projectman_team_attendance.html',{'pro':pro,'man':man})
    else:
        return redirect('/')  
def projectman_team_attandance(request,id):
    if 'prid' in request.session:
        if request.session.has_key('prid'):
            prid = request.session['prid']
        else:
           return redirect('/')
        pro = user_registration.objects.filter(id=prid)
        man = attendance.objects.filter(user_id=id)  
        if request.method == "POST":
            fromdate = request.POST.get('fromdate')
            todate = request.POST.get('todate') 
            mem1 = attendance.objects.filter(date__range=[fromdate, todate]).filter(user_id=id) 
        return render(request, 'projectman_team_attandance.html', {'pro': pro,'mem1':mem1,'man':man})
    else:
        return redirect('/')

def projectMANattendance(request):
    if 'prid' in request.session:
        if request.session.has_key('prid'):
            prid = request.session['prid']
        else:
            return redirect('/')
        pro = user_registration.objects.filter(id=prid)
        return render(request, 'projectMANattendance.html',{'pro':pro})
    else:
        return redirect('/')

def projectMANattandance(request):
    if 'prid' in request.session:
        if request.session.has_key('prid'):
            prid = request.session['prid']
        else:
            return redirect('/')
        pro = user_registration.objects.filter(id=prid)
        if request.method == "POST":
            fromdate = request.POST.get('fromdate')
            todate = request.POST.get('todate') 
            prm1 = attendance.objects.filter(date__range=[fromdate, todate]).filter(user_id=prid)
        return render(request, 'projectMANattendancesort.html',{'pro':pro,'prm1':prm1})
    else:
        return redirect('/')


# def projectMANreportsuccess(request):
#     if 'prid' in request.session:
#         if request.session.has_key('prid'):
#             prid = request.session['prid']
#         else:
#             return redirect('/')
#         pro = user_registration.objects.filter(id=prid)
#         if request.method == 'POST':
#             # uid=objects.GET.get('user_id')
#             vars = reported_issue()
#             vars.issue=request.POST.get('report')
#             vars.reported_date=datetime.datetime.now()
#             vars.reported_to_id=2
#             vars.reporter_id=prid
#             vars.status='pending'
#             vars.save()
#         return render(request, 'MANreportsuccess.html',{'pro':pro})
#     else:
#         return redirect('/')  

def projectMANleave(request):
    if 'prid' in request.session:
        if request.session.has_key('prid'):
            prid = request.session['prid']
        else:
            return redirect('/')
        pro = user_registration.objects.filter(id=prid)
        return render(request, 'projectMANleave.html',{'pro':pro})
    else:
        return redirect('/') 

def projectMANleavereq(request):
    if 'prid' in request.session:
        if request.session.has_key('prid'):
            prid = request.session['prid']
        else:
            return redirect('/')
        pro = user_registration.objects.filter(id=prid)
        if request.method == "POST":
            
            
            mem = leave()
            mem.from_date = request.POST.get('from')
            mem.to_date = request.POST.get('to')
            mem.leave_status = request.POST.get('haful')
            mem.reason = request.POST.get('reason')
            mem.user_id = request.POST.get('pr_id')
            mem.status = "pending"

            start = datetime.strptime(mem.from_date, '%Y-%m-%d').date() 
            end = datetime.strptime(mem.to_date, '%Y-%m-%d').date()

            diff = (end  - start).days
            
            cnt =  Event.objects.filter(start_time__range=(start,end)).count()
            
            if diff == 0:
                mem.days = 1
            else:
                mem.days = diff - cnt

            mem.save()
        return render(request, 'projectMANleavereq.html',{'pro':pro})  
    else:
        return redirect('/')




def projectMANreqedleave(request):
    if 'prid' in request.session:
        if request.session.has_key('prid'):
            prid = request.session['prid']
        else:
            return redirect('/')
        pro = user_registration.objects.filter(id=prid)
        var = leave.objects.filter(user_id=prid).order_by("-id")
        return render(request, 'projectMANreqedleave.html',{'pro':pro,'var':var}) 
    else:
        return redirect('/')

def Manager_employees(request):
    return render(request,'Manager_employees.html')

def projectManager_tl(request):
    if 'prid' in request.session:
        if request.session.has_key('prid'):
            prid = request.session['prid']
        else:
           return redirect('/')
        pro = user_registration.objects.filter(id=prid)
        dept_id = user_registration.objects.get(id=prid)
        p = designation.objects.get(designation="team leader")
        tlfil = user_registration.objects.filter(designation_id=p.id, department_id = dept_id.department_id, status="active").order_by("-id")
        return render(request, 'projectManager_tl.html', {'pro': pro, 'tlfil': tlfil})
    else:
        return redirect('/')


def projectManager_tl_dashboard(request, id):
    if 'prid' in request.session:
        if request.session.has_key('prid'):
            prid = request.session['prid']
        else:
           return redirect('/')
        pro = user_registration.objects.filter(id=prid)
        tls = user_registration.objects.filter(id=id) 
        labels = []
        data = []
        queryset = user_registration.objects.filter(id=id)
        for i in queryset:
            labels=[i.workperformance,i.attitude,i.creativity]
            data=[i.workperformance,i.attitude,i.creativity]
        return render(request, 'projectManager_tl_dashboard.html',{'labels':labels,'data':data,'pro': pro, 'tls': tls})
    else:
        return redirect('/')



def man_tl_attendance(request):
    return render(request,'man_tl_attendance.html')

def projectmanager_currentproject(request):
    if 'prid' in request.session:
        if request.session.has_key('prid'):
            prid = request.session['prid']
        else:
            return redirect('/')
        proj = user_registration.objects.get(id=prid)
        pro = user_registration.objects.filter(id=prid)
        var=project.objects.filter(department_id=proj.department_id,status="assigned").order_by('-id')
        return render(request, 'projectmanager_currentproject.html',{'pro':pro,'var':var}) 
    else:
        return redirect('/')
        
def completepro(request,id):
    if 'prid' in request.session:
        if request.session.has_key('prid'):
            prid = request.session['prid']
        else:
           return redirect('/')
        pro = user_registration.objects.filter(id=prid)
        display = project.objects.get(id=id)
        if request.method == "POST":
            var =project.objects.get(id=id)
            var.status="completed"
            var.progress=100
            var.save()
            pro = user_registration.objects.filter(id=prid)
            display = project.objects.get(id=id)
            return render(request, 'projectmanager_currentdetail.html',{'pro':pro,'display':display})
        return render(request, 'projectmanager_currentdetail.html',{'pro':pro,'display':display})
    else:
        return redirect('/')
        
def projectmanager_currentdetail(request,id):
    if 'prid' in request.session:
        if request.session.has_key('prid'):
            prid = request.session['prid']
        else:
            return redirect('/')
        pro = user_registration.objects.filter(id=prid)
        display = project.objects.get(id=id)
        return render(request, 'projectmanager_currentdetail.html',{'pro':pro,'display':display})
    else:
        return redirect('/')
def projectmanager_currentteam(request,id):
    if 'prid' in request.session:
        if request.session.has_key('prid'):
            prid = request.session['prid']
        else:
            return redirect('/')
        pro = user_registration.objects.filter(id=prid)
        
        display = project_taskassign.objects.filter(project_id=id).values('tl_id').distinct()
        
        uniq = user_registration.objects.all()
      
        return render(request, 'projectmanager_currentteam.html',{'pro':pro,'display':display, 'uniq':uniq})
    else:
        return redirect('/')
def projectmanager_completeteam(request,id):
    if 'prid' in request.session:
        if request.session.has_key('prid'):
            prid = request.session['prid']
        else:
            return redirect('/')
        pro = user_registration.objects.filter(id=prid)
        display = project_taskassign.objects.filter(project_id=id)
        return render(request, 'projectmanager_completeteam.html',{'pro':pro,'display':display})
    else:
        return redirect('/')


def projectmanager_currenttl(request,id):
    if 'prid' in request.session:
        if request.session.has_key('prid'):
            prid = request.session['prid']
        else:
            return redirect('/')

        pro = user_registration.objects.filter(id=prid)
        display2 = user_registration.objects.all()
        display = project_taskassign.objects.filter(project_id=id).values('project_id','tl_id').distinct()
        
        return render(request, 'projectmanager_currenttl.html',{'pro':pro,'display':display,'display2':display2})
    else:
        return redirect('/')

    
def projectmanager_completeproject(request):
    if 'prid' in request.session:
        if request.session.has_key('prid'):
            prid = request.session['prid']
        else:
            return redirect('/')
        pro = user_registration.objects.filter(id=prid)
        asus = project.objects.filter(status="completed")
        return render(request, 'projectmanager_completeproject.html',{'pro':pro,'asus':asus})
    else:
        return redirect('/')

def projectmanager_completedetail(request,id):
    if 'prid' in request.session:
        if request.session.has_key('prid'):
            prid = request.session['prid']
        else:
            return redirect('/')
        pro = user_registration.objects.filter(id=prid)
        val = project.objects.filter(id=id)
        return render(request, 'projectmanager_completedetail.html',{'pro':pro,'val':val})
    else:
        return redirect('/')



def projectmanager_teaminvolved(request, id):
    if 'prid' in request.session:
        if request.session.has_key('prid'):
            prid = request.session['prid']
        else:
           return redirect('/')
        pro = user_registration.objects.filter(id=prid)
        pri = project_taskassign.objects.filter(developer_id=id).order_by("-id")
        return render(request, 'projectmanager_teaminvolved.html',{'pro': pro, 'pri': pri})
    else:
        return redirect('/')


def projectmanager_devteam(request,id):
    if 'prid' in request.session:
        if request.session.has_key('prid'):
            prid = request.session['prid']
        else:
           return redirect('/')
        pro = user_registration.objects.filter(id=prid)
        man = user_registration.objects.filter(tl_id = id).order_by("-id")
        return render(request, 'projectmanager_devteam.html',{'pro':pro,'man':man})
    else:
        return redirect('/')



def projectmanager_completetl(request,id):
    if 'prid' in request.session:
        if request.session.has_key('prid'):
            prid = request.session['prid']
        else:
            return redirect('/')
        pro = user_registration.objects.filter(id=prid)
        com = project.objects.filter(status = "completed")
        display = project_taskassign.objects.filter(project_id=id).values('project_id','tl_id').distinct()
        user = user_registration.objects.all()

        return render(request, 'projectmanager_completetl.html',{'pro':pro,'com':com,'display':display,'user':user})
    else:
        return redirect('/')


def projectMANreportedissue(request):
    if 'prid' in request.session:
        if request.session.has_key('devdes'):
            devdes = request.session['devdes']
        if request.session.has_key('devdep'):
            devdep = request.session['devdep']
        if request.session.has_key('prid'):
            prid = request.session['prid']
        else:
           return redirect('/')
        pro = user_registration.objects.filter(id=prid)
        var=reported_issue.objects.filter(reporter=prid).order_by("-id")
    
        return render(request, 'projectMANreportedissue.html',{'var':var,'pro':pro})
    else:
        return redirect('/')
def projectMANreportissue(request):
    if 'prid' in request.session:
        if request.session.has_key('prid'):
            prid = request.session['prid']
        else:
           return redirect('/')
        pro = user_registration.objects.filter(id=prid)
        return render(request, 'projectMANreportissue.html',{'pro':pro})
    else:
        return redirect('/')

def projectmanagerreportedissue2(request,id):
    if 'prid' in request.session:
        if request.session.has_key('prid'):
            prid = request.session['prid']
        else:
           return redirect('/')
        pro = user_registration.objects.filter(id=prid)
        rid=request.GET.get('rid')
        var=reported_issue.objects.filter(id=id)
        
        return render(request, 'projectmanagerreportedissue2.html',{'var':var,'pro':pro})
    else:
        return redirect('/')

def projectmanagerreportedissue3(request,id):
    if 'prid' in request.session:
        if request.session.has_key('prid'):
            prid = request.session['prid']
        else:
           return redirect('/')
        pro = user_registration.objects.filter(id=prid)
        rid=request.GET.get('rid')
        var=reported_issue.objects.filter(id=id)
        
        return render(request, 'projectmanagerreportedissue2.html',{'var':var,'pro':pro})
    else:
        return redirect('/')


def currentperformance(request, id):
    if 'prid' in request.session:
   
        
        if request.session.has_key('prid'):
            prid = request.session['prid']
        
        pro = user_registration.objects.filter(id=prid)
        mem = user_registration.objects.get(id=id)
        if request.method == 'POST':
            mem.attitude = request.POST['sele1']
            mem.creativity = request.POST['sele2']
            mem.workperformance = request.POST['sele3']
            mem.save()
            return render(request, 'currentperformance.html', {'mem': mem, 'pro': pro})
        return render(request, 'currentperformance.html', {'mem': mem, 'pro': pro})
    else:
        return render('/')

def MANreportsuccess(request):
    if 'prid' in request.session:
        if request.session.has_key('prid'):
            prid = request.session['prid']
        else:
           return redirect('/')
        pro = user_registration.objects.filter(id=prid)
        pro1 = user_registration.objects.get(id=prid)
        design=designation.objects.get(designation="manager")
        man = user_registration.objects.get(branch_id=pro1.branch_id,designation_id=design.id)
        if request.method == 'POST':
            
            vars = reported_issue()
            vars.issue=request.POST.get('MANreportissue')
            vars.reported_date=datetime.now()
            vars.reported_to_id=man.id
            vars.reporter_id=prid
            vars.status='pending'
            vars.save()
        return render(request, 'projectMANreportedissues.html',{'pro':pro})
    else:
        return redirect('/')


def projectmanager_tlreported(request):
    if 'prid' in request.session:
        if request.session.has_key('prid'):
            prid = request.session['prid']
    
        else:
           return redirect('/')
        desi = designation.objects.get(designation="team leader")
        pro = user_registration.objects.filter(id=prid)
        vars=user_registration.objects.filter(designation=1)
        var=reported_issue.objects.filter(designation_id=desi.id)
        # vars=user_registration.objects.filter(designation_id=2).filter(id=devid)
        return render(request, 'projectmanager_tlreported.html',{'var':var,'vars':vars,'pro':pro})
    else:
        return redirect('/')

def projectreply(request,id):
    if 'prid' in request.session:
        if request.session.has_key('prid'):
            prid = request.session['prid']
        else:
           return redirect('/')
        pro = user_registration.objects.filter(id=prid)
        if request.method == 'POST':
            
            vars = reported_issue.objects.get(id=id)
            vars.reply=request.POST.get('reply')
            vars.save()
        return redirect('projectmanager_tlreported')
    else:
        return redirect('/')

def projectreplytl(request,id):
    if 'prid' in request.session:
        if request.session.has_key('tlid'):
            prid = request.session['tlid']
        else:
           return redirect('/')
        pro = user_registration.objects.filter(id=prid)
        if request.method == 'POST':
            v = reported_issue.objects.get(id=id)
            v.reply=request.POST.get('reply')
            v.save()
        return redirect('devtlreported')
    else:
        return redirect('/')

def projectMANreportedissues(request):
    if 'prid' in request.session:
        if request.session.has_key('prid'):
            prid = request.session['prid']
        pro = user_registration.objects.filter(id=prid)
        return render(request,'projectMANreportedissues.html',{'pro':pro})
    else:
        return redirect('/')


# -------------------------------------------------------------------------------------------------------------------------------------

# TL module

def TLdashboard(request):
    if 'tlid' in request.session:
        if request.session.has_key('tlid'):
            tlid = request.session['tlid']
        else:
            variable = "dummy"
        mem = user_registration.objects.filter(id=tlid)
        labels = []
        data = []
        queryset = user_registration.objects.filter(id=tlid)
        dev = user_registration.objects.filter(tl_id=tlid)
        ids = dev.values_list('id', flat="true")
        des = designation.objects.get(designation="developer")
        le = leave.objects.filter(user_id__in=ids.all(
        ), designation_id=des.id, leaveapprovedstatus=0)

        

        for i in queryset:
            labels = [i.workperformance, i.attitude, i.creativity]
            data = [i.workperformance, i.attitude, i.creativity]
        return render(request, 'TLdashboard.html', {'labels': labels, 'data': data, 'mem': mem, 'le': le})
    else:
        return redirect('/')
        
def tldevview(request,id):
    if 'tlid' in request.session:
        if request.session.has_key('tlid'):
            tlid = request.session['tlid']
        else:
           return redirect('/')
        mem = user_registration.objects.filter(id=tlid)
        rid=request.GET.get('rid')
        mem1=reported_issue.objects.filter(id=id)
        
        return render(request, 'tldevview.html',{'mem1':mem1,'mem':mem})
    else:
        return redirect('/')
        
def TLprojects(request):
    if 'tlid' in request.session:
        if request.session.has_key('tlid'):
            tlid = request.session['tlid']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(id=tlid)
        display1 = project.objects.all()
        display=project_taskassign.objects.filter(developer_id=tlid).values('project_id').distinct()
        return render(request, 'TLprojects.html',{'display':display,'mem':mem,'display1':display1})
    else:
        return redirect('/')

def tlprojecttasks(request,id):
    if 'tlid' in request.session:
        if request.session.has_key('tlid'):
            tlid = request.session['tlid']
        else:
            return redirect('/')
            
        
        if request.method == 'POST':
            uid = request.POST.get('id')
            mems = project_taskassign.objects.get(id=uid)
            task = test_status()
            task.date = datetime.now()
            task.workdone = request.POST['workdone']
            task.git_commit = request.POST['gitcommit']
            task.git_link = request.POST['gitlink']
            task.user_id = tlid
            task.subtask_id = mems.id
            task.project_id = mems.project_id
            
            dct_file = dict(request.FILES)
            lst_screenshot = dct_file['filed']
            lst_file = []
            for ins_screenshot in lst_screenshot:
                str_img_path = ""
                if ins_screenshot:
                    img_emp = ins_screenshot
                    fs = FileSystemStorage(location=settings.MEDIA_ROOT,base_url=settings.MEDIA_URL)
                    str_img = fs.save(''.join(filter(str.isalnum, str(img_emp))), img_emp)
                    str_img_path = fs.url(''.join(filter(str.isalnum, str_img)))
                    lst_file.append('/media/'+''.join(filter(str.isalnum, str(img_emp))))
                    task.json_testerscreenshot = lst_file
            task.save()
           
            msg_success = "Task added successfully"
            return render(request, 'TLprojecttasks.html', {'msg_success':msg_success})
        else:
            
            request.session['splitid']=id
            mem = user_registration.objects.filter(id=tlid)
            mem1 = test_status.objects.filter(subtask_id=id)
            mem2 = tester_status.objects.filter(tester_id=tlid)
            time=datetime.now()
            taskstatus = test_status.objects.all()
            display = project_taskassign.objects.filter(tl_id=tlid).filter(project_id=id)
            tasks = project_taskassign.objects.filter(project_id=id, developer_id = tlid)
            mem3 = user_registration.objects.get(id=tlid)
            display1=mem3.fullname
           
            return render(request, 'TLprojecttasks.html',{'display1':display1,'time':time,'display':display,'mem':mem,'mem1':mem1,'mem2':mem2,'taskstatus':taskstatus,'tasks':tasks})
    else:
        return redirect('/')

def extensionsave(request,id):
    if request.method == 'POST':
        task = project_taskassign.objects.get(id=id)
        task.extension = request.POST['days']
        task.reason = request.POST['reason']
        task.extension_date = datetime.now()
        task.extension_status = "submitted"
        task.save()
        base_url = reverse('tlprojecttasks', kwargs={'id': task.project_id})
        query_string = urlencode({'id': task.project_id})
        url = '{}?{}'.format(base_url, query_string)
    return redirect(url)
    
 
def tlprojectsave(request,id):
    if request.method == 'POST':
        task = project_taskassign.objects.get(id=id)
        task.progress= request.POST['progress']
        task.projectstatus = request.POST['prostatus']
        task.save()
        base_url = reverse('tlsplittask', kwargs={'id':id})
        query_string = urlencode({'id':id})
        url = '{}?{}'.format(base_url, query_string)
    return redirect(url)

def pdetailsave(request,id):
    if request.method == 'POST':
        task = project_taskassign.objects.get(id=id)
        task.progress= request.POST['progress']
        task.project_status = request.POST.get('status')
        task.save()
        base_url = reverse('tlprojecttasks', kwargs={'id': task.project_id})
        query_string = urlencode({'id': task.project_id})
        url = '{}?{}'.format(base_url, query_string)
    return redirect(url)

def extensionapprove(request,id):

    task = project_taskassign.objects.get(id=id)
    task.extension_status = "Approved"
    task.extension_date = datetime.now()
    task.save()
    base_url = reverse('tlsplittask', kwargs={'id': id})
    query_string =  urlencode({'id': id})
    url = '{}?{}'.format(base_url, query_string)
    return redirect(url)
    
    

def extensionreject(request,id):
  
    task = project_taskassign.objects.get(id=id)
    task.extension_status = "Rejected"
    task.extension_date = datetime.now()
    task.save()
    base_url = reverse('tlsplittask', kwargs={'id': id})
    query_string =  urlencode({'id': id})
    url = '{}?{}'.format(base_url, query_string)
    return redirect(url)
    
 

def tltaskstatus(request,id):
    if 'tlid' in request.session:
        if request.session.has_key('tlid'):
            tlid = request.session['tlid']
        else:
            return redirect('/')
       
        
            
    else:
        return redirect('/')
    
def tlsplittask(request,id):
        if 'tlid' in request.session:
            if request.session.has_key('tlid'):
                tlid = request.session['tlid']
            else:
                return redirect('/')
            splitid = request.session['splitid']
            sub1 = project_taskassign.objects.get(id=id)
            test = test_status.objects.all()
            tester = tester_status.objects.all()
            mem = user_registration.objects.filter(id=tlid)
            sub = project_taskassign.objects.filter(~Q(developer_id=tlid)).filter(project_id=splitid,tl_id=tlid) 
            return render(request, 'TLsplittask.html',{'mem':mem,'sub':sub,'sub1':sub1,'test':test,'tester':tester})
        else:
            return redirect('/') 

def tlgivetask(request):
    if 'tlid' in request.session:
        if request.session.has_key('tlid'):
            tlid = request.session['tlid']
        else:
            return redirect('/')
        splitid = request.session['splitid']
      
        mem = user_registration.objects.filter(id=tlid)
        dept_id = user_registration.objects.get(id=tlid)
       
        e = designation.objects.get(designation="tester")
        dev_id = designation.objects.get(designation="developer")
        e1 = e.id
        spa = user_registration.objects.filter(tl_id=dept_id.id, status="active")
        spa1 = user_registration.objects.filter(designation_id=e1)
        time=datetime.now().date()
        tasks = project_taskassign.objects.filter(tl_id=tlid,project_id=splitid).values('task').distinct()
        new = project.objects.get(id=splitid)
        
        if request.method =='POST':
            
            var = project_taskassign()
           
            var.developer_id =  request.POST['ename']
            var.tl_id = tlid
            var.tester_id = request.POST['tname']
            var.tl_description=request.POST.get('description')
            var.subtask=request.POST.get('subtask')
            var.task = request.POST.get('task')
            var.startdate= time
            
            var.enddate= request.POST.get('date')
            bb= (var.startdate).strftime('%d-%m-%Y')
            
            cc= datetime.strptime(var.enddate, '%Y-%m-%d').strftime('%d-%m-%Y')
            var.files=request.FILES['files']
            var.extension=0
            var.project_id = splitid
            var.description = new.description
            var.save()
            # v = request.POST.get('ename')
            # em=user_registration.objects.get(id=v)
            # print(em.email)
            # subject = 'Greetings from iNFOX TECHNOLOGIES'
            # message = 'Congratulations,\n' \
            # 'You are assigned new project from iNFOX TECHNOLOGIES.\n' \
            # 'following is your Project Details\n'\
            # 'Project :'+str(var.project.project)+'\n' 'Task :'+str(var.task) +'\n' 'Description :'+str(var.tl_description)+'\n' 'SubTask :'+str(var.subtask)+'\n''Start Date :'+bb+'\n' 'End Date :'+cc+'\n'\
            # '\n' 'Complete your project on or before Enddate \n'\
            #     'NOTE : THIS IS A SYSTEM GENETATED MAIL PLEASE DO NOT REPLY' 
            # recepient = str(em.email)
            # send_mail(subject, message, EMAIL_HOST_USER,
            #       [recepient], fail_silently=False)
            msg_success = "Task split successfully"
            return render(request, 'TLgivetask.html',{'msg_success':msg_success})
        else:
            return render(request, 'TLgivetask.html',{'mem':mem,'spa':spa,'spa1':spa1,'time':time,'tasks':tasks})
    else:
        return redirect('/')

def TLattendance(request):
    if 'tlid' in request.session:
        if request.session.has_key('tlid'):
            tlid = request.session['tlid']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(id=tlid)
        return render(request, 'TLattendance.html',{'mem':mem})
    else:
        return redirect('/')

def TLattendancesort(request):
    if 'tlid' in request.session:
        if request.session.has_key('tlid'):
            tlid = request.session['tlid']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(id=tlid)
        if request.method == "POST":
            fromdate = request.POST.get('fromdate')
            todate = request.POST.get('todate') 
            # mem1 = attendance.objects.raw('select * from app_attendance where user_id and date between "'+fromdate+'" and "'+todate+'"')
            mem1 = attendance.objects.filter(date__range=[fromdate, todate]).filter(user_id=tlid)
        return render(request, 'TLattendancesort.html',{'mem1':mem1,'mem':mem})
    else:
        return redirect('/')   

def TLreportissues(request):
    if 'tlid' in request.session:
        if request.session.has_key('tlid'):
            tlid = request.session['tlid']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(id=tlid)
        return render(request, 'TLreportissues.html',{'mem':mem})
    else:
        return redirect('/') 

def TLreportissues(request):
    if 'tlid' in request.session:
        if request.session.has_key('tlid'):
            tlid = request.session['tlid']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(id=tlid)
        return render(request, 'TLreportissues.html',{'mem':mem})
    else:
        return redirect('/')   

def TLreportedissue1(request):
    if 'tlid' in request.session:
        if request.session.has_key('tlid'):
            tlid = request.session['tlid']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(id=tlid)
        var=reported_issue.objects.filter(reporter_id=tlid).order_by("-id")
        return render(request, 'TLreportedissue1.html',{'mem':mem,'var':var})
    else:
        return redirect('/')   

def TLreportedissue2(request,id):
    if 'tlid' in request.session:
        if request.session.has_key('tlid'):
            tlid = request.session['tlid']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(id=tlid)
        var=reported_issue.objects.filter(id=id)
        return render(request, 'TLreportedissue2.html',{'mem':mem,'var':var})
    else:
        return redirect('/')   
   
def TLreport1(request):
    if 'tlid' in request.session:
        if request.session.has_key('tlid'):
            tlid = request.session['tlid']
        else:
            return redirect('/')  
        mem1 = user_registration.objects.get(id=tlid)
        
        if request.method == 'POST':
            
            vars = reported_issue()
            vars.issue=request.POST.get('report')
            vars.reported_date=datetime.now()
            vars.reported_to_id=mem1.projectmanager_id
            vars.reporter_id=tlid
            vars.status='pending'
            vars.save()
            return redirect('TLreport1')
        else:
            mem = user_registration.objects.filter(id=tlid)
            return render(request, 'TLreport1.html',{'mem':mem})
    else:
        return redirect('/')

def devtlreported(request):
    if 'tlid' in request.session:
        if request.session.has_key('tlid'):
            tlid = request.session['tlid']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(id=tlid)
        var=reported_issue.objects.filter(reported_to_id=tlid).order_by("-id")
        return render(request, 'devtlreported.html',{'mem':mem,'var':var})
    else:
        return redirect('/')   
 
def TLreportsuccess(request):
    if 'tlid' in request.session:
        if request.session.has_key('tlid'):
            tlid = request.session['tlid']
        else:
            return redirect('/')    
        mem = user_registration.objects.filter(id=tlid)
        mem1 = user_registration.objects.get(id=tlid)
        if request.method == 'POST':
            
            vars = reported_issue()
            vars.issue=request.POST.get('report')
            vars.reported_date=datetime.now()
            vars.designation_id=mem1.designation_id
            vars.reporter_id=tlid
            vars.status='pending'
            vars.save()
        return render(request, 'TLreportsuccess.html',{'mem':mem})
    else:
        return redirect('/')


def TLtasks(request):
    if 'tlid' in request.session:
        if request.session.has_key('tlid'):
            tlid = request.session['tlid']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(id=tlid)
        task = tasks.objects.filter(user_id=tlid).order_by("-id")
        return render(request, 'TLtasks.html',{'mem':mem,'task':task})
    else:
        return redirect('/')
        
def TLtasksub(request,id):
    task = tasks.objects.get(id=id)
    task.status = "1"
    task.save()
    return redirect('TLtasks')

def TLtaskformsubmit(request,id):
    if 'tlid' in request.session:
        if request.session.has_key('tlid'):
            tlid = request.session['tlid']
        else:
           return redirect('/')
        mem = user_registration.objects.filter(id=tlid)
        if request.method == "POST":
            var = datetime.now().date()
            task = project_taskassign.objects.get(id=id)
            task.employee_description = request.POST['description']
            task.git_link = request.POST['gitlink']
            task.employee_files = request.FILES['scn']
            task.submitted_date = var
            task.status = 'submitted'
            x = task.enddate
            y = var
            event = Event.objects.values_list('start_time',flat=True)
            z = 0
            day_delta = timedelta(days=1)
            for i in range((var-task.enddate).days):
                n = (x + i*day_delta)
                if n in event:
                    z=z+1 
            delta = datetime.now().date() - task.enddate
            delay = delta.days - z
            if delay > 0:
                task.delay = delay
                task.save()
            else:
                task.delay = 0
                task.save()
            
        return render(request, 'TLsuccess.html', {'mem': mem, 'task': task})
    else:
        return redirect('/')

def TLleavereq(request):
    if 'tlid' in request.session:
        if request.session.has_key('tlid'):
            tlid = request.session['tlid']
        else:
           return redirect('/')
        mem = user_registration.objects.filter(id=tlid)
        return render(request, 'TLleavereq.html',{'mem':mem})
    else:
        return redirect('/')


def TLreqedleave(request):
    if 'tlid' in request.session:
        if request.session.has_key('tlid'):
            tlid = request.session['tlid']
        else:
           return redirect('/')
        mem = user_registration.objects.filter(id=tlid)
        var = leave.objects.filter(user_id=tlid)
        return render(request, 'TLreqedleave.html',{'var': var,'mem':mem})
    else:
        return redirect('/')

def tl_leave_form(request):
    if 'tlid' in request.session:
        if request.session.has_key('tlid'):
            tlid = request.session['tlid']
        else:
           return redirect('/')
        mem = user_registration.objects.filter(id=tlid)
        des1 = designation.objects.get(designation='team leader')
        if request.method == "POST":
            leaves = leave()
            leaves.from_date = request.POST['from']
            leaves.to_date = request.POST['to']
            leaves.leave_status = request.POST['haful']
            leaves.reason = request.POST['reason']
            leaves.user_id = tlid
            leaves.status = "submitted"
            leaves.designation_id = des1.id
            leaves.leaveapprovedstatus=0

            start = datetime.strptime(leaves.from_date, '%Y-%m-%d').date() 
            end = datetime.strptime(leaves.to_date, '%Y-%m-%d').date()

            diff = (end  - start).days
            
            cnt =  Event.objects.filter(start_time__range=(start,end)).count()
            
            if diff == 0:
                leaves.days = 1
            else:
                leaves.days = diff - cnt
            leaves.save()
        return render(request, 'TLleavereq.html',{'mem':mem})   
    else:
        return redirect('/')


def TLgivetasks(request,id):
    if 'tlid' in request.session:
        if request.session.has_key('tlid'):
            tlid = request.session['tlid']
        else:
           return redirect('/')
        mem = user_registration.objects.filter(id=tlid)
        time = datetime.now()
        task = project_taskassign.objects.filter(tl_id=tlid).filter(id=id)
        return render(request, 'TLgivetasks.html', {'mem': mem, 'task': task, 'time': time})
    else:
        return redirect('/')

def TLgavetask(request,id):
    if 'tlid' in request.session:
        if request.session.has_key('tlid'):
            tlid = request.session['tlid']
        else:
           return redirect('/')
        mem = user_registration.objects.filter(id=tlid)
        task = project_taskassign.objects.filter(tl_id=tlid).filter(id=id)
        return render(request, 'TLgavetask.html', {'mem': mem, 'task': task})
    else:
        return redirect('/')

def TLleave(request):
    if 'tlid' in request.session:
        if request.session.has_key('tlid'):
            tlid = request.session['tlid']
        else:
           return redirect('/')
        mem = user_registration.objects.filter(id=tlid)
        return render(request, 'TLleave.html',{'mem':mem})
    else:
        return redirect('/')


# ------------------------------------------------------------------------------------------------------

# tester module

def TSdashboard(request):
    if 'usernametsid' in request.session:
       
        if request.session.has_key('usernamets'):
            usernamets = request.session['usernamets']
        if request.session.has_key('usernamets1'):
            usernamets1 = request.session['usernamets1']
        else:
           return redirect('/')
        mem=user_registration.objects.filter(designation_id=usernamets).filter(fullname=usernamets1)
        return render(request,'TSdashboard.html',{'mem':mem})
    else:
        return redirect('/')

def TStask(request):
    if 'usernametsid' in request.session:

        if request.session.has_key('usernamets'):
            usernamets = request.session['usernamets']
        if request.session.has_key('usernamets1'):
            usernamets1 = request.session['usernamets1']
        if request.session.has_key('usernametsid'):
            usertsid = request.session['usernametsid']
        else:
            return redirect('/')
        mem=user_registration.objects.filter(designation_id=usernamets).filter(fullname=usernamets1)
        task = tasks.objects.filter(user_id=usertsid).order_by("-id")
        return render(request,'TStask.html',{'mem':mem,'tasks':task})
    else:
        return redirect('/')


def testasksub(request,id):
    
    task = tasks.objects.get(id=id)
    task.status = "1"
    task.save()
    return redirect('TStask')
        
def TSproject(request):
    if 'usernametsid' in request.session:
        if request.session.has_key('usernamets'):
            usernamets = request.session['usernamets']
        if request.session.has_key('usernamets1'):
            usernamets1 = request.session['usernamets1']
        if request.session.has_key('usernametsid'):
            usertsid = request.session['usernametsid']
        else:
           return redirect('/')
        mem=user_registration.objects.filter(designation_id=usernamets) .filter(fullname=usernamets1)
        pros = project_taskassign.objects.filter(tester=usertsid).values('project_id').distinct()
        new = project.objects.all()
 
        return render(request,'TSproject.html',{'mem':mem,'pros':pros,'new':new})
    else:
        return redirect('/')

def TSprojectdetails(request,pid):
    if 'usernametsid' in request.session:
        if request.session.has_key('usernamets'):
            usernamets = request.session['usernamets']
        if request.session.has_key('usernamets1'):
            usernamets1 = request.session['usernamets1']
        if request.session.has_key('usernametsid'):
            usertsid = request.session['usernametsid']
        else:
           return redirect('/')
    

        mem=user_registration.objects.filter(designation_id=usernamets) .filter(fullname=usernamets1)
        var = project_taskassign.objects.filter(project=pid,tester_id=usertsid).order_by('-id')
        data = tester_status.objects.filter(project_id=pid)
        data1 = test_status.objects.filter(project_id=pid)

        date1= datetime.now()
        return render(request,'TSprojectdetails.html',{'date1':date1,'mem':mem,'var':var,'data':data,'data1':data1})
    else:
        return redirect('/')

def testersave(request,uid,pid):

    if request.session.has_key('usernametsid'):
        usertsid = request.session['usernametsid']
    else:
        return redirect('/')
    pr = project_taskassign.objects.get(id=pid)
    user = user_registration.objects.get(id=uid)
    if request.method == 'POST':
        test = tester_status()
        test.tester_id = usertsid
        test.date = datetime.now()
        test.project_id = pr.project_id
        test.user_id = user.id
        test.progress = pr.progress
        test.subtask_id = pid
        test.workdone = request.POST.get('workdone')
        test.files = request.FILES['files']
        test.save()
        base_url = reverse('TSprojectdetails', kwargs={'pid': test.project_id})
        query_string = urlencode({'pid': test.project_id})
        url = '{}?{}'.format(base_url, query_string)
        return redirect(url)



def projectdetailsave(request,uid,pid):
    if request.session.has_key('usernametsid'):
        usertsid = request.session['usernametsid']
    else:
       return redirect('/')
    if request.method == 'POST':
        
        user = project_taskassign.objects.get(developer_id=uid,id=pid)
        user.progress = request.POST.get('dprogress')
        user.projectstatus = request.POST.get('sp')
        user.save()
        base_url = reverse('TSprojectdetails', kwargs={'pid': user.project_id})
        query_string = urlencode({'pid': user.project_id})
        url = '{}?{}'.format(base_url, query_string)
        return redirect(url)


def TSassigned(request,id):
    if 'usernametsid' in request.session:
        if request.session.has_key('usernamets'):
            usernamets = request.session['usernamets']
        if request.session.has_key('usernamets1'):
            usernamets1 = request.session['usernamets1']
        else:
           return redirect('/')
        
        data = project_taskassign.objects.get(id=id)
        mem=user_registration.objects.filter(designation_id=usernamets) .filter(fullname=usernamets1)
        return render(request,'TSassigned.html',{'mem':mem,'data':data})
    else:
        return redirect('/')

def TSsubmitted(request,id):
    if 'usernametsid' in request.session:
        if request.session.has_key('usernamets'):
            usernamets = request.session['usernamets']
        if request.session.has_key('usernamets1'):
            usernamets1 = request.session['usernamets1']
        else:
           return redirect('/')
        
        var = project_taskassign.objects.get(id=id)
        mem=user_registration.objects.filter(designation_id=usernamets) .filter(fullname=usernamets1)
        return render(request,'TSsubmitted.html',{'mem':mem,'var':var})
    else:
        return redirect('/')

def TSsubmittedsave(request,id):
    if 'usernametsid' in request.session:
        if request.method =='POST':
            
            a = project_taskassign.objects.get(id=id)
            a.employee_description = request.POST.get('empdescription')
            a.employee_files = request.FILES.get('empfile')
            a.submitted_date = datetime.now()
            a.status = "submitted"
            a.save()
            return redirect('TStask')
        else:
            pass
    else:
        return redirect('/')


def TSsucess(request):
    if 'usernametsid' in request.session:
        if request.session.has_key('usernamets'):
            usernamets = request.session['usernamets']
        if request.session.has_key('usernamets1'):
            usernamets1 = request.session['usernamets1']
        else:
           return redirect('/')
        mem=user_registration.objects.filter(designation_id=usernamets) .filter(fullname=usernamets1)
        return render(request,'TSsucess.html',{'mem':mem})
    else:
        return redirect('/')

# -----------------------------------------------------------------------------------------------------------------------------------------

# developer module

def devindex(request):
    if request.session.has_key('devid'):
        devid = request.session['devid']
    else:
       return redirect('/')
    dev = user_registration.objects.filter(id=devid)
    return render(request, 'devindex.html', {'dev': dev})


def devdashboard(request):
    if request.session.has_key('devid'):
        devid = request.session['devid']
    else:
       return redirect('/')
    dev = user_registration.objects.filter(id=devid)
    labels = []
    data = []
    queryset = user_registration.objects.filter(id=devid)
    for i in queryset:
            labels=[i.workperformance,i.attitude,i.creativity]
            data=[i.workperformance,i.attitude,i.creativity]
    return render(request, 'devdashboard.html', {'labels':labels,'data':data,'dev': dev})


def devReportedissues(request):
    if 'devid' in request.session:    
        if request.session.has_key('devid'):
            devid = request.session['devid']
    
        else:
           return redirect('/')
        dev = user_registration.objects.filter(id=devid)
        return render(request,'devReportedissues.html',{'dev':dev})
    else:
        return redirect('/')


def devreportissue(request):
    if 'devid' in request.session:
        if request.session.has_key('devid'):
            devid = request.session['devid']
    
        else:
           return redirect('/')
        dev = user_registration.objects.filter(id=devid)
        var=reported_issue.objects.filter(reporter_id=devid).order_by("-id")    
        return render(request,'devreportissue.html',{'var':var,'dev':dev})
    else:
        return redirect('/')


def devreportedissue(request):
    if 'devid' in request.session:
        if request.session.has_key('devid'):
            devid = request.session['devid']
    
        else:
           return redirect('/')
        
        var=reported_issue.objects.filter(reporter_id=devid)  
        dev = user_registration.objects.filter(id=devid)  
        return render(request,'devreportedissue.html',{'var':var,'dev':dev})
    else:
        return redirect('/')


def devsuccess(request):
    if 'devid' in request.session:
        if request.session.has_key('devid'):
            devid = request.session['devid']
        
        dev = user_registration.objects.filter(id=devid)
        tl = user_registration.objects.get(id=devid)
        if request.method == 'POST':           
            vars = reported_issue()
            vars.issue=request.POST.get('reportissue')
            vars.reported_date=datetime.now()
            vars.reported_to_id=tl.tl_id
            vars.reporter_id=devid
            vars.status='pending'
            vars.save()
        return render(request,'devsuccess.html',{'dev':dev})
    else:
        return redirect('/')


def devissues(request,id):
    if request.session.has_key('devid'):
        devid = request.session['devid']
    else:
       return redirect('/')
    dev = user_registration.objects.filter(id=devid)
    man = reported_issue.objects.filter(id=id)
    return render(request, 'devissues.html', {'dev': dev,'man':man})


def devsample(request):
    if request.session.has_key('devid'):
        devid = request.session['devid']
    else:
       return redirect('/')
    dev = user_registration.objects.filter(id=devid)
    return render(request, 'devsample.html', {'dev': dev})


# *********************praveesh*********************


def Devapplyleav(request):
    if request.session.has_key('devid'):
        devid = request.session['devid']
    else:
       return redirect('/')
    dev = user_registration.objects.filter(id=devid)
    return render(request, 'Devapplyleav.html', {'dev': dev})


def dev_leave_form(request):
    des1 = designation.objects.get(designation='developer')
    if request.method == "POST":
        leaves = leave()
        leaves.from_date = request.POST['from']
        leaves.to_date = request.POST['to']
        leaves.leave_status = request.POST['haful']
        leaves.reason = request.POST['reason']
        leaves.leaveapprovedstatus=0
        leaves.user_id = request.POST['dev_id']
        leaves.designation_id = des1.id

        start = datetime.strptime(leaves.from_date, '%Y-%m-%d').date() 
        end = datetime.strptime(leaves.to_date, '%Y-%m-%d').date()

        diff = (end  - start).days
        
        cnt =  Event.objects.filter(start_time__range=(start,end)).count()
        
        if diff == 0:
            leaves.days = 1
        else:
            leaves.days = diff - cnt
        leaves.save()
        return render(request, 'Devapplyleav.html')
    else:
        return render(request, 'Devapplyleav1.html')


def Devapplyleav1(request):
    if request.session.has_key('devid'):
        devid = request.session['devid']
    else:
       return redirect('/')
    dev = user_registration.objects.filter(id=devid)
    return render(request, 'Devapplyleav1.html', {'dev': dev})


def Devapplyleav2(request):
    if request.session.has_key('devid'):
        devid = request.session['devid']
    else:
       return redirect('/')
    dev = user_registration.objects.filter(id=devid)
    return render(request, 'Devapplyleav2.html', {'dev': dev})


def Devleaverequiest(request):
    if request.session.has_key('devid'):
        devid = request.session['devid']
    else:
       return redirect('/')
    devl = leave.objects.filter(user_id=devid)
    dev = user_registration.objects.filter(id=devid)
    return render(request, 'Devleaverequiest.html', {'dev': dev, 'devl': devl})

def Devattendance(request):
    if 'devid' in request.session:
        if request.session.has_key('devid'):
            devid = request.session['devid']
        else:
           return redirect('/')
        dev = user_registration.objects.filter(id=devid)
        return render(request, 'Devattendance.html', {'dev': dev})
    else:
        return redirect('/')

def Devattendancesort(request):
    if 'devid' in request.session:
        if request.session.has_key('devid'):
            devid = request.session['devid']
        else:
           return redirect('/')
        dev = user_registration.objects.filter(id=devid)
        if request.method == "POST":
            fromdate = request.POST.get('fromdate')
            todate = request.POST.get('todate') 
            mem1 = attendance.objects.filter(date__range=[fromdate, todate]).filter(user_id=devid)          
        return render(request, 'Devattendancesort.html',{'dev':dev,'mem1':mem1})
        
    else:
        return redirect('/')


def Tattend(request):
    if request.session.has_key('devid'):
        devid = request.session['devid']
    else:
       return redirect('/')
    dev = user_registration.objects.filter(id=devid)
    return render(request, 'Tattend.html', {'dev': dev})


def Devapplyleav3(request):
    if request.session.has_key('devid'):
        devid = request.session['devid']
    else:
       return redirect('/')
    dev = user_registration.objects.filter(id=devid)
    return render(request, 'Devapplyleav3.html', {'dev': dev})


# **************************maneesh*******************************


def DEVprojects(request):
    if request.session.has_key('devid'):
        devid = request.session['devid']
    else:
       return redirect('/')
    dev = user_registration.objects.filter(id=devid)
    pros = project.objects.all()
    devp = project_taskassign.objects.filter(developer_id=devid).values('project_id').distinct()
    return render(request, 'DEVprojects.html', {'dev': dev, 'devp': devp, 'pros': pros})


def DEVtable(request, id):
    if request.session.has_key('devid'):
        devid = request.session['devid']
    else:
       return redirect('/')
    dev = user_registration.objects.filter(id=devid)
    devp = project_taskassign.objects.filter(project_id=id).filter(developer_id=devid).order_by("-id")
    teststatus = test_status.objects.all()
    testerstatus = tester_status.objects.filter(project_id=id)
    time = datetime.now()
    return render(request, 'DEVtable.html', {'dev': dev, 'devp': devp, 'time': time, 'teststatus': teststatus, 'testerstatus': testerstatus})


def DEVtaskstatus(request, id):
    if request.session.has_key('devid'):
        devid = request.session['devid']
    else:
       return redirect('/')
    dev = user_registration.objects.filter(id=devid)
    mem = project_taskassign.objects.get(id=id)
    if request.method == 'POST':
        task = test_status()
        task.date = datetime.now()
        task.workdone = request.POST['workdone']
        task.git_commit = request.POST['gitcommit']
        task.git_link = request.POST['gitlink']
        task.user_id = devid
        task.subtask_id = mem.id
        task.project_id = mem.project_id
        dct_file = dict(request.FILES)
        lst_screenshot = dct_file['filed']
        lst_file = []
        for ins_screenshot in lst_screenshot:
            str_img_path = ""
            if ins_screenshot:
                img_emp = ins_screenshot
                fs = FileSystemStorage(location=settings.MEDIA_ROOT,base_url=settings.MEDIA_URL)
                str_img = fs.save(''.join(filter(str.isalnum, str(img_emp))), img_emp)
                str_img_path = fs.url(''.join(filter(str.isalnum, str_img)))
                lst_file.append('/media/'+''.join(filter(str.isalnum, str(img_emp))))
                task.json_testerscreenshot = lst_file
        task.save()
       
        base_url = reverse('DEVtable', kwargs={'id': task.project_id})
        query_string = urlencode({'id': task.project_id})
        url = '{}?{}'.format(base_url, query_string)
        return redirect(url)

def DEVextension(request, id):
    if request.session.has_key('devid'):
        devid = request.session['devid']
    else:
       return redirect('/')
    dev = user_registration.objects.filter(id=devid)
    mem = project_taskassign.objects.get(id=id)
    if request.method == 'POST':
        ext = project_taskassign.objects.get(id=id)
        ext.extension = request.POST['dayz']
        ext.reason = request.POST['reason']
        ext.extension_date = datetime.now()
        ext.extension_status = "submitted"
        ext.save()
        base_url = reverse('DEVtable', kwargs={'id': ext.project_id})
        query_string = urlencode({'id': ext.project_id})
        url = '{}?{}'.format(base_url, query_string)
        return redirect(url)
        
def devprjsave(request,id):
    if request.method == 'POST':
       
        ext = project_taskassign.objects.get(id=id)
        ext.progress = request.POST['devpro']
        ext.projectstatus = request.POST['devstat']
        ext.save()
        base_url = reverse('DEVtable', kwargs={'id': ext.project_id})
        query_string = urlencode({'id': ext.project_id})
        url = '{}?{}'.format(base_url, query_string)
        return redirect(url)
       


def DEVtaskmain(request):
    if 'devid' in request.session:
        if request.session.has_key('devid'):
            devid = request.session['devid']
        else:
            return redirect('/')
        dev = user_registration.objects.filter(id=devid)
        task = tasks.objects.filter(user_id=devid).order_by("-id")
        return render(request,'DEVtaskmain.html', {'dev':dev,'task':task})
    else:
        return redirect('/')


def devtasksub(request,id):
    
    task = tasks.objects.get(id=id)
    task.status = "1"
    task.save()
    return redirect('DEVtaskmain')


def DEVtaskform(request, id):
    if request.session.has_key('devid'):
        devid = request.session['devid']
    else:
       return redirect('/')
    time = datetime.now()
    dev = user_registration.objects.filter(id=devid)
    task = project_taskassign.objects.filter(developer_id=devid).filter(id=id)
    return render(request, 'DEVtaskform.html', {'dev': dev, 'task': task, 'time': time})

def DEVtaskformsubmit(request, id):
    if request.session.has_key('devid'):
        devid = request.session['devid']
    else:
       return redirect('/')
    dev = user_registration.objects.filter(id=devid)
    if request.method == "POST":
        task = project_taskassign.objects.get(id=id)
        task.employee_description = request.POST['description']
        task.git_link = request.POST['gitlink']
        task.employee_files = request.FILES['scn']
        task.submitted_date = datetime.now().date()
        task.status = 'submitted'
        var = datetime.now().date()
        x = task.enddate
        y = var
        delta = y - x
        for i in range(delta.days + 1):
            day = x + timedelta(days=i)
        event = Event.objects.values_list('start_time',flat=True)
        z = 0
        for i in event:
            if i in event:
                z=z+1
        delta = datetime.now().date() - task.enddate
        delay = delta.days - z
        if delay > 0:
            task.delay = delay
            task.save()
            
        else:
            task.delay = 0
            task.save()
    return render(request, 'DEVtasksumitted.html', {'dev': dev, 'task': task})

def DEVtask(request, id):
    if request.session.has_key('devid'):
        devid = request.session['devid']
    else:
       return redirect('/')
    dev = user_registration.objects.filter(id=devid)
    task = project_taskassign.objects.filter(developer_id=devid).filter(id=id)
    return render(request, 'DEVtask.html', {'dev': dev, 'task': task})


def dev_task_submit(request):
    if request.session.has_key('devid'):
        devid = request.session['devid']
    else:
       return redirect('/')
    if request.method == "POST":
        dpid = request.POST.get('dpid')
        member = project_taskassign.objects.get(id=dpid)
        member.employee_description=request.POST['workdone']
        member.save()
        return redirect('DEVtable')


def DEVsuccess(request):
    if request.session.has_key('devid'):
        devid = request.session['devid']
    else:
       return redirect('/')
    dev = user_registration.objects.filter(id=devid)
    return render(request, 'DEVsuccess.html', {'dev': dev})

def DEVtasksumitted(request):
    if request.session.has_key('devid'):
        devid = request.session['devid']
    else:
       return redirect('/')
    dev = user_registration.objects.filter(id=devid)
    return render(request, 'DEVtasksumitted.html', {'dev': dev})
    
    
    
    
    
    
    
    # **********************internship****************
    
def man_internship_view(request):
    if request.session.has_key('m_id'):
        m_id = request.session['m_id']
    else:
        return redirect('/')    
    mem = user_registration.objects.filter(id=m_id)
    return render(request,'man_internship_view.html',{'mem':mem})
    
def BRadmin_internship_view(request):
    if request.session.has_key('Adm_id'):
        Adm_id = request.session['Adm_id']
    else:
        return redirect('/')    
    Adm = user_registration.objects.filter(id=Adm_id)
    return render(request,'BRadmin_internship_view.html',{'Adm':Adm})

def registrationview(request):
    if request.session.has_key('Adm_id'):
        Adm_id = request.session['Adm_id']
    else:
        return redirect('/')    
    Adm = user_registration.objects.filter(id=Adm_id)
    return render(request,'registrationview.html',{'Adm':Adm})

def registrationviewman(request):
    if request.session.has_key('m_id'):
        m_id = request.session['m_id']
    else:
        return redirect('/')    
    mem = user_registration.objects.filter(id=m_id)
    return render(request,'registrationviewman.html',{'mem':mem})

def BRadmin_internship(request):
    if request.session.has_key('Adm_id'):
        Adm_id = request.session['Adm_id']
    else:
        return redirect('/')    
    Adm = user_registration.objects.filter(id=Adm_id)

    var1=internship.objects.all().order_by("-id")
    return render(request,'BRadmin_internship.html',{'var1':var1,'Adm':Adm})
    
def man_internship(request):
    if request.session.has_key('m_id'):
        m_id = request.session['m_id']
    else:
        return redirect('/')    
    mem = user_registration.objects.filter(id=m_id) 
    var1=internship.objects.all().order_by("-id")
    return render(request,'man_internship.html',{'var1':var1,'mem':mem})

def man_internship_date(request):
    if request.session.has_key('m_id'):
        m_id = request.session['m_id']
    else:
        return redirect('/')    
    mem = user_registration.objects.filter(id=m_id)
    newdata1 = internship.objects.all().values('reg_date').distinct()
    return render(request,'man_internship_date.html',{'mem':mem,'newdata':newdata1})
    
def man_internship_dateview(request):
    if request.session.has_key('m_id'):
        m_id = request.session['m_id']
    else:
        return redirect('/')    
    mem = user_registration.objects.filter(id=m_id)
    reg_date=request.GET.get('reg_date')
    empid1=internship.objects.filter(reg_date=reg_date)
    return render(request,'man_internship_dateview.html',{'mem':mem,'data':empid1})

def BRadmin_internship_date(request):
    if request.session.has_key('Adm_id'):
        Adm_id = request.session['Adm_id']
    else:
        return redirect('/')    
    Adm = user_registration.objects.filter(id=Adm_id)
    newdata = internship.objects.all().values('reg_date').distinct()
    return render(request,'BRadmin_internship_date.html',{'Adm':Adm,'newdata':newdata})
    
def BRadmin_internship_dateview(request):
    if request.session.has_key('Adm_id'):
        Adm_id = request.session['Adm_id']
    else:
        return redirect('/')    
    Adm = user_registration.objects.filter(id=Adm_id)
    reg_date=request.GET.get('date')
    empid=internship.objects.filter(reg_date=reg_date)
    return render(request,'BRadmin_internship_dateview.html',{'Adm':Adm,'data':empid})
    

def BRadmin_internship_update(request,id):
    if request.session.has_key('Adm_id'):
        Adm_id = request.session['Adm_id']
    else:
        return redirect('/')    
    Adm = user_registration.objects.filter(id=Adm_id)
    var = internship.objects.get(id=id)
    return render(request,'BRadmin_internship_update.html',{'var':var,'Adm':Adm})
    
def render_pdf_view(request,id):

    date = datetime.now()   
    mem = internship.objects.get(id=id)
    template_path = 'pdf.html'
    context = {'mem': mem,
    'media_url':settings.MEDIA_URL,
    'date':date
    }
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    # response['Content-Disposition'] = 'attachment; filename="certificate.pdf"'
    response['Content-Disposition'] = 'filename="certificate.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
       html, dest=response)
    


    # if error then show some funy view
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response


    
def internshipupdatesave(request,id):
    if request.session.has_key('Adm_id'):
        Adm_id = request.session['Adm_id']
    else:
        return redirect('/')    
    Adm = user_registration.objects.filter(id=Adm_id)
    var = internship.objects.get(id=id)
    var.fullname = request.POST['fullname']
    var.collegename = request.POST['college']
    var.reg_no = request.POST['regno']
    var.course = request.POST['course']
    var.stream = request.POST['stream']        
    var.platform = request.POST['platform']        
    # var.branch_id  =  request.POST['branch']        
    var.start_date =  request.POST['startdate']        
    var.end_date  =  request.POST['enddate']        
    var.mobile  =  request.POST['mobile']        
    var.alternative_no  =  request.POST['altmob']        
    var.email = request.POST['email']
    var.hrmanager = request.POST['hrmanager']
    var.guide = request.POST['guide']
    var.rating = request.POST['rating']
    
    if request.FILES.get('profile_pic') is not None:
         var.profile_pic  =  request.FILES['profile_pic']
    var.save()
    return redirect('BRadmin_internship')

def interndelete(request,id):
    man = internship.objects.get(id=id)
    man.delete()
    return redirect('BRadmin_internship')

def maninterndelete(request,id):
    man1 = internship.objects.get(id=id)
    man1.delete()
    return redirect('man_internship')


def certificate_intrn(request,id):

    date = datetime.now()   
    mem = internship.objects.get(id=id)
    mems = internship.objects.filter(id=id)
    template_path = 'certificate_intrn.html'
    context = {'mem': mem, 'mems': mems,
    'media_url':settings.MEDIA_URL,
    'date':date
    }
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    # response['Content-Disposition'] = 'attachment; filename="certificate.pdf"'
    response['Content-Disposition'] = 'filename="certificate.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
       html, dest=response)
       

# *****************************registration********


# def man_registration_update(request,id):
#     if 'Adm_id' in request.session:
#         if request.session.has_key('Adm_id'):
#             Adm_id = request.session['Adm_id']
#         else:
#             return redirect('/')    
#         Adm = user_registration.objects.filter(id=Adm_id)
        
#         mem4 = user_registration.objects.get(id=id)
#         con = conditions.objects.get(id=1)
#         xem = extracurricular.objects.get(user_id=id)
#         qem = qualification.objects.get(user_id=id)
#         des = designation.objects.filter(~Q(designation='admin'))
        
#         admins = user_registration.objects.get(id=Adm_id)
        
#         br_name = branch_registration.objects.get(id=admins.id)
        
#         return render(request,'man_registration_update.html',{'con':con,'mem4':mem4,'qem':qem,'xem':xem,'Adm':Adm, 'des':des, 'br_name':br_name})
#     else:
#         return redirect('/')

def man_registration_update(request, id):
    if 'Adm_id' in request.session:
        if request.session.has_key('Adm_id'):
            Adm_id = request.session['Adm_id']
        else:
            return redirect('/')
        Adm = user_registration.objects.filter(id=Adm_id)

        mem4 = user_registration.objects.get(id=id)
        con = conditions.objects.get(id=1)
        xem = extracurricular.objects.get(user_id=id)
        qem = qualification.objects.get(user_id=id)
        des = designation.objects.filter(~Q(designation='admin'))
        desig = designation.objects.all().exclude(designation = 'team leader').exclude(designation ='manager').exclude(designation ='trainee').exclude(designation ='project manager').exclude(designation ='tester').exclude(designation ='trainingmanager').exclude(designation ='account').exclude(designation ='trainer').exclude(designation ='developer')

        admins = user_registration.objects.get(id=Adm_id)

        br_name = branch_registration.objects.get(id=admins.id)

        return render(request, 'man_registration_update.html', {'con': con, 'mem4': mem4, 'qem': qem, 'xem': xem, 'Adm': Adm, 'des': des, 'br_name': br_name, 'desig':desig})
    else:
        return redirect('/')

def man_registration(request):
    if request.session.has_key('m_id'):
        m_id = request.session['m_id']
    else:
        return redirect('/')    
    mem = user_registration.objects.filter(id=m_id)
    mem1 = user_registration.objects.all().order_by("-id")
    return render(request,'man_registration.html',{'mem':mem,'mem1':mem1})
    
def BRadmin_registration(request):
    if request.session.has_key('Adm_id'):
        Adm_id = request.session['Adm_id']
    else:
        return redirect('/')   
    if request.method=="POST":
        u_id = request.POST.get("id")
        dept_id = request.POST.get("dept")
        desi_id = request.POST.get("des")
        res = request.POST.get("stat")
   
        user = user_registration.objects.get(id=u_id)
        user.department_id = dept_id 
        user.status = res
        user.designation_id = desi_id
        user.save()
        return redirect("BRadmin_registration")
    Adm = user_registration.objects.filter(id=Adm_id)
    mem1 = user_registration.objects.filter(~Q(status="resigned")).order_by("-id")
    mem2 = designation.objects.filter(~Q(designation="admin"))
    mem3 = department.objects.all()
    return render(request,'BRadmin_registration.html',{'mem3':mem3,'mem2':mem2,'Adm':Adm,'mem1':mem1})

def BRadmin_resign(request):
    if request.session.has_key('Adm_id'):
        Adm_id = request.session['Adm_id']
    else:
        return redirect('/')    
    if request.method=="POST":
        u_id = request.POST.get("id")
        dept_id = request.POST.get("dept")
        desi_id = request.POST.get("des")
        user = user_registration.objects.get(id=u_id)
        user.department_id = dept_id 
        
        user.designation_id = desi_id
        user.save()
        return redirect("BRadmin_registration")
    Adm = user_registration.objects.filter(id=Adm_id)
    mem1 = user_registration.objects.filter(status="resigned").order_by("-id")
    mem2 = designation.objects.all()
    mem3 = department.objects.all()
    return render(request,'BRadmin_resign.html',{'mem3':mem3,'mem2':mem2,'Adm':Adm,'mem1':mem1})
    
def man_resign(request):
    if request.session.has_key('m_id'):
        m_id = request.session['m_id']
    else:
        return redirect('/')    
    if request.method=="POST":
        u_id = request.POST.get("id")
        dept_id = request.POST.get("dept")
        desi_id = request.POST.get("des")
        user = user_registration.objects.get(id=u_id)
        user.department_id = dept_id 
        
        user.designation_id = desi_id
        user.save()
        return redirect("BRadmin_registration")
    mem = user_registration.objects.filter(id=m_id)
    mem1 = user_registration.objects.filter(status="resigned").order_by("-id")
    mem2 = designation.objects.all()
    mem3 = department.objects.all()
    return render(request,'man_resign.html',{'mem3':mem3,'mem2':mem2,'mem':mem,'mem1':mem1})


def registrationupdatesave(request, id):
    a = user_registration.objects.get(id=id)
    b = qualification.objects.get(user_id=id)
    c = extracurricular.objects.get(user_id=id)
    d = conditions.objects.get(id=1)
    if request.method == 'POST':
        a.fullname = request.POST['name']
        a.fathername = request.POST['fathersname']
        a.mothername = request.POST['mothersname']
        a.presentaddress1 = request.POST['presentaddress1']
        a.presentaddress2 = request.POST['presentaddress2']
        a.presentaddress3 = request.POST['presentaddress3']
        a.pincode = request.POST['pincode']
        a.district = request.POST['district']
        a.state = request.POST['state']
        a.permanentaddress1 = request.POST['permanentaddress1']
        a.permanentaddress2 = request.POST['permanentaddress2']
        a.permanentaddress3 = request.POST['permanentaddress3']
        a.permanentpincode = request.POST['permanentpincode']
        a.permanentdistrict = request.POST['permanentdistrict']
        a.permanentstate = request.POST['permanentstate']
        a.designation_id = request.POST['designation']
        a.mobile = request.POST['mobile']
        a.alternativeno = request.POST['altmobile1']
        a.email = request.POST['email']
        a.hrmanager = request.POST['hrname']
        a.joiningdate = request.POST['dateofjoin']
        a.startdate = request.POST['startdate']
        a.enddate = request.POST['enddate']
        a.workperformance = request.POST['performance']
        a.hr_designation = request.POST['hrdesignation']
        if request.FILES.get('signature') is not None:
            a.signature = request.FILES['signature']
        a.save()

        b.user_id = a.id
        b.school = request.POST['school']
        b.schoolaggregate = request.POST['aggregate']
        b.ugdegree = request.POST['degree']
        b.ugstream = request.POST['stream']
        b.ugpassoutyr = request.POST['passoutyear']
        b.ugaggregrate = request.POST['aggregate1']
        b.pg = request.POST['pg']
        b.save()

        c.user_id = a.id
        c.internshipdetails = request.POST['details']
        c.internshipduration = request.POST['duration1']
        c.internshipcertificate = request.POST['certification']
        c.onlinetrainingdetails = request.POST['details1']
        c.onlinetrainingduration = request.POST['duration2']
        c.onlinetrainingcertificate = request.POST['certification1']
        c.projecttitle = request.POST['title']
        c.projectduration = request.POST['duration3']
        c.projectdescription = request.POST['description']
        c.projecturl = request.POST['url']
        c.skill1 = request.POST['skill1']
        c.skill2 = request.POST['skill2']
        c.skill3 = request.POST['skill3']
        c.save()
        d.condition1 = request.POST.get("condition1")
        d.condition2 = request.POST.get("condition2")
        d.condition3 = request.POST.get("condition3")
        d.condition4 = request.POST.get("condition4")
        d.condition5 = request.POST.get("condition5")
        d.condition6 = request.POST.get("condition6")
        d.save()
        return redirect('BRadmin_registration')
        
def registrationdelete(request,id):
    man = user_registration.objects.get(id=id)
  
    man1 = extracurricular.objects.get(user_id=man.id)
    man2 = qualification.objects.get(user_id=man.id)
    man2.delete()
    man1.delete()
    man.delete()
    os.remove(man.idproof.path)
    os.remove(man.photo.path)
    return redirect('BRadmin_registration')
    
#########################  trainee Payment New ######################

def trainee_payment(request):
    if 'usernametrns2' in request.session:
        
        if request.session.has_key('usernametrns2'):
            usernametrns2 = request.session['usernametrns2']
        z = user_registration.objects.filter(id=usernametrns2)
        return render(request,'trainee_payment.html',{'z':z})
    else:
        return redirect('/')

def trainee_payment_addpayment(request):
    if 'usernametrns2' in request.session:
        if request.session.has_key('usernametrns2'):
            usernametrns2 = request.session['usernametrns2']
        z = user_registration.objects.filter(id=usernametrns2)
        mem1 = user_registration.objects.get(id=usernametrns2)
        if request.method=="POST":
            ad=paymentlist()
            ad.amount_pay=request.POST['amount']
            ad.amount_date=request.POST['paymentdate']
            ad.amount_downlod=request.FILES['files']
            ad.current_date = datetime.now()
            ad.user_id=mem1
            ad.amount_status=0
            member = user_registration.objects.get(id=usernametrns2)
            co = course.objects.get(id = member.course_id)
            member.total_pay=int(request.POST['amount'])+member.total_pay
            member.payment_balance = co.total_fee - member.total_pay
            member.save()
            ad.save()
            return redirect('/trainee_payment')
        return render(request,'trainee_payment_addpayment.html',{'z':z})
    else:
        return redirect('/')

def trainee_payment_viewpayment(request):
    if 'usernametrns2' in request.session:
        
        if request.session.has_key('usernametrns2'):
            usernametrns2 = request.session['usernametrns2']
        
        z = user_registration.objects.filter(id=usernametrns2)
        mem=paymentlist.objects.filter(user_id = usernametrns2).order_by('-id')
        return render(request,'trainee_payment_viewpayment.html',{'z':z,'mem':mem})
                
    else:
        return redirect('/')


def accounts_leavehistory(request):
    if 'usernameacnt2' in request.session:
        if request.session.has_key('usernameacnt2'):
            usernameacnt2 = request.session['usernameacnt2']
        z = user_registration.objects.filter(id=usernameacnt2)
        cous = course.objects.all()
        dep = department.objects.all()
        des = designation.objects.all()
        emp = user_registration.objects.all()
        return render(request, 'accounts_leavehistory.html', {'z': z, 'cous': cous,'dep':dep,'des':des,'emp':emp})
    else:
        return redirect('/')



def accounts_leavehistory_department(request, id):
    if 'usernameacnt2' in request.session:
        if request.session.has_key('usernameacnt2'):
            usernameacnt2 = request.session['usernameacnt2']
        z = user_registration.objects.filter(id=usernameacnt2)
        var = department.objects.get(id=id)
        de = designation.objects.filter(~Q(designation='account'))
        return render(request, 'accounts_leavehistory_department.html', {'z': z, 'de': de, 'var': var})
    else:
        return redirect('/')


    
def accounts_leavehistory_employees(request, id, id1):
    if 'usernameacnt2' in request.session:
        if request.session.has_key('usernameacnt2'):
            usernameacnt2 = request.session['usernameacnt2']
        z = user_registration.objects.filter(id=usernameacnt2)
        var = user_registration.objects.filter(
            designation_id=id, department_id=id1)
        return render(request, 'accounts_leavehistory_employees.html', {'z': z, 'var': var})
    else:
        return redirect('/')
        

def accounts_emp_leavehistory(request, id):
    if 'usernameacnt2' in request.session:
        if request.session.has_key('usernameacnt2'):
            usernameacnt2 = request.session['usernameacnt2']
        z = user_registration.objects.filter(id=usernameacnt2)
        var = leave.objects.filter(user=id)
        return render(request, 'accounts_emp_leavehistory.html', {'z': z, 'var': var})
    else:
        return redirect('/')




def accounts_Dashboard(request):
    if 'usernameacnt2' in request.session:
        if request.session.has_key('usernameacnt2'):
            usernameacnt2 = request.session['usernameacnt2']
        z = user_registration.objects.filter(id=usernameacnt2)
        year = date.today().year
        month = date.today().month
        vars = vars = acntspayslip.objects.filter(~Q(fromdate__year=year,
                                          fromdate__month=month)).count()
        vars1 = user_registration.objects.filter(confirm_salary_status=1).count()
        des2 = designation.objects.get(designation='trainee')
        Adm1 = designation.objects.get(designation="Admin")
        vars2 = user_registration.objects.exclude(designation=des2.id).exclude(designation=Adm1.id).count()
        vars3 = acntspayslip.objects.filter(fromdate__year=year,
                                          fromdate__month=month).count()
        deta = user_registration.objects.filter(designation=des2.id,payment_status=0).count()
        deta2 = user_registration.objects.filter(designation=des2.id).count()
        deta2 = user_registration.objects.filter(designation=des2.id,).count()
        icount=internship.objects.all().count()
        return render(request, 'accounts_Dashboard.html', {'z': z,'vars':vars,'vars1':vars1,'vars2':vars2,'vars3':vars3,'deta':deta,'deta2':deta2,'icount':icount})
    else:
        return redirect('/')

# def account_accounts(request):
#     if 'usernameacnt2' in request.session:
#         if request.session.has_key('usernameacnt2'):
#             usernameacnt2 = request.session['usernameacnt2']
#         z = user_registration.objects.filter(id= usernameacnt2)
#         return render(request,'account_accounts.html', {'z': z})
#     else:
#         return redirect('/')

def account_accounts(request):
    if 'usernameacnt2' in request.session:
        if request.session.has_key('usernameacnt2'):
            usernameacnt2 = request.session['usernameacnt2']
        z = user_registration.objects.filter(id=usernameacnt2)
        return render(request, 'account_accounts.html', {'z': z})
    else:
        return redirect('/')

# def imagechange_accounts(request):
#     if 'usernameacnt2' in request.session:
#         if request.method == 'POST':
#             id = request.GET.get('id')
#             abc = user_registration.objects.get(id=id)
#             abc.photo = request.FILES['filenamees']
#             abc.save()
#             return redirect('account_accounts')
#         return render(request,'account_accounts.html' )
#     else:
#         return redirect('/')

def imagechange_accounts(request):
    if 'usernameacnt2' in request.session:
        if request.method == 'POST':
            id = request.GET.get('id')
            abc = user_registration.objects.get(id=id)
            abc.photo = request.FILES['filenamees']
            abc.save()
            return redirect('account_accounts')
        return render(request, 'account_accounts.html')
    else:
        return redirect('/')
        
def changepassword_accounts(request):
    if 'usernameacnt2' in request.session:
            if request.session.has_key('usernameacnt2'):
                usernameacnt2 = request.session['usernameacnt2']
            z = user_registration.objects.filter(id=usernameacnt2)
            if request.method == 'POST':
                abc = user_registration.objects.get(id=usernameacnt2)
                oldps = request.POST['currentPassword']
                newps = request.POST['newPassword']
                cmps = request.POST.get('confirmPassword')
                if oldps != newps:
                    if newps == cmps:
                        abc.password = request.POST.get('confirmPassword')
                        abc.save()
                        return render(request,'accounts_Dashboard.html', {'z': z})
                    return render(request,'changepassword_accounts.html', {'z': z})
                return render(request,'changepassword_accounts.html', {'z': z})
    else:
        return redirect('/')

def accounts_employee(request): 
    if 'usernameacnt2' in request.session:
        if request.session.has_key('usernameacnt2'):
            usernameacnt2 = request.session['usernameacnt2']
        z = user_registration.objects.filter(id=usernameacnt2) 
        des = department.objects.all()
        return render(request,'accounts_employee.html',{'des':des,'z' : z})
    else:
        return redirect('/')

def accounts_emp_dep(request,id):
    if 'usernameacnt2' in request.session:
        if request.session.has_key('usernameacnt2'):
            usernameacnt2 = request.session['usernameacnt2']
        z = user_registration.objects.filter(id=usernameacnt2)
        mem = department.objects.get(id=id)
        des=designation.objects.all()
        context = {'mem':mem,'des':des,'z' : z,}
        return render(request,'accounts_emp_dep.html', context)
    else:
        return redirect('/')

def accounts_emp_list(request,id,pk): 
    if 'usernameacnt2' in request.session:
        if request.session.has_key('usernameacnt2'):
            usernameacnt2 = request.session['usernameacnt2']
        z = user_registration.objects.filter(id=usernameacnt2)  
        mem = department.objects.get(id=id)
        mem1 = designation.objects.get(pk=pk)
        use=user_registration.objects.filter(department_id=mem.id,designation=mem1)
        context = {'use':use,'z' : z,}
        return render(request,'accounts_emp_list.html', context)
    else:
        return redirect('/')

def accounts_emp_details(request,id):  
    if 'usernameacnt2' in request.session:
        if request.session.has_key('usernameacnt2'):
            usernameacnt2 = request.session['usernameacnt2']
        z = user_registration.objects.filter(id=usernameacnt2)  
        vars=user_registration.objects.get(id=id)
        context = {'vars':vars,'z' : z,}
        return render(request,'accounts_emp_details.html', context)
    else:
        return redirect('/')

def accounts_payment(request):
    if 'usernameacnt2' in request.session:
        if request.session.has_key('usernameacnt2'):
            usernameacnt2 = request.session['usernameacnt2']
        z = user_registration.objects.filter(id=usernameacnt2)
        des = department.objects.all()
        return render(request,'accounts_payment.html', {'des' : des ,'z' : z,})
    else:
        return redirect('/')

def accounts_payment_dep(request,id): 
    if 'usernameacnt2' in request.session:
        if request.session.has_key('usernameacnt2'):
            usernameacnt2 = request.session['usernameacnt2']
        z = user_registration.objects.filter(id=usernameacnt2)
        mem = course.objects.get(id=id)
        des = designation.objects.all()
        context = {'mem':mem,'des':des,'z' : z,}
        return render(request,'accounts_payment_dep.html', context)
    else:
        return redirect('/')

def accounts_payment_list(request,id,pk):
    if 'usernameacnt2' in request.session:
        if request.session.has_key('usernameacnt2'):
            usernameacnt2 = request.session['usernameacnt2']
        z = user_registration.objects.filter(id=usernameacnt2) 
        mem = department.objects.get(id=id)
        mem1 = designation.objects.get(pk=pk)
        use=user_registration.objects.filter(department_id=mem.id,designation=mem1)
        context = {'use':use,'z' : z,}
        return render(request,'accounts_payment_list.html', context)
    else:
        return redirect('/')

def accounts_coursefee(request):
    if 'usernameacnt2' in request.session:
        if request.session.has_key('usernameacnt2'):
            usernameacnt2 = request.session['usernameacnt2']
        z = user_registration.objects.filter(id=usernameacnt2)
        mem=course.objects.all()
        return render(request,'accounts_coursefee.html',{'mem':mem,'z' : z,})
    else:
        return redirect('/')

def accounts_coursefee_addnew(request):
    if 'usernameacnt2' in request.session:
        if request.session.has_key('usernameacnt2'):
            usernameacnt2 = request.session['usernameacnt2']
        z = user_registration.objects.filter(id=usernameacnt2)
        mem=course()
        if request.method=="POST":
            mem.name=request.POST['coursename']
            mem.total_fee=request.POST['totalfee']
            try:
                user= course.objects.get(name=mem.name)
                context = {'msg': 'Course already exists!!!....  Try to add another course','z':z}
                return render(request,'accounts_coursefee_addnew.html',context)
            except :
                mem.save()
                return redirect('/accounts_coursefee')
        return render(request,'accounts_coursefee_addnew.html',{'z':z})
    else:
        return redirect('/')  

def coursefeeupdate(request,id):
    if 'usernameacnt2' in request.session:
        if request.session.has_key('usernameacnt2'):
            usernameacnt2 = request.session['usernameacnt2']
        z = user_registration.objects.filter(id=usernameacnt2)
        if request.method=="POST":
            abc=course.objects.get(id=id)
            abc.total_fee=request.POST['totalfee']
            abc.save()
            return redirect('accounts_coursefee')
        return render(request,'accounts_coursefee_addnew.html',{'z' : z,})
    else:
        return redirect('/')

def coursedelete(request,id):
    if 'usernameacnt2' in request.session:
        if request.session.has_key('usernameacnt2'):
            usernameacnt2 = request.session['usernameacnt2']
        z = user_registration.objects.filter(id=usernameacnt2)
        abc=course.objects.get(id=id)
        abc.delete()
        return redirect('accounts_coursefee')
    else:
        return redirect('/')

def accounts_registration_details(request):
    if 'usernameacnt2' in request.session:
        if request.session.has_key('usernameacnt2'):
            usernameacnt2 = request.session['usernameacnt2']
        z = user_registration.objects.filter(id=usernameacnt2)
        des = designation.objects.get(designation='trainee')
        deta = user_registration.objects.filter(designation=des.id)
        vars = paymentlist.objects.all()
        return render(request,'accounts_registration_details.html', { 'z' : z, 'deta':deta , 'vars':vars})
    else:
        return redirect('/')

def accounts_payment_detail_list(request, id):
    if 'usernameacnt2' in request.session:
        
        if request.session.has_key('usernameacnt2'):
            usernameacnt2 = request.session['usernameacnt2']
        
        else:
            return redirect('/')

        z = user_registration.objects.filter(id=usernameacnt2)

        a = user_registration.objects.get(id=id)
        
        pay = paymentlist.objects.filter(user_id_id = a.id).order_by('-id')
        
        return render(request,'accounts_payment_detail_list.html',{ 'z' : z, 'pay': pay , 'a':a })
    else:
        return redirect('/')

def verify(request,id):
    rem = paymentlist.objects.get(id=id)
    rem.amount_status = 1
    rem.save()
    return redirect('/accounts_registration_details')
    
def reminder(request,id):
    rem = user_registration.objects.get(id=id)
    rem.payment_status = 1
    rem.save()
    return redirect('/accounts_registration_details')

def accounts_expenses(request):
    if 'usernameacnt2' in request.session:
        if request.session.has_key('usernameacnt2'):
            usernameacnt2 = request.session['usernameacnt2']
        z = user_registration.objects.filter(id=usernameacnt2)
        vars=acntexpensest.objects.all()
        return render(request,'accounts_expenses.html',{'z':z, 'vars':vars})
    else:
        return redirect('/')

def accounts_expenses_viewEdit(request,id):
    if 'usernameacnt2' in request.session:
        if request.session.has_key('usernameacnt2'):
            usernameacnt2 = request.session['usernameacnt2']
        z = user_registration.objects.filter(id=usernameacnt2)
        var=acntexpensest.objects.filter(id=id)
        return render(request,'accounts_expenses_viewEdit.html',{'z':z, 'var':var})
    else:
        return redirect('/')

def accounts_expenses_viewEdit_Update(request,id):
    if 'usernameacnt2' in request.session:
        if request.session.has_key('usernameacnt2'):
            usernameacnt2 = request.session['usernameacnt2']
        z = user_registration.objects.filter(id=usernameacnt2)
        if request.method == 'POST':
            emps = acntexpensest.objects.get(id=id)
            emps.payee = request.POST['payee']
            emps.payacnt = request.POST['payacnt']
            emps.paymethod = request.POST['paymod']
            emps.paydate = request.POST['paydt']
            emps.category = request.POST['category']
            emps.description = request.POST['description']
            emps.refno = request.POST['ref']
            emps.amount = request.POST['amount']
            emps.tax = request.POST['tax']
            emps.total = request.POST['total']                
            emps.save() 
            return redirect('/accounts_expenses')
        return render(request,'accounts_expenses_viewEdit.html',{'z':z})
    else:
        return redirect('/')

def accounts_expense_newTransaction(request):
    if 'usernameacnt2' in request.session:
        if request.session.has_key('usernameacnt2'):
            usernameacnt2 = request.session['usernameacnt2']
        z = user_registration.objects.filter(id=usernameacnt2)
        mem=acntexpensest()
        if request.method == 'POST':
            mem.payee = request.POST['payee']
            mem.payacnt = request.POST['payacnt']
            mem.paymethod = request.POST['paymod']
            mem.paydate = request.POST['paydt']
            mem.category = request.POST['category']
            mem.description = request.POST['description']
            mem.refno = request.POST['ref']
            mem.amount = request.POST['amount']
            mem.tax = request.POST['tax']
            mem.total = request.POST['total']                
            mem.save()
            return redirect('/accounts_expenses')
        else:
            return render(request,'accounts_expense_newTransaction.html',{'z':z})
    else:
        return redirect('/')

def account_report(request):
    if 'usernameacnt2' in request.session:
        if request.session.has_key('usernameacnt2'):
            usernameacnt2 = request.session['usernameacnt2']
        z = user_registration.objects.filter(id=usernameacnt2)
        return render(request,'account_report.html',{'z':z})
    else:
        return redirect('/')
        
def account_reportt_issue(request):
    if 'usernameacnt2' in request.session:
        if request.session.has_key('usernameacnt2'):
            usernameacnt2 = request.session['usernameacnt2']
        z = user_registration.objects.filter(id=usernameacnt2)
        vars = reported_issue()
        if request.method == 'POST':
            vars.issue=request.POST['issue']
            vars.reporter_id=usernameacnt2
            vars.reported_date=datetime.now()
            vars.issuestatus=0
            vars.save()
            return redirect('account_report')
        return render(request,'account_report_issue.html',{'z':z})
    else:
        return redirect('/')
    
def account_reported_issue(request):
    if 'usernameacnt2' in request.session:
        if request.session.has_key('usernameacnt2'):
            usernameacnt2 = request.session['usernameacnt2']
        z = user_registration.objects.filter(id=usernameacnt2)
        n = reported_issue.objects.filter(reporter_id=usernameacnt2).order_by('-id')
        return render(request,'account_reported_issue.html',{'z':z,'n':n})
    else:
        return redirect('/')

def account_payment_details(request,id):
    if 'usernameacnt2' in request.session:
        if request.session.has_key('usernameacnt2'):
            usernameacnt2 = request.session['usernameacnt2']
        z = user_registration.objects.filter(id=usernameacnt2)
        vars=user_registration.objects.get(id=id)
        context = {'vars':vars,'z' : z,}
        return render(request,'account_payment_details.html', context)
    else:
        return redirect('/')

# @csrf_exempt
# def accounts_salary_leave(request):
#         fdate = request.GET.get('fdate')
#         tdate = request.GET.get('tdate')
#         his_id = request.GET.get('his_id')
#         global k1
#         global d14
#         global d5
#         global d4
#         try:
#             date_exe = acnt_monthdays.objects.get(month_fromdate__gte=fdate,month_todate__lte=tdate)
            
#             if date_exe:
#                 work_day = date_exe.month_workingdays
#                 start = datetime.strptime(fdate, '%Y-%m-%d')
#                 end = datetime.strptime(tdate, '%Y-%m-%d').date()
#                 event = Event.objects.filter(start_time__gte=start,start_time__lte=end).values('start_time')
#                 day_delta = timedelta(days=1)
#                 pro = project_taskassign.objects.filter(developer_id= his_id,startdate__range=(start,end),enddate__range =(start,end),submitted_date__range=(start,end))
#                 pro_delay = project_taskassign.objects.filter(id__in = pro,submitted_date__isnull = True).values('delay','enddate')
#                 # pro_delay_list = list(pro_delay)
#                 # print(pro_delay_list)
#                 pro_delay_value = project_taskassign.objects.filter(id__in = pro,submitted_date__isnull = False).values('delay','enddate','submitted_date')
#                 leave_emp = leave.objects.filter(user_id = his_id,from_date__gte = start,to_date__lte = end).values('from_date','to_date')
#                 k1=0
#                 for k in leave_emp:
#                     k2 = (k['to_date']-k['from_date']).days
#                     if k2 == 0:
#                         k2 = 1
#                     k1 = k1 + k2
                
#                 d14 =0
#                 for i in pro_delay_value:
#                     d10 = (i['enddate'])
#                     d11 = (i['submitted_date'])
#                     if d11 >= end:
#                         d11 = end
#                     d13 = (d11-d10).days
#                     if d13 == 1:
#                         d13=1
#                     delta1 = d11-d10
#                     z1 = 0

#                     cnt =  Event.objects.filter(start_time__gte=d10,start_time__lte=d11).values('start_time').count()
#                     # for g in range((delta1).days):
#                     #     n = (d10 + g*day_delta)
#                     #     if n in event:
#                     #         z1=z1+1
#                     d14 = d13 - cnt
#                     print(cnt,d14,d13)
#                 d5 = 0
#                 d4=0
#                 for j in pro_delay:
#                     d2 = (j['enddate'])
#                     if d2 >= end:
#                         d5 = 0
#                     else:
#                         d4=0
#                         z = 0
#                         d3 = (end - d2).days
#                         delta = end - d2
#                         cnt =  Event.objects.filter(start_time__gte=d2,start_time__lte=end).values('start_time').count()
#                         # for i in range((delta).days):
#                         #     n = (d2 + i*day_delta)
#                         #     if n in event:
#                         #         z=z+1
#                         d4 = d3 - cnt
#                         print(cnt,d4,d3)
#                 delay_total = d14+d5+d4
#                 total_delay =delay_total+k1
#                 conf = user_registration.objects.get(id=his_id)
#                 conf_salary = conf.confirm_salary
#                 if conf_salary == "":
#                     conf_salary = 0
#                 one_day_sal = int(conf_salary) / int(work_day)
#                 total_delay_amt = float(one_day_sal) * float(total_delay)
#                 net_salary = float(conf_salary) - float(total_delay_amt)
#                 if net_salary <= 0:
#                     net_salary = 0
#                 return HttpResponse(json.dumps({'net_salary':net_salary, 'delay_total':delay_total,'k1':k1,'work_day':work_day,'conf_salary':conf_salary}))
#             else:
#                 msg = "please add month days"
#                 return HttpResponse(json.dumps({'msg':msg}))
#         except acnt_monthdays.DoesNotExist:
#             msg = "please add month days"
#             return HttpResponse(json.dumps({'msg':msg}))


def account_payment_salary(request,id):
    if 'usernameacnt2' in request.session:
        if request.session.has_key('usernameacnt2'):
            usernameacnt2 = request.session['usernameacnt2']
        z = user_registration.objects.filter(id=usernameacnt2)
        
        vars=user_registration.objects.get(id=id)
        if request.method == "POST":
            abc = acntspayslip()
            abc.basic_salary = request.POST["salary"]
            abc.hra = request.POST["hra"]
            abc.conveyns = request.POST["ca"]
            abc.pf_tax = request.POST["pt"]
            abc.incentives = request.POST["ins"]
            abc.delay = request.POST["leaves"]
            abc.net_salary = request.POST["net_salary"]
            abc.leavesno= request.POST["commonleaves"]
            abc.fromdate= request.POST["efdate"]
            abc.tax = 0
            abc.da = request.POST['DA']
            abc.pf = request.POST["pf"]
            abc.incometax = 0
            abc.other_allovance = request.POST["other_allowance"]
            abc.other_allovancetype = request.POST["other_allowance_type"]
            abc.basictype = request.POST["basictype"]
            abc.pftype = request.POST["pftype"]
            abc.esitype = request.POST["esitype"]
            abc.hratype = request.POST["hratype"]
            abc.contype = request.POST["contype"]
            abc.protype = request.POST["protype"]
            abc.instype = request.POST["instype"]
            abc.deltype = request.POST["deltype"]
            abc.leatype = request.POST["leatype"]
            abc.esi = request.POST["esi"] 
            abc.user_id_id = vars.id
            abc.department_id = vars.department.id
            abc.designation_id = vars.designation.id
            
            abc.account_no = vars.account_no
            abc.bank_branch = vars.bank_branch
            abc.bank_name = vars.bank_name
            abc.ifsc = vars.ifsc
            
            
            
            
            abc.save()
            msg = "Salary payslip generated"
            return render(request, 'account_payment_salary.html',{'msg':msg, 'vars':vars,'z' : z})
        return render(request, 'account_payment_salary.html',{'vars':vars,'z' : z})
    else:
        return redirect('/')

def account_payment_view(request,id):
    if 'usernameacnt2' in request.session:
        if request.session.has_key('usernameacnt2'):
            usernameacnt2 = request.session['usernameacnt2']
        z = user_registration.objects.filter(id=usernameacnt2)
        reg =user_registration.objects.get(id=id)
        use=acntspayslip.objects.filter(user_id_id=id)
        return render(request,'account_payment_view.html',{'reg':reg,'use':use,'z' : z,})
    else:
        return redirect('/')

def accounts_bank_acnt_details(request,id):
    if 'usernameacnt2' in request.session:
        if request.session.has_key('usernameacnt2'):
            usernameacnt2 = request.session['usernameacnt2']
        z = user_registration.objects.filter(id=usernameacnt2)
        mem1=user_registration.objects.filter(id=id)
        return render(request,'accounts_bank_acnt_details.html',{ 'mem1':mem1,'z': z})
    else:
        return redirect('/')

def accounts_add_bank_acnt(request,id):
    if 'usernameacnt2' in request.session:
        if request.session.has_key('usernameacnt2'):
            usernameacnt2 = request.session['usernameacnt2']
        z = user_registration.objects.filter(id=usernameacnt2)
        mem1=user_registration.objects.filter(id=id)
        if request.method == 'POST':
            vars = user_registration.objects.get(id=id)
            vars.account_no = request.POST['account_no']
            vars.ifsc = request.POST['ifsc']
            vars.bank_branch = request.POST['bank_branch']
            vars.bank_name= request.POST['bank_name']
            vars.save()
        return render(request,'accounts_add_bank_acnt.html',{'mem1':mem1,'z': z})
    else:
        return redirect('/')

def accounts_salary_details(request,id):
    if 'usernameacnt2' in request.session:
        if request.session.has_key('usernameacnt2'):
            usernameacnt2 = request.session['usernameacnt2']
        z = user_registration.objects.filter(id=usernameacnt2)
        mem1=user_registration.objects.get(id=id)
        usk=acntspayslip.objects.filter(user_id=id)
        return render(request,'accounts_salary_details.html',{ 'mem1':mem1,'usk':usk,'z': z})
    else:
        return redirect('/')

def logout5(request):
    if 'usernameacnt2' in request.session:  
        request.session.flush()
        return redirect('/')
    else:
        return redirect('/') 

@csrf_exempt
def accounts_acntpay(request):
    if 'usernameacnt2' in request.session:
        fdate = request.POST['fdate']
        tdate = request.POST['tdate']
        dept_id = int(request.POST['depmt'])
        desig_id = int(request.POST['desi'])  
        names = acntspayslip.objects.filter(fromdate__range=(fdate,tdate),designation_id= desig_id, department_id= dept_id).values('user_id__fullname','eno', 'user_id__account_no', 'user_id__bank_name', 'user_id__bank_branch','user_id__id', 'user_id__email','id')  
        
        return render(request,'accounts_acntpay.html', {'names':names})
    else:
        return redirect('/')

def accounts_payslip(request):
    if 'usernameacnt2' in request.session:
        if request.session.has_key('usernameacnt2'):
            usernameacnt2 = request.session['usernameacnt2']
        z = user_registration.objects.filter(id=usernameacnt2)   
        dept = department.objects.all()
        des = designation.objects.all()
        return render(request,'accounts_payslip.html', {'dept':dept, 'des':des,'z':z})      
    else:
        return redirect('/')

def accounts_paydetails(request,id,tid):
    if 'usernameacnt2' in request.session:
        if request.session.has_key('usernameacnt2'):
            usernameacnt2 = request.session['usernameacnt2']
        z = user_registration.objects.filter(id=usernameacnt2)   
        user = user_registration.objects.get(id=tid)
        acc = acntspayslip.objects.get(id=id)
        names = acntspayslip.objects.all()
        return render(request,'accounts_paydetails.html', {'acc':acc, 'user':user,'z':z})
    else:
        return redirect('/')
        
def accounts_print(request,id,tid):
    if 'usernameacnt2' in request.session:
        if request.session.has_key('usernameacnt2'):
            usernameacnt2 = request.session['usernameacnt2']
        z = user_registration.objects.filter(id=usernameacnt2)   
        user = user_registration.objects.get(id=tid)
        acc = acntspayslip.objects.get(id=id)
        return render(request,'accounts_print.html', {'acc':acc, 'user':user,'z':z})
    else:
        return redirect('/')

def acntpaypdf(request, id, tid):
    date = datetime.now()
    user = user_registration.objects.get(id=tid)
    acc = acntspayslip.objects.get(id=id)
    print(acc)
    year = date.today().year
    month = date.today().month

    leave = acnt_monthdays.objects.get(month_fromdate__year__gte=year,
                                       month_fromdate__month__gte=month,
                                       month_todate__year__lte=year,
                                       month_todate__month__lte=month)
    mm = leave.month_workingdays
    m = leave.month_holidays
    print(mm)
    abc = int(user.confirm_salary)
    print(abc)
    c = abc/mm
    v = acc.leavesno
    z = v-m
    mem = mm-z
    if mem == '-':
        mem = 0
        conf = abc-c
        words = num2words(conf)
        template_path = 'acntpaypdf.html'
        context = {'acc': acc, 'user': user, 'c': c, 'mm': mm, 'mem': mem, 'conf': conf, 'words': words,
                   'media_url': settings.MEDIA_URL,
                   'date': date,
                   }
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'filename="Payslip.pdf"'
        template = get_template(template_path)
        html = template.render(context)
        pisa_status = pisa.CreatePDF(
            html, dest=response)
        if pisa_status.err:
            return HttpResponse('We had some errors <pre>' + html + '</pre>')
        return response
    else:

        conf = abc-c
        words = num2words(conf)
        template_path = 'acntpaypdf.html'
        context = {'acc': acc, 'user': user, 'c': c, 'mm': mm, 'mem': mem, 'conf': conf, 'words': words,
                   'media_url': settings.MEDIA_URL,
                   'date': date,
                   }
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'filename="Payslip.pdf"'
        template = get_template(template_path)
        html = template.render(context)
        pisa_status = pisa.CreatePDF(
            html, dest=response)
        if pisa_status.err:
            return HttpResponse('We had some errors <pre>' + html + '</pre>')
        return response      
        
        
    # ************************Reset password*****************************
def reset_password(request):
    if request.method == "POST":
        email_id = request.POST.get('email')
        access_user_data = user_registration.objects.filter(email=email_id).exists()
        if access_user_data:
            _user = user_registration.objects.get(email=email_id)
            password = random.SystemRandom().randint(100000, 999999)

            _user.password = password
            subject = 'iNFOX Technologies your authentication data updated'
            message = 'Password Reset Successfully\n\nYour login details are below\n\nUsername : ' + str(email_id) + '\n\nPassword : ' + str(password) + \
                '\n\nYou can login this details\n\nNote: This is a system generated email, do not reply to this email id'
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [email_id, ]
            send_mail(subject, message, email_from,
                      recipient_list, fail_silently=True)

            _user.save()
            msg_success = "Password Reset successfully check your mail new password"
            return render(request, 'Reset_password.html', {'msg_success': msg_success})
        else:
            msg_error = "This email does not exist iNFOX Technologies "
            return render(request, 'Reset_password.html', {'msg_error': msg_error})

    return render(request,'Reset_password.html')
    
    
    
# **************************christin account settings and change password**************************
def tlaccountset(request):
    if request.session.has_key('tlid'):
        tlid = request.session['tlid']
    else:
        return redirect('/')
    mem = user_registration.objects.filter(id=tlid)
    return render(request, 'tlaccountset.html', {'mem': mem})

def devaccountset(request):
    if request.session.has_key('devid'):
        devid = request.session['devid']
    else:
        return redirect('/')
    dev = user_registration.objects.filter(id=devid)
    return render(request, 'devaccountset.html', {'dev': dev})

def testaccountset(request):
    if request.session.has_key('usernametsid'):
        usernametsid = request.session['usernametsid']
    else:
        return redirect('/')
    mem = user_registration.objects.filter(id=usernametsid)
    mems = user_registration.objects.filter(id=usernametsid)
    return render(request, 'testaccountset.html', {'mem': mem, 'mems': mems})

def pmaccountset(request):
    if request.session.has_key('prid'):
        prid = request.session['prid']
    else:
        return redirect('/')
    pro = user_registration.objects.filter(id=prid)
    return render(request, 'pmaccountset.html', {'pro': pro})


def imagechange_tl(request, id):
    if request.session.has_key('tlid'):
        tlid = request.session['tlid']
    else:
        return redirect('/')
    mem = user_registration.objects.filter(id=tlid)
    if request.method == 'POST':
        abc = user_registration.objects.get(id=id)
        abc.photo = request.FILES['filename']
        
        abc.save()
        return redirect('tlaccountset')
    return render(request, 'tlaccountset.html',{'mem': mem})

def imagechange_dev(request, id):
    if request.session.has_key('devid'):
        devid = request.session['devid']
    else:
        return redirect('/')
    dev = user_registration.objects.filter(id=devid)
    if request.method == 'POST':
        abc = user_registration.objects.get(id=id)
        abc.photo = request.FILES['filename']
        
        abc.save()
        return redirect('devaccountset')
    return render(request, 'devaccountset.html',{'dev': dev})

def imagechange_test(request, id):
    if request.session.has_key('usernametsid'):
        usernametsid = request.session['usernametsid']
    else:
        return redirect('/')
    mem = user_registration.objects.filter(id=usernametsid)
    if request.method == 'POST':
        abc = user_registration.objects.get(id=id)
        abc.photo = request.FILES['filename']
        
        abc.save()
        return redirect('testaccountset')
    return render(request, 'testaccountset.html',{'mem': mem})

def imagechange_pm(request, id):
    if request.session.has_key('prid'):
        prid = request.session['prid']
    else:
        return redirect('/')
    pro = user_registration.objects.filter(id=prid)
    if request.method == 'POST':
        abc = user_registration.objects.get(id=id)
        abc.photo = request.FILES['filename']
        
        abc.save()
        return redirect('pmaccountset')
    return render(request, 'pmaccountset.html',{'pro': pro})


def tlchangepass(request):
    if request.session.has_key('tlid'):
        tlid = request.session['tlid']
    else:
        return redirect('/')
    mem = user_registration.objects.filter(id=tlid)

    if request.method == 'POST':
        abc = user_registration.objects.get(id=tlid)
        cur = abc.password
        oldps = request.POST["currentPassword"]
        newps = request.POST["newPassword"]
        cmps = request.POST["confirmPassword"]
        if oldps == cur:
            if oldps != newps:
                if newps == cmps:
                    abc.password = request.POST.get('confirmPassword')
                    abc.save()
                    return render(request, 'TLdashboard.html', {'mem': mem})
            elif oldps == newps:
                messages.add_message(request, messages.INFO, 'Current and New password same')
            else:
                messages.info(request, 'Incorrect password same')

            return render(request, 'tlchangepass.html', {'mem': mem})
        else:
            messages.add_message(request, messages.INFO, 'old password wrong')
            return render(request, 'tlchangepass.html', {'mem': mem})
    return render(request, 'tlchangepass.html', {'mem': mem})

def devchangepass(request):
    if request.session.has_key('devid'):
        devid = request.session['devid']
    else:
        return redirect('/')
    dev = user_registration.objects.filter(id=devid)

    if request.method == 'POST':
        abc = user_registration.objects.get(id=devid)
        cur = abc.password
        oldps = request.POST["currentPassword"]
        newps = request.POST["newPassword"]
        cmps = request.POST["confirmPassword"]
        if oldps == cur:
            if oldps != newps:
                if newps == cmps:
                    abc.password = request.POST.get('confirmPassword')
                    abc.save()
                    return render(request, 'devdashboard.html', {'dev': dev})
            elif oldps == newps:
                messages.add_message(request, messages.INFO, 'Current and New password same')
            else:
                messages.info(request, 'Incorrect password same')

            return render(request, 'devchangepass.html', {'dev': dev})
        else:
            messages.add_message(request, messages.INFO, 'old password wrong')
            return render(request, 'devchangepass.html', {'dev': dev})
    return render(request, 'devchangepass.html', {'dev': dev})

def testchangepass(request):
    if request.session.has_key('usernametsid'):
        usernametsid = request.session['usernametsid']
    else:
        return redirect('/')
    mem = user_registration.objects.filter(id=usernametsid)

    if request.method == 'POST':
        abc = user_registration.objects.get(id=usernametsid)
        cur = abc.password
        oldps = request.POST["currentPassword"]
        newps = request.POST["newPassword"]
        cmps = request.POST["confirmPassword"]
        if oldps == cur:
            if oldps != newps:
                if newps == cmps:
                    abc.password = request.POST.get('confirmPassword')
                    abc.save()
                    return render(request, 'TLdashboard.html', {'mem': mem})
            elif oldps == newps:
                messages.add_message(request, messages.INFO, 'Current and New password same')
            else:
                messages.info(request, 'Incorrect password same')

            return render(request, 'testchangepass.html', {'mem': mem})
        else:
            messages.add_message(request, messages.INFO, 'old password wrong')
            return render(request, 'testchangepass.html', {'mem': mem})
    return render(request, 'testchangepass.html', {'mem': mem})

def prchangepass(request):
    if request.session.has_key('prid'):
        prid = request.session['prid']
    else:
        return redirect('/')
    pro = user_registration.objects.filter(id=prid)

    if request.method == 'POST':
        abc = user_registration.objects.get(id=prid)
        cur = abc.password
        oldps = request.POST["currentPassword"]
        newps = request.POST["newPassword"]
        cmps = request.POST["confirmPassword"]
        if oldps == cur:
            if newps == cmps:
                abc.password = request.POST.get('confirmPassword')
                abc.save()
                return render(request, 'pmanager_dash.html', {'pro': pro})
            elif oldps == newps:
                messages.info(request,  'Current and New password same')
            else:
                messages.info(request, 'Incorrect password same')
                return render(request, 'TSdashboard.html', {'pro': pro})
        else:
            messages.add_message(request, messages.INFO, 'old password wrong')
            return render(request, 'prchangepass.html', {'pro': pro})
    return render(request, 'prchangepass.html', {'pro': pro})
    
    
    
    
    
    
#super admin views #
def superadmin_changepwd(request):
    if 'SAdm_id' in request.session:
        if request.session.has_key('SAdm_id'):
            SAdm_id = request.session['SAdm_id']
        users = User.objects.filter(id=SAdm_id)
        if request.method == 'POST':

            newPassword = request.POST.get('newPassword')
            confirmPassword = request.POST.get('confirmPassword')

            user = User.objects.get(is_superuser=True)
            if newPassword == confirmPassword:
                user.set_password(newPassword)
                user.save()
                msg_success = "Password has been changed successfully"
                return render(request, 'superadmin_changepwd.html', {'msg_success': msg_success})
            else:
                msg_error = "Password does not match"
                return render(request, 'superadmin_changepwd.html', {'msg_error': msg_error})
        return render(request,'superadmin_changepwd.html',{'users':users})
    else:
        return redirect('/')
    
    

def superadmin_index(request):
    if 'SAdm_id' in request.session:
        if request.session.has_key('SAdm_id'):
                SAdm_id = request.session['SAdm_id']
        users = User.objects.filter(id=SAdm_id)
        return render(request,'SuperAdmin_index.html',{'users':users})
    else:
        return redirect('/')

def superadmin_logout(request):
    request.session.flush()
    return redirect("/")



# **************************Anandhu Super-Admin Dashboard section**************************

def SuperAdmin_index(request):
    # if 'Adm_id' in request.session:
    #     if request.session.has_key('Adm_id'):
    #         Adm_id = request.session['Adm_id']
    #     else:
    #         return redirect('/')
    #     mem = user_registration.objects.filter(id=Adm_id)
    #     return render(request,'SuperAdmin_index.html',{'mem':mem})
    # else:
    #     return redirect('/')
    return render(request, 'SuperAdmin_index.html')


def SuperAdmin_dashboard(request):
    if 'SAdm_id' in request.session:
        if request.session.has_key('SAdm_id'):
                SAdm_id = request.session['SAdm_id']
        users = User.objects.filter(id=SAdm_id)
        branch = branch_registration.objects.all()
        
        return render(request, 'SuperAdmin_dashboard.html',{'branch_registration':branch,'users':users}) 
    else:
        return redirect('/')


def SuperAdmin_profile(request,id):
    if 'SAdm_id' in request.session:
        if request.session.has_key('SAdm_id'):
                SAdm_id = request.session['SAdm_id']
        users = User.objects.filter(id=SAdm_id)
        branch = branch_registration.objects.get(id = id)
        Num1 = project.objects.filter(branch_id=id).count()
        Num = user_registration.objects.filter(branch_id=id).count()
        Trainer = designation.objects.get(designation='trainer')
        trcount=user_registration.objects.filter(designation=Trainer,branch_id=id).count()
        return render(request, 'SuperAdmin_profile.html',{'users':users,'br':branch,'Num1':Num1,'Num':Num,'trcount':trcount}) 
    else:
        return redirect('/')


def SuperAdmin_trainersdepartment(request,id):
    if 'SAdm_id' in request.session:
        if request.session.has_key('SAdm_id'):
                SAdm_id = request.session['SAdm_id']
        users = User.objects.filter(id=SAdm_id)
        Dept = department.objects.filter(branch = id)
        return render(request,'SuperAdmin_trainersdepartment.html',{'users':users,'Dept':Dept})
    else:
        return redirect('/')


def SuperAdmin_trainerstable(request,id):
    if 'SAdm_id' in request.session:
        if request.session.has_key('SAdm_id'):
                SAdm_id = request.session['SAdm_id']
        users = User.objects.filter(id=SAdm_id)

        Trainer = designation.objects.get(designation='Trainer')
            
        trainers_data=user_registration.objects.filter(designation=Trainer).filter(department=id)
        topics=topic.objects.all()
        return render(request,'SuperAdmin_trainerstable.html',{'users':users,'trainers_data':trainers_data,'topics':topics})
    else:
        return redirect('/')

def SuperAdmin_trainerteams(request,id):
    if 'SAdm_id' in request.session:
        if request.session.has_key('SAdm_id'):
                SAdm_id = request.session['SAdm_id']
        users = User.objects.filter(id=SAdm_id)
        user=user_registration.objects.filter(id=id)
        team=create_team.objects.all()
        return render(request,'SuperAdmin_trainerteams.html',{'users':users,'team':team,'user':user})
    else:
        return redirect('/')

def  SuperAdmin_trainerteam(request,id):
    if 'SAdm_id' in request.session:
        if request.session.has_key('SAdm_id'):
                SAdm_id = request.session['SAdm_id']
        users = User.objects.filter(id=SAdm_id)
        id=id
        Trainee = designation.objects.get(designation='Trainee')
        num=user_registration.objects.filter(designation=Trainee).filter(team=id).count()
        num1=topic.objects.filter(team=id).count()
        return render(request,'SuperAdmin_trainerteam.html',{'users':users,'id':id,'num':num,'num1':num1})
    else:
        return redirect('/')

def SuperAdmin_topictable(request,id):
    if 'SAdm_id' in request.session:
        if request.session.has_key('SAdm_id'):
                SAdm_id = request.session['SAdm_id']
        users = User.objects.filter(id=SAdm_id)
        topics=topic.objects.filter(team=id).order_by("-id")
        return render(request,'SuperAdmin_topictable.html',{'users':users,'topics':topics})
    else:
        return redirect('/')
        
def SuperAdmin_traineestable(request,id):
    if 'SAdm_id' in request.session:
        if request.session.has_key('SAdm_id'):
                SAdm_id = request.session['SAdm_id']
        users = User.objects.filter(id=SAdm_id)
        Trainee = designation.objects.get(designation='Trainee')
        trainees_data=user_registration.objects.filter(designation=Trainee).filter(team=id)
        return render(request,'SuperAdmin_traineestable.html',{'users':users,'trainees_data':trainees_data}) 
    else:
        return redirect('/')

        
def SuperAdmin_traineeprofile(request,id):
    if 'SAdm_id' in request.session:
        if request.session.has_key('SAdm_id'):
                SAdm_id = request.session['SAdm_id']
        users = User.objects.filter(id=SAdm_id)
        trainees_data=user_registration.objects.get(id=id)
        user=user_registration.objects.get(id=id)
        num=trainer_task.objects.filter(user=user).filter(task_status='1').count()
        return render(request,'SuperAdmin_traineeprofile.html',{'users':users,'trainees_data':trainees_data,'num':num})
    else:
        return redirect('/')

def SuperAdmin_completedtasktable(request,id):
    if 'SAdm_id' in request.session:
        if request.session.has_key('SAdm_id'):
                SAdm_id = request.session['SAdm_id']
        users = User.objects.filter(id=SAdm_id)
        user=user_registration.objects.get(id=id)
        task=trainer_task.objects.filter(user=user)
        return render(request,'SuperAdmin_completedtasktable.html',{'users':users,'task_data':task})   
    else:
        return redirect('/')
   

# **************************subeesh akhil sharon  Super-Admin Dashboard-project section**************************


# current projects- sharon
def SuperAdmin_pythons(request):
    if 'SAdm_id' in request.session:
        if request.session.has_key('SAdm_id'):
                SAdm_id = request.session['SAdm_id']
        users = User.objects.filter(id=SAdm_id)
        project_details = project.objects.all()
        return render(request,'SuperAdmin_projects.html',{'users':users,'proj_det':project_details})
    else:
        return redirect('/')
    # if 'Adm_id' in request.session:
    #     if request.session.has_key('Adm_id'):
    #         Adm_id = request.session['Adm_id']
    #     else:
    #         return redirect('/')
    #     Adm = user_registration.objects.filter(id=Adm_id)
        
    # else:
    #     return redirect('/')

def SuperAdmin_dept(request,id):
    if 'SAdm_id' in request.session:
        if request.session.has_key('SAdm_id'):
                SAdm_id = request.session['SAdm_id']
        users = User.objects.filter(id=SAdm_id)    
        project_details = project.objects.all()
        depart =department.objects.filter(branch=id)
        
        return render(request,'SuperAdmin_dept.html',{'users':users,'proj_det':project_details,'department':depart})
    else:
        return redirect('/')
    # if 'Adm_id' in request.session:
    #     if request.session.has_key('Adm_id'):
    #         Adm_id = request.session['Adm_id']
    #     else:
    #         return redirect('/')
    #     Adm = user_registration.objects.filter(id=Adm_id)
    
    # else:
    #     return redirect('/')

    
# def SuperAdmin_profiledash(request):
#     Num= project.objects.count()
#     project_details = project.objects.all()
#     return render(request,'SuperAdmin_profiledash.html',{'proj_det':project_details,'num':Num})

def SuperAdmin_projects(request,id):
    if 'SAdm_id' in request.session:
        if request.session.has_key('SAdm_id'):
                SAdm_id = request.session['SAdm_id']
        users = User.objects.filter(id=SAdm_id)
        Num= project.objects.filter(status='accepted').filter(department=id).count()
        num= project.objects.filter(status='completed').filter(department=id).count()
        project_details = project.objects.all()
        depart =department.objects.get(id=id)
        id=id
        return render(request,'SuperAdmin_projects.html',{'users':users,'proj_det':project_details,'num':Num,'Num':num,'department':depart,'id':id})
    else:
        return redirect('/')
    # if 'Adm_id' in request.session:
    #     if request.session.has_key('Adm_id'):
    #         Adm_id = request.session['Adm_id']
    #     else:
    #         return redirect('/')
    #     Adm = user_registration.objects.filter(id=Adm_id)
    
    # else:
    #     return redirect('/')
 
def SuperAdmin_proj_list(request,id):
    if 'SAdm_id' in request.session:
        if request.session.has_key('SAdm_id'):
                SAdm_id = request.session['SAdm_id']
        users = User.objects.filter(id=SAdm_id)
        project_details = project.objects.filter(department=id)
        print (project_details.count())
        return render(request,'SuperAdmin_proj_list.html',{'users':users,'proj_det':project_details})
    else:
        return redirect('/')

def SuperAdmin_proj_det(request,id):
    if 'SAdm_id' in request.session:
        if request.session.has_key('SAdm_id'):
                SAdm_id = request.session['SAdm_id']
        users = User.objects.filter(id=SAdm_id)
        project_details = project.objects.get(id=id)
        return render(request,'SuperAdmin_proj_det.html',{'users':users,'proj_det':project_details})
    else:
        return redirect('/')

def SuperAdmin_proj_mngrs(request,id):
    if 'SAdm_id' in request.session:
        if request.session.has_key('SAdm_id'):
                SAdm_id = request.session['SAdm_id']
        users = User.objects.filter(id=SAdm_id)
        project_details = project.objects.get(id=id)
        return render(request,'SuperAdmin_proj_mngrs.html',{'users':users,'proj_det':project_details})
    else:
        return redirect('/')

# def SuperAdmin_proj_mangrs1(request,id):
#     if request.session.has_key('Adm_id'):
#         Adm_id = request.session['Adm_id']
 
#     mem = user_registration.objects.filter(id=Adm_id)
#     project_details = project.objects.get(id=id) 
#     return render(request,'SuperAdmin_proj_mangrs1.html',{'proj_det':project_details,'mem':mem})
def SuperAdmin_proj_mangrs1(request,id):
    if 'SAdm_id' in request.session:
        if request.session.has_key('SAdm_id'):
                SAdm_id = request.session['SAdm_id']
        users = User.objects.filter(id=SAdm_id)
        project_details = project.objects.get(id=id) 
        proj1=project_details.projectmanager_id
        dept_id=project_details.department_id
        user_det=user_registration.objects.filter(designation_id=proj1)
        return render(request,'SuperAdmin_proj_mangrs1.html',{'users':users,'proj1':proj1,'user_det':user_det,'proj_det':project_details})
    else:
        return redirect('/')

def SuperAdmin_proj_mangrs2(request,id):
    if 'SAdm_id' in request.session:
        if request.session.has_key('SAdm_id'):
                SAdm_id = request.session['SAdm_id']
        users = User.objects.filter(id=SAdm_id)
        project_details = project.objects.get(id=id) 
        proj1=project_details.projectmanager_id
        dept_id=project_details.department_id
        user_det=user_registration.objects.filter(designation_id=proj1)
        
        return render(request,'SuperAdmin_proj_mangrs2.html',{'users':users,'proj1':proj1,'user_det':user_det,'proj_det':project_details})
    else:
        return redirect('/')

def SuperAdmin_daily_report(request,id):
    if 'SAdm_id' in request.session:
        if request.session.has_key('SAdm_id'):
                SAdm_id = request.session['SAdm_id']
        users = User.objects.filter(id=SAdm_id)


        proj_name =  project_taskassign.objects.all()
        tester_name = user_registration.objects.all()
        tester = tester_status.objects.filter(user_id=id)
        return render(request,'SuperAdmin_daily_report.html',{'users':users,'test':tester, 'tester_name':tester_name, 'proj_name':proj_name})
    else:
        return redirect('/')
        
def SuperAdmin_developers(request,id):
    if 'SAdm_id' in request.session:
        if request.session.has_key('SAdm_id'):
                SAdm_id = request.session['SAdm_id']
        users = User.objects.filter(id=SAdm_id)

        proj2=request.session['proj2']
        
    
        project_details = project.objects.get(id=proj2) 
        project_task = project_taskassign.objects.filter(project_id = project_details).filter(tl_id=id)
        user_det=user_registration.objects.filter(tl_id=id).order_by("-id")
        progress_bar= tester_status.objects.all()
        
        return render(request,'SuperAdmin_developers.html',{'users':users,'proj_task':project_task,'proj_det':project_details,'prog_status':progress_bar,'user_det':user_det})
    else:
        return redirect('/')


# completed projects- subeesh
 
def SuperAdmin_proj_cmpltd_new(request, id):
    if 'SAdm_id' in request.session:
        if request.session.has_key('SAdm_id'):
                SAdm_id = request.session['SAdm_id']
        users = User.objects.filter(id=SAdm_id)
        project_details=project.objects.filter(department=id)
        print (project_details.count())
        return render(request,'SuperAdmin_proj_cmpltd_show.html',{'users':users,'project': project_details})
    else:
        return redirect('/')


def SuperAdmin_cmpltd_proj_det_new(request, id):
    if 'SAdm_id' in request.session:
        if request.session.has_key('SAdm_id'):
                SAdm_id = request.session['SAdm_id']
        users = User.objects.filter(id=SAdm_id)
        project_details = project.objects.get(id=id)
        return render(request,'SuperAdmin_cmpltd_proj_det_show.html',{'users':users,'project': project_details})
    else:
        return redirect('/')
        
def SuperAdmin_proj_mngrs_new(request, id):
    if 'SAdm_id' in request.session:
        if request.session.has_key('SAdm_id'):
                SAdm_id = request.session['SAdm_id']
        users = User.objects.filter(id=SAdm_id)
        project_details = project.objects.get(id=id)
        return render(request,'SuperAdmin_proj_mngrs_show.html', {'users':users,'project': project_details})
    else:
        return redirect('/')

# def SuperAdmin_proj_mangrs1_new(request,id):
#     if request.session.has_key('Adm_id'):
#         Adm_id = request.session['Adm_id']
 
#     mem = user_registration.objects.filter(id=Adm_id)
#     project_details = project.objects.get(id=id)
#     return render(request,'SuperAdmin_proj_mangrs1_show.html', {'project': project_details,'mem':mem})
def SuperAdmin_proj_mangrs1_new(request,id):
    if 'SAdm_id' in request.session:
        if request.session.has_key('SAdm_id'):
                SAdm_id = request.session['SAdm_id']
        users = User.objects.filter(id=SAdm_id)
        project_details = project.objects.get(id=id) 
        proj1=project_details.projectmanager_id
        dept_id=project_details.department_id
        user_det=user_registration.objects.filter(designation_id=proj1)
        return render(request,'SuperAdmin_proj_mangrs1_show.html',{'users':users,'proj1':proj1,'user_det':user_det,'proj_det':project_details})
    else:
        return redirect('/')
        
def SuperAdmin_proj_mangrs2_new(request, id):
    if 'SAdm_id' in request.session:
        if request.session.has_key('SAdm_id'):
                SAdm_id = request.session['SAdm_id']
        users = User.objects.filter(id=SAdm_id)
        project_details = project.objects.get(id=id)
        project_task = project_taskassign.objects.all()
        return render(request,'SuperAdmin_proj_mangrs2_show.html', {'users':users,'project':project_details,'project_taskassign':project_task})
    else:
        return redirect('/')

def SuperAdmin_developers_new(request, id):
    if 'SAdm_id' in request.session:
        if request.session.has_key('SAdm_id'):
                SAdm_id = request.session['SAdm_id']
        users = User.objects.filter(id=SAdm_id)
        project_details = project.objects.get(id=id)
        project_task = project_taskassign.objects.filter(tl_id = id)
        progress_bar= tester_status.objects.all()
        return render(request,'SuperAdmin_developers_show.html', {'users':users,'project':project_details,'project_taskassign':project_task,'prog_status':progress_bar})
    else:
        return redirect('/')

def SuperAdmin_daily_report_new(request, id):
    if 'SAdm_id' in request.session:
        if request.session.has_key('SAdm_id'):
                SAdm_id = request.session['SAdm_id']
        users = User.objects.filter(id=SAdm_id)
        project_task = project_taskassign.objects.get(user_id=id)
        tester = tester_status.objects.all()
        return render(request,'SuperAdmin_daily_report_show.html', {'users':users,'project':project_task,'tester_status':tester})
    else:
        return redirect('/')


    # **************************meenu nimisha  Super-Admin Dashboard-employee section**************************

def SuperAdmin_employees(request,id):
    if 'SAdm_id' in request.session:
        if request.session.has_key('SAdm_id'):
                SAdm_id = request.session['SAdm_id']
        users = User.objects.filter(id=SAdm_id)
        Dept = department.objects.filter(branch=id)
        return render(request,'SuperAdmin_Employees1.html',{'users':users,'Dept':Dept})
    else:
        return redirect('/')

        
def SuperAdmin_edepartments(request,id):
    if 'SAdm_id' in request.session:
        if request.session.has_key('SAdm_id'):
                SAdm_id = request.session['SAdm_id']
        users = User.objects.filter(id=SAdm_id)
        Dept = department.objects.get(id = id)
        deptid=id        
        Desig = designation.objects.all()
        return render(request,'SuperAdmin_edpartments.html',{'users':users,'Desig':Desig,'Dept':Dept,'dept_id':deptid})
    else:
        return redirect('/')

def SuperAdmin_projectman(request,id,did):
    if 'SAdm_id' in request.session:
        if request.session.has_key('SAdm_id'):
                SAdm_id = request.session['SAdm_id']
        users = User.objects.filter(id=SAdm_id)
        Project_man= designation.objects.get(id = id)
        project_name = project.objects.filter(designation=Project_man).filter(department=did)
        Project_man_data=user_registration.objects.filter(designation=Project_man).filter(department=did).order_by("-id")
        return render(request,'SuperAdmin_projectman.html',{'users':users,'pro_man_data':Project_man_data,'project_name':project_name,'Project_man':Project_man})
    else:
        return redirect('/')
    

def SuperAdmin_ViewTrainers(request,id,did):  
    if 'SAdm_id' in request.session:
        if request.session.has_key('SAdm_id'):
                SAdm_id = request.session['SAdm_id']
        users = User.objects.filter(id=SAdm_id)
        projectname=project.objects.all()
        trainer=designation.objects.get(id=id)
        userreg=user_registration.objects.filter(designation=trainer).filter(department=did).order_by("-id")
        return render(request,'SuperAdmin_ViewTrainers.html', {'users':users,'user_registration':userreg, 'project':projectname})
    else:
        return redirect('/')


def SuperAdmin_View_Trainerprofile(request,id):  
    if 'SAdm_id' in request.session:
        if request.session.has_key('SAdm_id'):
                SAdm_id = request.session['SAdm_id']
        users = User.objects.filter(id=SAdm_id)
        userreg=user_registration.objects.get(id=id)
        labels = []
        data = []
        queryset = user_registration.objects.filter(id=id)
        for i in queryset:
            labels=[i.workperformance,i.attitude,i.creativity]
            data=[i.workperformance,i.attitude,i.creativity]
        return render(request,'SuperAdmin_View_Trainerprofile.html', {'users':users,'user_registration':userreg,'labels':labels,'data':data})
    else:
        return redirect('/')


def SuperAdmin_View_Currenttraineesoftrainer(request,id):
    if 'SAdm_id' in request.session:
        if request.session.has_key('SAdm_id'):
                SAdm_id = request.session['SAdm_id']
        users = User.objects.filter(id=SAdm_id)
        user=user_registration.objects.filter(id=id)
        trainee=designation.objects.get(designation='trainee')
        user2=user_registration.objects.filter(designation=trainee)
        return render(request,'SuperAdmin_View_Currenttraineesoftrainer.html',{'users':users,'user_registration':user,'user_registration2':user2})
    else:
        return redirect('/')
   
def SuperAdmin_View_Currenttraineeprofile(request,id):
    if 'SAdm_id' in request.session:
        if request.session.has_key('SAdm_id'):
                SAdm_id = request.session['SAdm_id']
        users = User.objects.filter(id=SAdm_id)
        userreg=user_registration.objects.get(id=id)
        labels = []
        data = []
        queryset = user_registration.objects.filter(id=id)
        for i in queryset:
            labels=[i.workperformance,i.attitude,i.creativity]
            data=[i.workperformance,i.attitude,i.creativity]
        return render(request,'SuperAdmin_View_Currenttraineeprofile.html', {'users':users,'user_registration':userreg,'labels':labels,'data':data})
    else:
        return redirect('/')
   
       
def SuperAdmin_View_Currenttraineetasks(request,id):
    if 'SAdm_id' in request.session:
        if request.session.has_key('SAdm_id'):
                SAdm_id = request.session['SAdm_id']
        users = User.objects.filter(id=SAdm_id)
        # user=user_registration.objects.get(id=id)
        tasks=trainer_task.objects.filter(user=id)
        return render(request,'SuperAdmin_View_Currenttraineetasks.html',{'users':users,'trainer_task':tasks})
    else:
        return redirect('/')
    
       
def SuperAdmin_View_Currenttraineeattendance(request,id):
    if 'SAdm_id' in request.session:
        if request.session.has_key('SAdm_id'):
                SAdm_id = request.session['SAdm_id']
        users = User.objects.filter(id=SAdm_id)
        usr=user_registration.objects.get(id=id)
        return render(request,'SuperAdmin_View_Currenttraineeattendance.html', {'users':users,'user_registration':usr})
    else:
        return redirect('/')


def SuperAdmin_ViewCurrenttraineeattendancesort(request,id): 
    if 'SAdm_id' in request.session:
        if request.session.has_key('SAdm_id'):
                SAdm_id = request.session['SAdm_id']
        users = User.objects.filter(id=SAdm_id)
        usr=user_registration.objects.get(id=id)
        if request.method == "POST":
            fromdate = request.POST.get('fromdate')
            todate = request.POST.get('todate') 
            adata =attendance.objects.filter(date__range=[fromdate,todate]).filter(user_id=id)
        return render(request,'SuperAdmin_View_Currenttraineeattendancesort.html',{'users':users,'adata':adata,'user_registration':usr})
    else:
        return redirect('/')
    
        
def SuperAdmin_View_Previoustraineesoftrainer(request,id): 
    if 'SAdm_id' in request.session:
        if request.session.has_key('SAdm_id'):
                SAdm_id = request.session['SAdm_id']
        users = User.objects.filter(id=SAdm_id)
        user=user_registration.objects.filter(id=id)
        trainee=designation.objects.get(designation='trainee')
        user2=user_registration.objects.filter(designation=trainee)
        return render(request,'SuperAdmin_View_Previoustraineesoftrainer.html',{'users':users,'user_registration':user,'user_registration2':user2})
    else:
        return redirect('/')

def SuperAdmin_View_Previoustraineetasks(request,id):   
    if 'SAdm_id' in request.session:
        if request.session.has_key('SAdm_id'):
                SAdm_id = request.session['SAdm_id']
        users = User.objects.filter(id=SAdm_id)
        user=user_registration.objects.get(id=id)
        tasks=trainer_task.objects.filter(user=user)        
        return render(request,'SuperAdmin_View_Previoustraineetasks.html',{'users':users,'trainer_task':tasks})
    else:
        return redirect('/')


def SuperAdmin_View_Previoustraineeattendance(request,id):
    if 'SAdm_id' in request.session:
        if request.session.has_key('SAdm_id'):
                SAdm_id = request.session['SAdm_id']
        users = User.objects.filter(id=SAdm_id)
        usr=user_registration.objects.get(id=id)
        return render(request,'SuperAdmin_View_Previoustraineeattendance.html', {'users':users,'user_registration':usr})
    else:
        return redirect('/')


def SuperAdmin_ViewPrevioustraineeattendancesort(request,id):
    if 'SAdm_id' in request.session:
        if request.session.has_key('SAdm_id'):
                SAdm_id = request.session['SAdm_id']
        users = User.objects.filter(id=SAdm_id)
        usr=user_registration.objects.get(id=id)
        if request.method == "POST":
            fromdate = request.POST.get('fromdate')
            todate = request.POST.get('todate') 
            adata = attendance.objects.filter(date__range=[fromdate,todate]).filter(user_id=id)
        return render(request,'SuperAdmin_ViewPrevioustraineeattendancesort.html',{'users':users,'adata':adata,'user_registration':usr})
    else:
        return redirect('/')
    
   
def SuperAdmin_View_Trainerattendance(request,id):
    if 'SAdm_id' in request.session:
        if request.session.has_key('SAdm_id'):
                SAdm_id = request.session['SAdm_id']
        users = User.objects.filter(id=SAdm_id)
        usr=user_registration.objects.get(id=id)
        return render(request,'SuperAdmin_View_Trainerattendance.html', {'users':users,'user_registration':usr})
    else:
        return redirect('/')


def SuperAdmin_ViewTrainerattendancesort(request,id):  
    if 'SAdm_id' in request.session:
        if request.session.has_key('SAdm_id'):
                SAdm_id = request.session['SAdm_id']
        users = User.objects.filter(id=SAdm_id)
        usr=user_registration.objects.get(id=id)
        if request.method == "POST":
            fromdate = request.POST.get('fromdate')
            todate = request.POST.get('todate') 
            adata = attendance.objects.filter(date__range=[fromdate,todate]).filter(user_id=id)
        return render(request,'SuperAdmin_ViewTrainerattendancesort.html',{'users':users,'adata':adata,'user_registration':usr})
    else:
        return redirect('/')
    

def SuperAdmin_View_Previoustraineeprofile(request,id):   
    if 'SAdm_id' in request.session:
        if request.session.has_key('SAdm_id'):
                SAdm_id = request.session['SAdm_id']
        users = User.objects.filter(id=SAdm_id)
        usr=user_registration.objects.get(id=id)
        labels = []
        data = []
        queryset = user_registration.objects.filter(id=id)
        for i in queryset:
            labels=[i.workperformance,i.attitude,i.creativity]
            data=[i.workperformance,i.attitude,i.creativity]
        return render(request,'SuperAdmin_View_Previoustraineeprofile.html', {'users':users,'user_registration':usr,'labels':labels,'data':data})
    else:
        return redirect('/')
    
    
def SuperAdmin_proname(request,id):
    if 'SAdm_id' in request.session:
        if request.session.has_key('SAdm_id'):
                SAdm_id = request.session['SAdm_id']
        users = User.objects.filter(id=SAdm_id)
        Project_man_data = user_registration.objects.get(id = id)
        labels = []
        data = []
        queryset = user_registration.objects.filter(id=id)
        for i in queryset:
            labels=[i.workperformance,i.attitude,i.creativity]
            data=[i.workperformance,i.attitude,i.creativity]
        return render(request,'SuperAdmin_proname.html',{'users':users,'pro_man_data':Project_man_data,'labels':labels,'data':data})
    else:
        return redirect('/')
    

def SuperAdmin_proinvolve(request,id):
    if 'SAdm_id' in request.session:
        if request.session.has_key('SAdm_id'):
                SAdm_id = request.session['SAdm_id']
        users = User.objects.filter(id=SAdm_id)
        Pro_data = project.objects.filter(projectmanager_id = id).order_by("-id")
        return render(request,'SuperAdmin_proinvolve.html',{'users':users,'pro_data':Pro_data})
    else:
        return redirect('/')
    
def SuperAdmin_promanatten(request,id):
    if 'SAdm_id' in request.session:
        if request.session.has_key('SAdm_id'):
                SAdm_id = request.session['SAdm_id']
        users = User.objects.filter(id=SAdm_id)
        id = id
        return render(request, 'SuperAdmin_promanatten.html',{'users':users,'id':id})
    else:
        return redirect('/')

def SuperAdmin_promanattendsort(request,id):
    if 'SAdm_id' in request.session:
        if request.session.has_key('SAdm_id'):
                SAdm_id = request.session['SAdm_id']
        users = User.objects.filter(id=SAdm_id)
        id = id
        if request.method == "POST":
            fromdate = request.POST.get('fromdate')
            todate = request.POST.get('todate') 
                # mem1 = attendance.objects.raw('select * from app_attendance where user_id and date between "'+fromdate+'" and "'+todate+'"')
            mem1 = attendance.objects.filter(date__range=[fromdate, todate]).filter(user_id = id)
        return render(request, 'SuperAdmin_promanattensort.html',{'users':users,'mem1':mem1,'id':id})
    else:
        return redirect('/')
    

def SuperAdmin_admin_registration(request):
    if 'SAdm_id' in request.session:
        if request.session.has_key('SAdm_id'):
                SAdm_id = request.session['SAdm_id']
        users = User.objects.filter(id=SAdm_id)
        return render(request,'SuperAdmin_admin_registration.html',{'users':users})
    else:
        return redirect('/')

def SuperAdmin_registration(request):
    if 'SAdm_id' in request.session:
        if request.session.has_key('SAdm_id'):
                SAdm_id = request.session['SAdm_id']
        users = User.objects.filter(id=SAdm_id)
        branches=branch_registration.objects.all()
        
        return render(request,'SuperAdmin_registration.html',{'users':users,'branches':branches,})
    else:
        return redirect('/')

def SuperAdmin_Add(request):
    if 'SAdm_id' in request.session:
        if request.session.has_key('SAdm_id'):
                SAdm_id = request.session['SAdm_id']
        users = User.objects.filter(id=SAdm_id)
        des=designation.objects.get(designation="admin")
        if request.method == 'POST':
            fn1 = request.POST['fname']
            fn2 = request.POST['faname']
            fn3 = request.POST['adob']
            fn4 = request.POST['agender']
            fn5 = request.POST['amobile']
            fn6 = request.POST['aemail']
            fn7 = request.POST['aalternative']
            fn8 = request.POST['Adminbranch']
            fn9 = request.FILES['aproof']
            fn10 = request.FILES['cphoto']
            
           
            
            new2 = user_registration(fullname=fn1, fathername=fn2, dateofbirth=fn3, gender=fn4, mobile=fn5, email=fn6, alternativeno=fn7,branch_id=fn8,
                                    idproof=fn9, photo=fn10,designation_id=des.id)
            new2.save()
            return render(request,'SuperAdmin_registration.html',{'users':users})
        else:
            return redirect('SuperAdmin_registration')
    else:
        return redirect('/')




def SuperAdmin_admin_view(request):
    if 'SAdm_id' in request.session:
        if request.session.has_key('SAdm_id'):
                SAdm_id = request.session['SAdm_id']
        users = User.objects.filter(id=SAdm_id)
        designations=designation.objects.get(designation='Admin')
        user=user_registration.objects.filter(designation=designations)
        return render(request,'SuperAdmin_view_admin.html',{'users':users,'user_registration':user,'designation':designations})
    else:
        return redirect('/')

def admindelete(request, id):
    
    user = user_registration.objects.get(id=id)
    try:
        user.delete()
        return redirect('SuperAdmin_admin_view')
    except:
        messages.success(request, "  Error Occured: It can't be deleted, it used as ForeignKey Constrain !!")
        return redirect('SuperAdmin_admin_view')


def SuperAdmin_admin_update(request,id):
    if 'SAdm_id' in request.session:
        if request.session.has_key('SAdm_id'):
                SAdm_id = request.session['SAdm_id']
        users = User.objects.filter(id=SAdm_id)
        user=user_registration.objects.get(id=id)
        branchs=branch_registration.objects.all()

        return render(request,'SuperAdmin_update_admin.html',{'users':users,'user_registration':user,'branch_registration':branchs})
    else:
        return redirect('/')

def SuperAdmin_updatesave(request,id):
    if 'SAdm_id' in request.session:
        if request.session.has_key('SAdm_id'):
                SAdm_id = request.session['SAdm_id']
        users = User.objects.filter(id=SAdm_id)
        if request.method == 'POST':
            usr = user_registration.objects.get(id=id)
            usr.fullname = request.POST.get('aname')
            usr.fathername = request.POST.get('fname')
            usr.dateofbirth = request.POST.get('date')
            usr.gender = request.POST.get('gen')
            usr.mobile = request.POST.get('mob')
            usr.email = request.POST.get('mail')
            usr.alternativeno = request.POST.get('alternative')
            try:
                usr.idproof = request.FILES['idp']
                usr.photo = request.FILES['pic']
            except:
                pass
            
            br_id = request.POST.get("Adminbranch")
            usr.branch_id = br_id
            usr.save()
            return redirect('SuperAdmin_admin_view')
        else:
            return render(request,'SuperAdmin_update_admin.html',{'users':users})

    else:
        return redirect('/')






def SuperAdmin_Branch(request):
    if 'SAdm_id' in request.session:
        if request.session.has_key('SAdm_id'):
                SAdm_id = request.session['SAdm_id']
        users = User.objects.filter(id=SAdm_id)
        if request.session.has_key('SAdm_id'):
                SAdm_id = request.session['SAdm_id']
        users = User.objects.filter(id=SAdm_id)
        return render(request,'SuperAdmin_Branch.html',{'users':users})
    else:
        return redirect('/')

def SuperAdmin_AddBranch(request):
    if 'SAdm_id' in request.session:
        if request.session.has_key('SAdm_id'):
                SAdm_id = request.session['SAdm_id']
        users = User.objects.filter(id=SAdm_id)
        if request.method == 'POST':
            br1 = request.POST['Brname']
            br2 = request.POST['location']
            br3 = request.POST['Brtype']
            br4 = request.POST['Bradmin']
            br5 = request.POST['Bremail']
            br6 = request.POST['Brcontact']
            br7 = request.FILES['img[]']
    
            new1 = branch_registration(branch_name=br1,location=br2,
                                      branch_type=br3, branch_admin=br4,logo = br7,
                                      email= br5,mobile =br6)
            new1.save()
    
        return render(request,'SuperAdmin_AddBranch.html',{'users':users})
    else:
        return redirect('/')


def SuperAdmin_Viewbranch(request):
    if 'SAdm_id' in request.session:
        if request.session.has_key('SAdm_id'):
            SAdm_id = request.session['SAdm_id']
        users = User.objects.filter(id=SAdm_id)

        branch=branch_registration.objects.all()
        return render(request,'SuperAdmin_Viewbranch.html',{'users':users,'branch_registration':branch})
    else:
        return redirect('/')

def SuperAdmin_Updatebranch(request,id):
    if 'SAdm_id' in request.session:
        if request.session.has_key('SAdm_id'):
            SAdm_id = request.session['SAdm_id']
        users = User.objects.filter(id=SAdm_id)

        branch=branch_registration.objects.get(id=id)
       
        return render(request,'SuperAdmin_Updatebranch.html',{'users':users,'branch_registration':branch})
    else:
        return redirect('/')

def SuperAdmin_branchupdate(request,id):
    if 'SAdm_id' in request.session:
        if request.session.has_key('SAdm_id'):
                SAdm_id = request.session['SAdm_id']
        users = User.objects.filter(id=SAdm_id)
        if request.method=="POST":
            br=branch_registration.objects.get(id=id)
            br.branch_name=request.POST['brname']
            br.location=request.POST['brlocation']
            br.branch_type=request.POST['brtype']
            br.branch_admin=request.POST['bradmin']
            br.email=request.POST['bremail']
            br.mobile=request.POST['brmobile']
            br.save()
            
            lg=branch_registration.objects.get(id=id)
            try: 
                lg.logo = request.FILES['photo']
                lg.save()
            except:
                br.save()
        
            return redirect('SuperAdmin_Viewbranch')
        else:
            return render(request,'SuperAdmin_Viewbranch.html',{'users':users})
    else:
        return redirect('/')

def SuperAdmin_Branchdelete(request,id):
    branch=branch_registration.objects.get(id=id)
    try:
        
        branch.delete()
        return redirect('SuperAdmin_Viewbranch')
    except:
        messages.success(request, "  Error Occured: It can't be deleted, it used as ForeignKey Constrain !!")
        return redirect('SuperAdmin_Viewbranch')


def SuperAdmin_ReportedissueShow(request,id):
    if 'SAdm_id' in request.session:
        if request.session.has_key('SAdm_id'):
                SAdm_id = request.session['SAdm_id']
        users = User.objects.filter(id=SAdm_id)
        ad_id = designation.objects.get(designation="admin")
        admin_id = ad_id.id
        reported_issues=reported_issue.objects.all()
        user1=user_registration.objects.all()
        return render(request,'SuperAdmin_ReportedissueShow.html',{'users':users,'reported_issue':reported_issues,'user1':user1, 'admin_id':admin_id})
    else:
        return redirect('/')

def SuperAdmin_Reportedissue_department(request):
    if 'SAdm_id' in request.session:
        if request.session.has_key('SAdm_id'):
                SAdm_id = request.session['SAdm_id']
        users = User.objects.filter(id=SAdm_id)
        branch=branch_registration.objects.all()
        file = user_registration.objects.all()
        return render(request, 'SuperAdmin_Reportedissue_department.html',{'users':users,'branches':branch,'files':file})
    else:
        return redirect('/')

def SuperAdminreply(request,id):
    if 'SAdm_id' in request.session:
        if request.session.has_key('SAdm_id'):
                SAdm_id = request.session['SAdm_id']
        users = User.objects.filter(id=SAdm_id)
        if request.method == 'POST':
            v = reported_issue.objects.get(id=id)
            v.reply=request.POST.get('reply')
            v.save()
            return redirect('SuperAdmin_Reportedissue_department')
        else:
            return render(request,'SuperAdmin_ReportedissueShow.html',{'users':users})
    else:
        return redirect('/')
        
def trainer_currentprogress(request,id):
    if 'usernametrnr2' in request.session:
        if request.session.has_key('usernametrnr2'):
            usernametrnr2 = request.session['usernametrnr2']
        z = user_registration.objects.filter(id=usernametrnr2)
        var = user_registration.objects.get(id=id)
        
        
        
        if request.method == 'POST':
            mm = previousTeam.objects.get(user=id,teamname=var.team_id)
            print(mm.user)
            mm.progress = request.POST['sele1']
            mm.save()
            
            msg_success = "Progress submitted"
            return render(request, 'trainer_currentprogress.html', {'z': z,'msg_success':msg_success,'var':var})
        return render(request, 'trainer_currentprogress.html', {'z': z,'var':var, 'old_pr':old_pr})
    else:
        return render('/')
        
def trainer_currentprogress(request,id):
    if 'usernametrnr2' in request.session:
        if request.session.has_key('usernametrnr2'):
            usernametrnr2 = request.session['usernametrnr2']
        z = user_registration.objects.filter(id=usernametrnr2)
        var = user_registration.objects.get(id=id)
       
        old_pr = previousTeam.objects.get(user=id,teamname_id=var.team_id)
        
        if request.method == 'POST':
            mm = previousTeam.objects.get(user=id,teamname=var.team_id)
            print(mm.user)
            mm.progress = request.POST['sele1']
            mm.save()
            
            msg_success = "Progress submitted"
            return render(request, 'trainer_currentprogress.html', {'z': z,'msg_success':msg_success,'var':var})
        return render(request, 'trainer_currentprogress.html', {'z': z,'var':var, 'old_pr':old_pr})
    else:
        return render('/')



def BRadmin_new_registration(request):
    if request.session.has_key('Adm_id'):
        Adm_id = request.session['Adm_id']
    else:
        return redirect('/')
    if request.method == "POST":
        u_id = request.POST.get("id")
        dept_id = request.POST.get("dept")
        desi_id = request.POST.get("des")
        res = request.POST.get("stat")

        user = user_registration.objects.get(id=u_id)
        user.department_id = dept_id
        user.status = res
        user.designation_id = desi_id
        user.save()
        return redirect("BRadmin_new_registration")
    Adm = user_registration.objects.filter(id=Adm_id)
    mem1 = user_registration.objects.filter(~Q(status="resigned"),reg_status=0).order_by("-id")
    mem2 = designation.objects.filter(~Q(designation="admin"))
    mem3 = department.objects.all()
    return render(request, 'BRadmin_new_registration.html', {'mem3': mem3, 'mem2': mem2, 'Adm': Adm, 'mem1': mem1})


def registrationstatus(request, id):
    man = user_registration.objects.get(id=id)
    man.reg_status = "1"    
    man.save()
    return redirect('BRadmin_new_registration')

def BRadmin_internship_pending(request):
    if request.session.has_key('Adm_id'):
        Adm_id = request.session['Adm_id']
    else:
        return redirect('/')
    Adm = user_registration.objects.filter(id=Adm_id)

    data=internship.objects.filter(complete_status='0')
    use=internship_type.objects.all()
   
    return render(request, 'BRadmin_internship_pending.html', {'data': data,'use': use,'Adm':Adm})

def BRadmin_internship_acc_approved(request):
    if request.session.has_key('Adm_id'):
        Adm_id = request.session['Adm_id']
    else:
        return redirect('/')
    Adm = user_registration.objects.filter(id=Adm_id)
    data=internship.objects.filter(verify_status='1')
    use=internship_type.objects.all()

    return render(request, 'BRadmin_internship_acc_approved.html', {'data': data ,'use':use, 'Adm':Adm})



def BRadmin_accounts(request):
    if 'Adm_id' in request.session:
        if request.session.has_key('Adm_id'):
            Adm_id = request.session['Adm_id']
        else:
            return redirect('/')
        Adm = user_registration.objects.filter(id=Adm_id)
        return render(request, 'BRadmin_accounts.html', {'Adm': Adm})
    else:
        return redirect('/')

def BRadmin_accounts_traineepayment_notverified(request):
    if 'Adm_id' in request.session:
        if request.session.has_key('Adm_id'):
            Adm_id = request.session['Adm_id']
        else:
            return redirect('/')
        Adm = user_registration.objects.filter(id=Adm_id)
        des = designation.objects.get(designation='trainee')
        deta = user_registration.objects.filter(designation=des.id)
        return render(request,'BRadmin_accounts_traineepayment_notverified.html', { 'Adm': Adm, 'deta':deta})
    else:
        return redirect('/')

def BRadmin_accounts_traineepayment_pending(request):
    if 'Adm_id' in request.session:
        if request.session.has_key('Adm_id'):
            Adm_id = request.session['Adm_id']
        else:
            return redirect('/')
        Adm = user_registration.objects.filter(id=Adm_id)
        des = designation.objects.get(designation='trainee')
        deta = user_registration.objects.filter(designation=des.id)
        return render(request,'BRadmin_accounts_traineepayment_pending.html', { 'Adm': Adm, 'deta': deta })
    else:
        return redirect('/')

def BRadmin_accounts_newtrainees(request):
    if 'Adm_id' in request.session:
        if request.session.has_key('Adm_id'):
            Adm_id = request.session['Adm_id']
        else:
            return redirect('/')
        Adm = user_registration.objects.filter(id=Adm_id)
        des = designation.objects.get(designation='trainee')
        deta = user_registration.objects.filter(designation=des.id)
        return render(request,'BRadmin_accounts_newtrainees.html', { 'Adm': Adm, 'deta':deta })
    else:
        return redirect('/')

def BRadmin_accounts_salaried_employees(request):
    if 'Adm_id' in request.session:
        if request.session.has_key('Adm_id'):
            Adm_id = request.session['Adm_id']
        else:
            return redirect('/')
        Adm = user_registration.objects.filter(id=Adm_id)
        vars = user_registration.objects.filter(confirm_salary_status=1).order_by("-id")
        return render(request,'BRadmin_accounts_salaried_employees.html', {'Adm': Adm,'vars':vars})
    else:
        return redirect('/')

def BRadmin_accounts_salary_employees(request):
    if 'Adm_id' in request.session:
        if request.session.has_key('Adm_id'):
            Adm_id = request.session['Adm_id']
        else:
            return redirect('/')
        Adm = user_registration.objects.filter(id=Adm_id)
        des2 = designation.objects.get(designation='trainee')
        Adm1 = designation.objects.get(designation="Admin")
        vars = user_registration.objects.exclude(designation=des2.id).exclude(designation=Adm1.id).order_by("-id")
        return render(request,'BRadmin_accounts_salary_employees.html', {'Adm': Adm,'vars':vars})
    else:
        return redirect('/')   

def BRadmin_accounts_internship(request):
    if 'Adm_id' in request.session:
        if request.session.has_key('Adm_id'):
            Adm_id = request.session['Adm_id']
        else:
            return redirect('/')
        Adm = user_registration.objects.filter(id=Adm_id)
   
        return render(request, 'BRadmin_accounts_internship.html', {'Adm': Adm})
    else:
        return redirect('/')   


def BRadmin_accounts_internship_viewall(request):
    if 'Adm_id' in request.session:
        if request.session.has_key('Adm_id'):
            Adm_id = request.session['Adm_id']
        else:
            return redirect('/')
        Adm = user_registration.objects.filter(id=Adm_id)

        data=internship.objects.filter(complete_status='1')
        use=internship_type.objects.all()
    
        return render(request, 'BRadmin_accounts_internship_viewall.html', {'Adm': Adm,'data': data,'use': use})
    else:
        return redirect('/')   
    
def BRadmin_accounts_internship_payment_pending(request):
    if 'Adm_id' in request.session:
        if request.session.has_key('Adm_id'):
            Adm_id = request.session['Adm_id']
        else:
            return redirect('/')
        Adm = user_registration.objects.filter(id=Adm_id)

        data=internship.objects.filter(complete_status='0')
        use=internship_type.objects.all()
    
        return render(request, 'BRadmin_accounts_internship_payment_pending.html', {'Adm': Adm,'data': data,'use': use})
    else:
        return redirect('/')   

def BRadmin_accounts_intrenship_viewbydate(request):
    if 'Adm_id' in request.session:
        if request.session.has_key('Adm_id'):
            Adm_id = request.session['Adm_id']
        Adm = user_registration.objects.filter(id=Adm_id)

    newdata = internship.objects.filter(verify_status=1)
    return render(request, 'BRadmin_accounts_internship_viewbydate.html', {'Adm': Adm,'newdata':newdata})

def BRadmin_accounts_internship_dateview(request):  
    if 'Adm_id' in request.session:
        if request.session.has_key('Adm_id'):
            Adm_id = request.session['Adm_id']
        Adm = user_registration.objects.filter(id=Adm_id)
    reg_date = request.GET.get('date')  
    # empid = internship.objects.get(id=id)  
    empid = internship.objects.filter(reg_date=reg_date)  
    return render(request, 'BRadmin_accounts_internship_dateview.html',{'Adm': Adm, 'empid':empid})  

def BRadmin_accounts_internship_update(request, id):
    if 'Adm_id' in request.session:
        if request.session.has_key('Adm_id'):
            Adm_id = request.session['Adm_id']
        Adm = user_registration.objects.filter(id=Adm_id)
    var = internship.objects.get(id=id)
    return render (request, 'BRadmin_accounts_internship_update.html', {'Adm': Adm,'var': var})


def BRadmin_accounts_interndelete(request, id):
    man = internship.objects.get(id=id)
    man.delete()
    return redirect('BRadmin_accounts_internship')

def BRadmin_accounts_internshipupdatesave(request, id):
    if 'Adm_id' in request.session:
        if request.session.has_key('Adm_id'):
            Adm_id = request.session['Adm_id']
        Adm = user_registration.objects.filter(id=Adm_id) 
  
        
        Adm = user_registration.objects.filter(id=Adm_id)
        var = internship.objects.get(id=id)
        var.fullname = request.POST['fullname']
        var.collegename = request.POST['college']
        var.reg_no = request.POST['regno']
        var.course = request.POST['course']
        var.stream = request.POST['stream']
        var.platform = request.POST['platform']
        # var.branch_id  =  request.POST['branch']
        var.start_date = request.POST['startdate']
        var.end_date = request.POST['enddate']
        var.mobile = request.POST['mobile']
        var.alternative_no = request.POST['altmob']
        var.email = request.POST['email']
        var.hrmanager = request.POST['hrmanager']
        var.guide = request.POST['guide']
        var.rating = request.POST['rating']
        var.save()
        return redirect('BRadmin_accounts_internship')

def BRadmin_monthdays(request):
    if 'Adm_id' in request.session:
        if request.session.has_key('Adm_id'):
            Adm_id = request.session['Adm_id']
        Adm = user_registration.objects.filter(id=Adm_id)
        return render(request,'BRadmin_monthdays.html', {'Adm': Adm})
    else:
        return redirect('/')
        
def BRadmin_viewdays(request):
    if 'Adm_id' in request.session:
        if request.session.has_key('Adm_id'):
            Adm_id = request.session['Adm_id']
        Adm = user_registration.objects.filter(id=Adm_id)
        mem = acnt_monthdays.objects.all()
        return render(request,'BRadmin_viewdays.html', {'Adm': Adm,'mem':mem})
    else:
        return redirect('/')
        
# def BRadmin_salary_given(request):
#     if 'Adm_id' in request.session:
#         if request.session.has_key('Adm_id'):
#             Adm_id = request.session['Adm_id']
#         Adm = user_registration.objects.filter(id=Adm_id)
#         mem = user_registration.objects.filter(salary_status=1)
#         return render(request,'BRadmin_salary_given.html', {'Adm': Adm,'mem':mem})
#     else:
#         return redirect('/')

def BRadmin_salary_given(request):
    if 'Adm_id' in request.session:
        if request.session.has_key('Adm_id'):
            Adm_id = request.session['Adm_id']
        Adm = user_registration.objects.filter(id=Adm_id)
        year = date.today().year
        month = date.today().month
        mem = acntspayslip.objects.filter(fromdate__year=year,
                                          fromdate__month=month)
        return render(request,'BRadmin_salary_given.html', {'Adm': Adm,'mem':mem})
    else:
        return redirect('/')


def BRadmin_project_dept(request):
     if 'Adm_id' in request.session:
        if request.session.has_key('Adm_id'):
            Adm_id = request.session['Adm_id']
        else:
            return redirect('/')
        Adm = user_registration.objects.filter(id=Adm_id)
        project_details = project.objects.all()
        depart = department.objects.all()
        return render(request, 'BRadmin_project_dept.html', {'proj_det': project_details, 'department': depart, 'Adm': Adm})
     else:
        return redirect('/')


def BRadmin_project_list(request,id):
    if 'Adm_id' in request.session:
        if request.session.has_key('Adm_id'):
            Adm_id = request.session['Adm_id']
        else:
            return redirect('/')
        Adm = user_registration.objects.filter(id=Adm_id)
        project_details = project.objects.filter(
            ~Q(status='Rejected'), department_id=id)
        return render(request, 'BRadmin_project_list.html', {'proj_det': project_details, 'Adm': Adm})
    else:
        return redirect('/')


def BRadmin_project_table(request,id):
    if 'Adm_id' in request.session:
        if request.session.has_key('Adm_id'):
            Adm_id = request.session['Adm_id']
        else:
            return redirect('/')
        Adm = user_registration.objects.filter(id=Adm_id)
        des = designation.objects.get(designation="team leader")
        dev = designation.objects.get(designation="developer")
        var = project_taskassign.objects.filter(
            project_id=id).order_by('-id')
        data = test_status.objects.filter(project_id=id).order_by('-id')
        data1 = tester_status.objects.filter(project_id=id).order_by('-id')
        newdata = project_taskassign.objects.filter(
            project_id=id, subtask__isnull=False).order_by('-id')
        return render(request, 'BRadmin_project_table.html', {'Adm': Adm, 'var': var, 'data': data, 'data1': data1, 'newdata': newdata})
    else:
        return redirect('/')

# def BRadmin_salary_pending(request):
#     if 'Adm_id' in request.session:
#         if request.session.has_key('Adm_id'):
#             Adm_id = request.session['Adm_id']
#         else:
#             return redirect('/')
#         Adm = user_registration.objects.filter(id=Adm_id)
#         mem = user_registration.objects.filter(salary_status=0)
#         return render(request,'BRadmin_salary_pending.html', {'Adm': Adm,'mem':mem})
#     else:
#         return redirect('/')

def BRadmin_salary_pending(request):
    if 'Adm_id' in request.session:
        if request.session.has_key('Adm_id'):
            Adm_id = request.session['Adm_id']
        Adm = user_registration.objects.filter(id=Adm_id)
        year = date.today().year
        month = date.today().month
        mem = acntspayslip.objects.filter(~Q(fromdate__year=year,
                                          fromdate__month=month))
        return render(request,'BRadmin_salary_pending.html', {'Adm': Adm,'mem':mem})
    else:
        return redirect('/')


# def accounts_intrenship_viewbydate(request):
#     if 'usernameacnt2' in request.session:
#         if request.session.has_key('usernameacnt2'):
#             usernameacnt2 = request.session['usernameacnt2']
#         z = user_registration.objects.filter(id=usernameacnt2)
        
#     newdata = internship.objects.filter(verify_status=1)
#     return render(request, 'accounts_internship_viewbydate.html', {'z':z,'newdata':newdata})

# def accounts_internship(request):
#     if 'usernameacnt2' in request.session:
#         if request.session.has_key('usernameacnt2'):
#             usernameacnt2 = request.session['usernameacnt2']
#         z = user_registration.objects.filter(id=usernameacnt2)
#         ipcount=internship.objects.filter(complete_status='0').count()
#         ivacount=internship.objects.filter(complete_status=1).count()
#         ivdcount=internship.objects.filter(verify_status=1).count()
#         return render(request,'accounts_internship.html',{'z': z,'ipcount':ipcount,'ivacount':ivacount,'ivdcount':ivdcount})
#     else:
#         return redirect('/')

# def accounts_internship_update(request, id):
#     if 'usernameacnt2' in request.session:  
#         if request.session.has_key('usernameacnt2'):  
#             usernameacnt2 = request.session['usernameacnt2']  
#         z = user_registration.objects.filter(id=usernameacnt2) 
#     var = internship.objects.get(id=id)
#     return render (request,'accounts_internship_update.html', {'z': z,'var': var})


# def accounts_interndelete(request, id):
#     man = internship.objects.get(id=id)
#     man.delete()
#     return redirect('accounts_internship')

# def accounts_internshipupdatesave(request, id):
#     if 'usernameacnt2' in request.session:  
#         if request.session.has_key('usernameacnt2'):  
#             usernameacnt2 = request.session['usernameacnt2']  
  
#         else:
#             return redirect('/')
#         Adm = user_registration.objects.filter(id=usernameacnt2)
#         var = internship.objects.get(id=id)
#         var.fullname = request.POST['fullname']
#         var.collegename = request.POST['college']
#         var.reg_no = request.POST['regno']
#         var.course = request.POST['course']
#         var.stream = request.POST['stream']
#         var.platform = request.POST['platform']
#         #var.branch_id  =  request.POST['branch']
#         var.start_date = request.POST['startdate']
#         var.end_date = request.POST['enddate']
#         var.mobile = request.POST['mobile']
#         var.alternative_no = request.POST['altmob']
#         var.email = request.POST['email']
#         var.hrmanager = request.POST['hrmanager']
#         var.guide = request.POST['guide']
#         var.rating = request.POST['rating']
#         var.save()
#         return redirect('accounts_internship')

def accounts_intrenship_viewbydate(request):
    if 'usernameacnt2' in request.session:
        if request.session.has_key('usernameacnt2'):
            usernameacnt2 = request.session['usernameacnt2']
        z = user_registration.objects.filter(id=usernameacnt2)
    newdata = internship.objects.all().values('reg_date').distinct()
    # newdata = internship.objects.filter(verify_status=1)
    return render(request, 'accounts_internship_viewbydate.html', {'z':z,'newdata':newdata})

def accounts_internship(request):
    if 'usernameacnt2' in request.session:
        if request.session.has_key('usernameacnt2'):
            usernameacnt2 = request.session['usernameacnt2']
        z = user_registration.objects.filter(id=usernameacnt2)
        ipcount=internship.objects.filter(complete_status='0').count()
        ivacount=internship.objects.filter(complete_status=1).count()
        ivdcount=internship.objects.filter(verify_status=1).count()
        return render(request,'accounts_internship.html',{'z': z,'ipcount':ipcount,'ivacount':ivacount,'ivdcount':ivdcount})
    else:
        return redirect('/')

def accounts_internship_update(request, id):
    if 'usernameacnt2' in request.session:  
        if request.session.has_key('usernameacnt2'):  
            usernameacnt2 = request.session['usernameacnt2']  
        z = user_registration.objects.filter(id=usernameacnt2) 
    var = internship.objects.get(id=id)
    return render (request,'accounts_internship_update.html', {'z': z,'var': var})
    
def accounts_internship_dateview(request):  
    if 'usernameacnt2' in request.session:  
        if request.session.has_key('usernameacnt2'):  
            usernameacnt2 = request.session['usernameacnt2']  
        z = user_registration.objects.filter(id=usernameacnt2)  

    reg_date = request.GET.get('date')    
    empid = internship.objects.filter(reg_date=reg_date)  
    return render(request, 'accounts_internship_dateview.html',{'z':z, 'empid':empid})  

def accounts_interndelete(request, id):
    man = internship.objects.get(id=id)
    man.delete()
    return redirect('accounts_internship')

def accounts_internshipupdatesave(request, id):
    if 'usernameacnt2' in request.session:  
        if request.session.has_key('usernameacnt2'):  
            usernameacnt2 = request.session['usernameacnt2']  
  
        else:
            return redirect('/')
        Adm = user_registration.objects.filter(id=usernameacnt2)
        var = internship.objects.get(id=id)
        var.fullname = request.POST['fullname']
        var.collegename = request.POST['college']
        var.reg_no = request.POST['regno']
        var.course = request.POST['course']
        var.stream = request.POST['stream']
        var.platform = request.POST['platform']
        # var.branch_id  =  request.POST['branch']
        var.start_date = request.POST['startdate']
        var.end_date = request.POST['enddate']
        var.mobile = request.POST['mobile']
        var.alternative_no = request.POST['altmob']
        var.email = request.POST['email']
        var.hrmanager = request.POST['hrmanager']
        var.guide = request.POST['guide']
        var.rating = request.POST['rating']
        var.save()
        return redirect('accounts_internship')
 
def trainer_save(request,id):  
    var = user_registration.objects.get(id=id)  
    var.trainer_level = request.POST['tr_level']  
    var.save()  
    msg_success="Added succesfully"
    return render(request, 'trainer.html', {'msg_success':msg_success})

# def accounts_internship_viewbydate(request):
#     if 'usernameacnt2' in request.session:
#         if request.session.has_key('usernameacnt2'):
#             usernameacnt2 = request.session['usernameacnt2']
#         z = user_registration.objects.filter(id=usernameacnt2)
        
#     newdata = internship.objects.all().values('reg_date').distinct()
#     return render(request, 'accounts_internship_viewbydate.html', {'z':z,'newdata':newdata})
    
# #################Emil
# def accounts_internship_dateview(request):  
#     if 'usernameacnt2' in request.session:  
#         if request.session.has_key('usernameacnt2'):  
#             usernameacnt2 = request.session['usernameacnt2']  
#         z = user_registration.objects.filter(id=usernameacnt2)  

#     reg_date = request.GET.get('date')    
#     empid = internship.objects.filter(reg_date=reg_date)  
#     return render(request, 'accounts_internship_dateview.html',{'z':z, 'empid':empid})  

# def accounts_internship_payment_pending(request):
#     if 'usernameacnt2' in request.session:
#         if request.session.has_key('usernameacnt2'):
#             usernameacnt2 = request.session['usernameacnt2']
#         z = user_registration.objects.filter(id=usernameacnt2)

#     data=internship.objects.filter(complete_status='0')
#     use=internship_type.objects.all()
   
#     return render(request, 'internship_payment_pending.html', {'z': z,'data': data,'use': use})

# def accounts_internship_type_sel(request,id):
#     if 'usernameacnt2' in request.session:
#         if request.session.has_key('usernameacnt2'):
#             usernameacnt2 = request.session['usernameacnt2']
#         z = user_registration.objects.filter(id=usernameacnt2)
#     data=internship.objects.all()
#     ab=internship.objects.get(id=id)
#     ab.internshiptype_id=request.POST['inter']    
#     use=internship_type.objects.get(id=int(request.POST['inter']))
#     ab.total_fee=use.fee
#     ab.save()
#     msg_success = "Add Succesfully"
   
   
#     return render(request, 'internship_payment_pending.html', {'z': z,'data': data,'msg_success': msg_success})

# def addamount(request,id):
#     if 'usernameacnt2' in request.session:
#         if request.session.has_key('usernameacnt2'):
#             usernameacnt2 = request.session['usernameacnt2']
#         z = user_registration.objects.filter(id=usernameacnt2)
#         if request.method == "POST":
            
#             abc = internship.objects.get(id=id)
           
#             abc.pay_date = request.POST['date']
#             abc.amount = request.POST['amount']
#             abc.total_pay= int(request.POST['amount'])+abc.total_pay
#             abc.balance = abc.total_fee - abc.total_pay

#             # member.total_pay = int(request.POST['amount'])+member.total_pay
#             # member.payment_balance = member.total_amount - member.total_pay


            
#             abc.save()
#             abcd = internship_paydata()
#             abcd.internship_user=abc
#             abcd.date = request.POST['date']
#             abcd.amount = request.POST['amount']
#             abcd.save()
#             msg_success = "Add Succesfully"
#             return render(request, 'internship_payment_pending.html', {'z': z,'msg_success': msg_success})
#         return render(request, 'internship_payment_pending.html', {'z': z,})
#     else:
#         return redirect('/')
    
# def accounts_internship_verify(request,id):
#     if 'usernameacnt2' in request.session:
#         if request.session.has_key('usernameacnt2'):
#             usernameacnt2 = request.session['usernameacnt2']
#         z = user_registration.objects.filter(id=usernameacnt2)

#     data=internship.objects.get(id=id)
#     data.verify_status=1
#     data.save()
#     msg_success = "Verifyed Succesfully"
#     return render(request, 'internship_payment_pending.html', {'z': z,'msg_success': msg_success})

# def accounts_internship_complete(request,id):
#     if 'usernameacnt2' in request.session:
#         if request.session.has_key('usernameacnt2'):
#             usernameacnt2 = request.session['usernameacnt2']
#         z = user_registration.objects.filter(id=usernameacnt2)

#     data=internship.objects.get(id=id)
#     data.complete_status=1
#     data.save()
#     msg_success = "Verifyed Succesfully"
#     return render(request, 'internship_payment_pending.html', {'z': z,'msg_success': msg_success})

# def accounts_internship_viewall(request):
#     if 'usernameacnt2' in request.session:
#         if request.session.has_key('usernameacnt2'):
#             usernameacnt2 = request.session['usernameacnt2']
#         z = user_registration.objects.filter(id=usernameacnt2)

#     data=internship.objects.filter(complete_status='1')
#     use=internship_type.objects.all()
   
#     return render(request, 'accounts_internship_viewall.html', {'z': z,'data': data,'use': use})
   
    


# #########################   jishnu   ##############################

# def accounts_intrenship_type(request):
#     if 'usernameacnt2' in request.session:
#         if request.session.has_key('usernameacnt2'):
#             usernameacnt2 = request.session['usernameacnt2']
#         z = user_registration.objects.filter(id=usernameacnt2)
#         mem = internship_type.objects.all()
        
#     return render(request, 'accounts_intrenship_type.html', {'z': z,'mem':mem,})

# def accounts_intrenship_add(request):
#     if 'usernameacnt2' in request.session:
#         if request.session.has_key('usernameacnt2'):
#             usernameacnt2 = request.session['usernameacnt2']
#         z = user_registration.objects.filter(id=usernameacnt2)

#         if request.method == 'POST':
#             vars = internship_type()
#             vars.type = request.POST['type']
#             vars.duration = request.POST['duration']
#             vars.fee = request.POST['fees']
#             vars.save()
#             msg_success = "Add Succesfully"
#             return render(request, 'accounts_intrenship_add.html', {'z': z,'msg_success':msg_success})

#     return render(request, 'accounts_intrenship_add.html', {'z': z,})

# def internshiptypeupdate(request, id):
#     if 'usernameacnt2' in request.session:
#         if request.session.has_key('usernameacnt2'):
#             usernameacnt2 = request.session['usernameacnt2']
#         z = user_registration.objects.filter(id=usernameacnt2)
#         if request.method == "POST":
#             vars = internship_type.objects.get(id=id)
#             vars.type = request.POST['types']
#             vars.duration = request.POST['durations']
#             vars.fee = request.POST['fees']
#             vars.save()
#             msg_success = "Updated Succesfully"
#             return render(request, 'accounts_intrenship_type.html', {'z': z, 'msg_success':msg_success })
#         return render(request, 'accounts_intrenship_type.html', {'z': z, })
#     else:
#         return redirect('/')

# def internshiptypedelete(request, id):
#     if 'usernameacnt2' in request.session:
#         if request.session.has_key('usernameacnt2'):
#             usernameacnt2 = request.session['usernameacnt2']
#         z = user_registration.objects.filter(id=usernameacnt2)
#         vars = internship_type.objects.get(id=id)
#         vars.delete()
#         msg_success = "Deleted Succesfully"
#         return render(request, 'accounts_intrenship_type.html', {'z': z, 'msg_success':msg_success })
#     else:
#         return redirect('/')
        
def accounts_internship_viewbydate(request):
    if 'usernameacnt2' in request.session:
        if request.session.has_key('usernameacnt2'):
            usernameacnt2 = request.session['usernameacnt2']
        z = user_registration.objects.filter(id=usernameacnt2)
        
    newdata = internship.objects.all().values('reg_date').distinct()
    return render(request, 'accounts_internship_viewbydate.html', {'z':z,'newdata':newdata})
    
# Emil
def accounts_internship_dateview(request):  
    if 'usernameacnt2' in request.session:  
        if request.session.has_key('usernameacnt2'):  
            usernameacnt2 = request.session['usernameacnt2']  
        z = user_registration.objects.filter(id=usernameacnt2)  

    reg_date = request.GET.get('date')    
    empid = internship.objects.filter(reg_date=reg_date)  
    return render(request, 'accounts_internship_dateview.html',{'z':z, 'empid':empid})  

def accounts_internship_payment_pending(request):
    if 'usernameacnt2' in request.session:
        if request.session.has_key('usernameacnt2'):
            usernameacnt2 = request.session['usernameacnt2']
        z = user_registration.objects.filter(id=usernameacnt2)

    data=internship.objects.filter(complete_status='0')
    use=internship_type.objects.all()
   
    return render(request, 'internship_payment_pending.html', {'z': z,'data': data,'use': use})

def accounts_internship_type_sel(request,id):
    if 'usernameacnt2' in request.session:
        if request.session.has_key('usernameacnt2'):
            usernameacnt2 = request.session['usernameacnt2']
        z = user_registration.objects.filter(id=usernameacnt2)
    data=internship.objects.all()
    ab=internship.objects.get(id=id)
    ab.internshiptype_id=request.POST['inter']    
    use=internship_type.objects.get(id=int(request.POST['inter']))
    ab.total_fee=use.fee
    ab.save()
    msg_success = "Add Succesfully"
   
   
    return render(request, 'internship_payment_pending.html', {'z': z,'data': data,'msg_success': msg_success})

def addamount(request,id):
    if 'usernameacnt2' in request.session:
        if request.session.has_key('usernameacnt2'):
            usernameacnt2 = request.session['usernameacnt2']
        z = user_registration.objects.filter(id=usernameacnt2)
        if request.method == "POST":
            
            abc = internship.objects.get(id=id)
           
            abc.pay_date = request.POST['date']
            abc.amount = request.POST['amount']
            abc.total_pay= int(request.POST['amount'])+abc.total_pay
            abc.balance = abc.total_fee - abc.total_pay

            # member.total_pay = int(request.POST['amount'])+member.total_pay
            # member.payment_balance = member.total_amount - member.total_pay


            
            abc.save()
            abcd = internship_paydata()
            abcd.internship_user=abc
            abcd.date = request.POST['date']
            abcd.amount = request.POST['amount']
            abcd.save()
            msg_success = "Add Succesfully"
            return render(request, 'internship_payment_pending.html', {'z': z,'msg_success': msg_success})
        return render(request, 'internship_payment_pending.html', {'z': z,})
    else:
        return redirect('/')
    
def accounts_internship_verify(request,id):
    if 'usernameacnt2' in request.session:
        if request.session.has_key('usernameacnt2'):
            usernameacnt2 = request.session['usernameacnt2']
        z = user_registration.objects.filter(id=usernameacnt2)

    data=internship.objects.get(id=id)
    data.verify_status=1
    data.save()
    msg_success = "Verifyed Succesfully"
    return render(request, 'internship_payment_pending.html', {'z': z,'msg_success': msg_success})

def accounts_internship_complete(request,id):
    if 'usernameacnt2' in request.session:
        if request.session.has_key('usernameacnt2'):
            usernameacnt2 = request.session['usernameacnt2']
        z = user_registration.objects.filter(id=usernameacnt2)

    data=internship.objects.get(id=id)
    data.complete_status=1
    data.save()
    msg_success = "Verifyed Succesfully"
    return render(request, 'internship_payment_pending.html', {'z': z,'msg_success': msg_success})

def accounts_internship_viewall(request):
    if 'usernameacnt2' in request.session:
        if request.session.has_key('usernameacnt2'):
            usernameacnt2 = request.session['usernameacnt2']
        z = user_registration.objects.filter(id=usernameacnt2)

    data=internship.objects.filter(complete_status='1')
    use=internship_type.objects.all()
   
    return render(request, 'accounts_internship_viewall.html', {'z': z,'data': data,'use': use})
   
    


#########################   jishnu   ##############################

def accounts_intrenship_type(request):
    if 'usernameacnt2' in request.session:
        if request.session.has_key('usernameacnt2'):
            usernameacnt2 = request.session['usernameacnt2']
        z = user_registration.objects.filter(id=usernameacnt2)
        mem = internship_type.objects.all()
        
    return render(request, 'accounts_intrenship_type.html', {'z': z,'mem':mem,})

def accounts_intrenship_add(request):
    if 'usernameacnt2' in request.session:
        if request.session.has_key('usernameacnt2'):
            usernameacnt2 = request.session['usernameacnt2']
        z = user_registration.objects.filter(id=usernameacnt2)

        if request.method == 'POST':
            vars = internship_type()
            vars.type = request.POST['type']
            vars.duration = request.POST['duration']
            vars.fee = request.POST['fees']
            vars.save()
            msg_success = "Add Succesfully"
            return render(request, 'accounts_intrenship_add.html', {'z': z,'msg_success':msg_success})

    return render(request, 'accounts_intrenship_add.html', {'z': z,})

def internshiptypeupdate(request, id):
    if 'usernameacnt2' in request.session:
        if request.session.has_key('usernameacnt2'):
            usernameacnt2 = request.session['usernameacnt2']
        z = user_registration.objects.filter(id=usernameacnt2)
        if request.method == "POST":
            vars = internship_type.objects.get(id=id)
            vars.type = request.POST['types']
            vars.duration = request.POST['durations']
            vars.fee = request.POST['fees']
            vars.save()
            msg_success = "Updated Succesfully"
            return render(request, 'accounts_intrenship_type.html', {'z': z, 'msg_success':msg_success })
        return render(request, 'accounts_intrenship_type.html', {'z': z, })
    else:
        return redirect('/')

def internshiptypedelete(request, id):
    if 'usernameacnt2' in request.session:
        if request.session.has_key('usernameacnt2'):
            usernameacnt2 = request.session['usernameacnt2']
        z = user_registration.objects.filter(id=usernameacnt2)
        vars = internship_type.objects.get(id=id)
        vars.delete()
        msg_success = "Deleted Succesfully"
        return render(request, 'accounts_intrenship_type.html', {'z': z, 'msg_success':msg_success })
    else:
        return redirect('/')        

def projectmanager_workstatus(request):
    if 'prid' in request.session:
        if request.session.has_key('prid'):
            prid = request.session['prid']
        else:
            return redirect('/')
        pro = user_registration.objects.filter(id=prid)
        dept  = user_registration.objects.get(id=prid)

        cous = course.objects.all()
        dep = department.objects.filter(id=dept.department_id)
        des = designation.objects.all()
        emp = user_registration.objects.all()

        return render(request,'projectmanager_workstatus.html',{'pro':pro, 'cous':cous,'dep':dep,'des':des,'emp':emp,})
    else:
        return redirect('/')


@csrf_exempt
def projectmanager_designation(request):
    if 'prid' in request.session:
        if request.session.has_key('prid'):
            prid = request.session['prid']
        else:
            return redirect('/')
        pro = user_registration.objects.filter(id=prid)

        dept_id = request.GET.get('dept_id')
        
        br_id = department.objects.get(id=dept_id)
        Desig = designation.objects.filter(~Q(designation="admin"),~Q(designation="manager"),~Q(designation="project manager"),~Q(designation="tester"),~Q(designation="trainingmanager"),~Q(designation="trainer"),~Q(designation="trainee"),~Q(designation="account"),~Q(designation="hr")).filter(branch_id=br_id.branch_id)
        return render(request,'projectmanager_designation.html',{'pro':pro,'Desig': Desig, })
    else:
        return redirect('/')


@csrf_exempt
def projectmanager_emp_ajax(request):
    if 'prid' in request.session:
        if request.session.has_key('prid'):
            prid = request.session['prid']
        else:
            return redirect('/')
        pro = user_registration.objects.filter(id=prid)

        dept_id = request.GET.get('dept_id')
        desigId = request.GET.get('desigId')
        Desig = user_registration.objects.filter(department_id=dept_id, designation_id=desigId)

        return render(request,'projectmanager_emp_ajax.html',{'pro':pro,'Desig': Desig,})
    else:
        return redirect('/')

@csrf_exempt
def projectmanager_projects_details(request):
    if 'prid' in request.session:
        emp = request.POST['emp']
        fdate = request.POST['fdate']
        tdate = request.POST['tdate']
        names = project_taskassign.objects.filter(developer=emp,startdate__gte=fdate, enddate__lte=tdate) 
        print(emp)
        print(fdate)
        print(tdate)
        print(names)
        year = date.today().year
        month = date.today().month

        leave = project_taskassign.objects.filter(developer=emp,startdate__year__gte=year,
                                          startdate__month__gte=month,
                                          submitted_date__year__lte=year,
                                          submitted_date__month__lte=month)
        mm = leave.values_list('delay', flat='true')

        a=0
        for i in mm:
            
            a=a+int(i)


        return render(request,'projectmanager_projects_details.html', {'names':names,'mm':mm,'a':a ,})
    else:
        return redirect('/')

# Error fix:

# def accounts_traineepayment_notverified(request):
#     if 'usernameacnt2' in request.session:
#         if request.session.has_key('usernameacnt2'):
#             usernameacnt2 = request.session['usernameacnt2']
#         z = user_registration.objects.filter(id=usernameacnt2)
#         des = designation.objects.get(designation='trainee')
#         deta = user_registration.objects.filter(designation=des.id)
#         return render(request, 'accounts_traineepayment_notverified.html', {'z': z, 'deta': deta})
#     else:
#         return redirect('/')


# def verified(request, id):
#     rem = user_registration.objects.get(id=id)
#     rem.payment_status = 2
#     rem.save()
#     return redirect('/accounts_traineepayment_notverified')


# def accounts_traineepayment_pending(request):
#     if 'usernameacnt2' in request.session:
#         if request.session.has_key('usernameacnt2'):
#             usernameacnt2 = request.session['usernameacnt2']
#         z = user_registration.objects.filter(id=usernameacnt2)
#         des = designation.objects.get(designation='trainee')
#         deta = user_registration.objects.filter(designation=des.id)

#         return render(request, 'accounts_traineepayment_pending.html', {'z': z, 'deta': deta})
#     else:
#         return redirect('/')


# def accounts_newtrainees(request):
#     if 'usernameacnt2' in request.session:
#         if request.session.has_key('usernameacnt2'):
#             usernameacnt2 = request.session['usernameacnt2']
#         z = user_registration.objects.filter(id=usernameacnt2)
#         des = designation.objects.get(designation='trainee')
#         deta = user_registration.objects.filter(designation=des.id)
#         return render(request, 'accounts_newtrainees.html', {'z': z, 'deta': deta})
#     else:
#         return redirect('/')


# def accounts_salary_employees(request):
#     if 'usernameacnt2' in request.session:
#         if request.session.has_key('usernameacnt2'):
#             usernameacnt2 = request.session['usernameacnt2']
#         z = user_registration.objects.filter(id=usernameacnt2)
#         des2 = designation.objects.get(designation='trainee')
#         Adm1 = designation.objects.get(designation="Admin")
#         vars = user_registration.objects.exclude(
#             designation=des2.id).exclude(designation=Adm1.id).order_by("-id")
#         return render(request, 'accounts_salary_employees.html', {'z': z, 'vars': vars})
#     else:
#         return redirect('/')


# def accounts_salaryconfirm(request, id):
#     if 'usernameacnt2' in request.session:
#         if request.session.has_key('usernameacnt2'):
#             usernameacnt2 = request.session['usernameacnt2']
#         z = user_registration.objects.filter(id=usernameacnt2)

#         des2 = designation.objects.get(designation='trainee')
#         Adm1 = designation.objects.get(designation="Admin")
#         vars = user_registration.objects.exclude(
#             designation=des2.id).exclude(designation=Adm1.id).order_by("-id")
#         if request.method == 'POST':
#             var = user_registration.objects.get(id=id)
#             var.confirm_salary = request.POST['salary']
#             var.confirm_salary_status = 1
#             var.save()
#             msg_success = "submitted successfully"
#             return render(request, 'accounts_salary_employees.html', {'z': z, 'vars': vars, 'msg_success': msg_success})
#         return render(request, 'accounts_salary_employees.html', {'z': z, 'vars': vars})
#     else:
#         return redirect('/')


# def accounts_salaried_employees(request):
#     if 'usernameacnt2' in request.session:
#         if request.session.has_key('usernameacnt2'):
#             usernameacnt2 = request.session['usernameacnt2']
#         z = user_registration.objects.filter(id=usernameacnt2)
#         vars = user_registration.objects.filter(
#             confirm_salary_status=1).order_by("-id")
#         return render(request, 'accounts_salaried_employees.html', {'z': z, 'vars': vars})
#     else:
#         return redirect('/')


# def accounts_monthdays_cards(request):
#     if 'usernameacnt2' in request.session:
#         if request.session.has_key('usernameacnt2'):
#             usernameacnt2 = request.session['usernameacnt2']
#         z = user_registration.objects.filter(id=usernameacnt2)
#         return render(request, 'accounts_monthdays_cards.html', {'z': z})
#     else:
#         return redirect('/')


# def accounts_month_adddays_form(request):
#     if 'usernameacnt2' in request.session:
#         if request.session.has_key('usernameacnt2'):
#             usernameacnt2 = request.session['usernameacnt2']
#         z = user_registration.objects.filter(id=usernameacnt2)
#         mem = acnt_monthdays()
#         if request.method == 'POST':
#             mem.month_fromdate = request.POST['fromdate']
#             mem.month_todate = request.POST['todate']
#             mem.month_workingdays = request.POST['workingdays']
#             mem.month_holidays = request.POST['holidays']
#             mem.save()
#             msg_success = 'submitted succesfully'
#             return render(request, 'accounts_month_adddays_form.html', {'z': z, 'msg_success': msg_success})

#         return render(request, 'accounts_month_adddays_form.html', {'z': z})
#     else:
#         return redirect('/')


# def accounts_month_viewdays(request):
#     if 'usernameacnt2' in request.session:
#         if request.session.has_key('usernameacnt2'):
#             usernameacnt2 = request.session['usernameacnt2']
#         z = user_registration.objects.filter(id=usernameacnt2)
#         mem = acnt_monthdays.objects.all()

#         return render(request, 'accounts_month_viewdays.html', {'z': z, 'mem': mem})
#     else:
#         return redirect('/')

def accounts_traineepayment_notverified(request):
    if 'usernameacnt2' in request.session:
        if request.session.has_key('usernameacnt2'):
            usernameacnt2 = request.session['usernameacnt2']
        z = user_registration.objects.filter(id=usernameacnt2)
        des = designation.objects.get(designation='trainee')
        deta = user_registration.objects.filter(designation=des.id)
        return render(request, 'accounts_traineepayment_notverified.html', {'z': z, 'deta': deta})
    else:
        return redirect('/')


def verified(request, id):
    rem = user_registration.objects.get(id=id)
    rem.payment_status = 2
    rem.save()
    return redirect('/accounts_traineepayment_notverified')


def accounts_traineepayment_pending(request):
    if 'usernameacnt2' in request.session:
        if request.session.has_key('usernameacnt2'):
            usernameacnt2 = request.session['usernameacnt2']
        z = user_registration.objects.filter(id=usernameacnt2)
        des = designation.objects.get(designation='trainee')
        deta = user_registration.objects.filter(designation=des.id)

        return render(request, 'accounts_traineepayment_pending.html', {'z': z, 'deta': deta})
    else:
        return redirect('/')


def accounts_newtrainees(request):
    if 'usernameacnt2' in request.session:
        if request.session.has_key('usernameacnt2'):
            usernameacnt2 = request.session['usernameacnt2']
        z = user_registration.objects.filter(id=usernameacnt2)
        des = designation.objects.get(designation='trainee')
        deta = user_registration.objects.filter(designation=des.id)
        return render(request, 'accounts_newtrainees.html', {'z': z, 'deta': deta})
    else:
        return redirect('/')


def accounts_salary_employees(request):
    if 'usernameacnt2' in request.session:
        if request.session.has_key('usernameacnt2'):
            usernameacnt2 = request.session['usernameacnt2']
        z = user_registration.objects.filter(id=usernameacnt2)
        des2 = designation.objects.get(designation='trainee')
        Adm1 = designation.objects.get(designation="Admin")
        vars = user_registration.objects.exclude(
            designation=des2.id).exclude(designation=Adm1.id).order_by("-id")
        return render(request, 'accounts_salary_employees.html', {'z': z, 'vars': vars})
    else:
        return redirect('/')


def accounts_salaryconfirm(request, id):
    if 'usernameacnt2' in request.session:
        if request.session.has_key('usernameacnt2'):
            usernameacnt2 = request.session['usernameacnt2']
        z = user_registration.objects.filter(id=usernameacnt2)

        des2 = designation.objects.get(designation='trainee')
        Adm1 = designation.objects.get(designation="Admin")
        vars = user_registration.objects.exclude(
            designation=des2.id).exclude(designation=Adm1.id).order_by("-id")
        if request.method == 'POST':
            var = user_registration.objects.get(id=id)
            var.confirm_salary = request.POST['salary']
            var.confirm_salary_status = 1
            var.save()
            msg_success = "submitted successfully"
            return render(request, 'accounts_salary_employees.html', {'z': z, 'vars': vars, 'msg_success': msg_success})
        return render(request, 'accounts_salary_employees.html', {'z': z, 'vars': vars})
    else:
        return redirect('/')


def accounts_salaried_employees(request):
    if 'usernameacnt2' in request.session:
        if request.session.has_key('usernameacnt2'):
            usernameacnt2 = request.session['usernameacnt2']
        z = user_registration.objects.filter(id=usernameacnt2)
        vars = user_registration.objects.filter(
            confirm_salary_status=1).order_by("-id")
        return render(request, 'accounts_salaried_employees.html', {'z': z, 'vars': vars})
    else:
        return redirect('/')

def accounts_monthdays_cards(request):
    if 'usernameacnt2' in request.session:
        if request.session.has_key('usernameacnt2'):
            usernameacnt2 = request.session['usernameacnt2']
        z = user_registration.objects.filter(id=usernameacnt2)
        mem = acnt_monthdays.objects.all().count()
        return render(request, 'accounts_monthdays_cards.html', {'mem':mem,'z': z})
    else:
        return redirect('/')


def accounts_month_adddays_form(request):
    if 'usernameacnt2' in request.session:
        if request.session.has_key('usernameacnt2'):
            usernameacnt2 = request.session['usernameacnt2']
        z = user_registration.objects.filter(id=usernameacnt2)
        mem = acnt_monthdays()
        if request.method == 'POST':
            mem.month_fromdate = request.POST['fromdate']
            mem.month_todate = request.POST['todate']
            mem.month_workingdays = request.POST['workingdays']
            mem.month_holidays = request.POST['holidays']
            mem.save()
            msg_success = 'submitted succesfully'
            return render(request, 'accounts_month_adddays_form.html', {'z': z, 'msg_success': msg_success})

        return render(request, 'accounts_month_adddays_form.html', {'z': z})
    else:
        return redirect('/')


def accounts_month_viewdays(request):
    if 'usernameacnt2' in request.session:
        if request.session.has_key('usernameacnt2'):
            usernameacnt2 = request.session['usernameacnt2']
        z = user_registration.objects.filter(id=usernameacnt2)
        mem = acnt_monthdays.objects.all()

        return render(request, 'accounts_month_viewdays.html', {'z': z, 'mem': mem})
    else:
        return redirect('/')

def SuperAdmin_leavehistory(request):
    if 'SAdm_id' in request.session:
        if request.session.has_key('SAdm_id'):
            SAdm_id = request.session['SAdm_id']
        users = User.objects.filter(id=SAdm_id)
        usr = user_registration.objects.all()
        des = designation.objects.get(designation="trainee")
        le = leave.objects.filter(leaveapprovedstatus=0).exclude(
            designation_id=des.id).order_by('-id')
        return render(request, 'SuperAdmin_leavehistory.html', {'users': users, 'le': le})
    else:
        return redirect('/')


def SuperAdmin_leaveapprovedstatus(request, id):
    if 'SAdm_id' in request.session:
        if request.session.has_key('SAdm_id'):
            SAdm_id = request.session['SAdm_id']
        users = User.objects.filter(id=SAdm_id)
        usr = user_registration.objects.all()

        le = leave.objects.get(id=id)
        le.leaveapprovedstatus = 1
        le.save()
        msg_success = "Leave Approved Successfully"
        return render(request, 'SuperAdmin_leavehistory.html', {'users': users, 'msg_success': msg_success})
    else:
        return redirect('/')


def SuperAdmin_rejectedstatus(request, id):
    if 'SAdm_id' in request.session:
        if request.session.has_key('SAdm_id'):
            SAdm_id = request.session['SAdm_id']
        users = User.objects.filter(id=SAdm_id)
        usr = user_registration.objects.all()

        le = leave.objects.get(id=id)
        le.leaveapprovedstatus = 2
        le.leave_rejected_reason = request.POST['review']
        le.save()
        msg_warning = "Leave Rejected Successfully"
        return render(request, 'SuperAdmin_leavehistory.html', {'users': users, 'msg_warning': msg_warning})
    else:
        return redirect('/')


def projectMAN_leavehistory(request):
    if 'prid' in request.session:
        if request.session.has_key('prid'):
            prid = request.session['prid']
        pro = user_registration.objects.filter(id=prid)
        des = designation.objects.get(designation="team leader")
        des1 = designation.objects.get(designation="developer")

        dev = user_registration.objects.filter(projectmanager_id=prid)
        ids = dev.values_list('id', flat="true")
        le = leave.objects.filter(user_id__in=ids.all()).filter(Q(designation_id=des.id) | Q(
            designation_id=des1.id)).filter(leaveapprovedstatus=0).order_by('-id')
        return render(request, 'projectMAN_leavehistory.html', {'pro': pro, 'le': le})
    else:
        return redirect('/')


def projectMAN_leaveapprovedstatus(request, id):
    if 'prid' in request.session:
        if request.session.has_key('prid'):
            prid = request.session['prid']
        pro = user_registration.objects.filter(id=prid)

        le = leave.objects.get(id=id)
        le.leaveapprovedstatus = 1
        le.save()
        msg_success = "Leave aprroved Successfully"
        return render(request, 'projectMAN_leavehistory.html', {'pro': pro, 'msg_success': msg_success})
    else:
        return redirect('/')


def projectMAN_rejectedstatus(request, id):
    if 'prid' in request.session:
        if request.session.has_key('prid'):
            prid = request.session['prid']
        pro = user_registration.objects.filter(id=prid)

        le = leave.objects.get(id=id)
        le.leaveapprovedstatus = 2
        le.leave_rejected_reason = request.POST['review']
        le.save()
        msg_warning = "Leave Rejected Successfully"
        return render(request, 'projectMAN_leavehistory.html', {'pro': pro, 'msg_warning': msg_warning})
    else:
        return redirect('/')


def TL_leavehistory(request):
    if 'tlid' in request.session:
        if request.session.has_key('tlid'):
            tlid = request.session['tlid']
        if request.session.has_key('tlteam'):
            tlteam = request.session['tlteam']

        else:
            variable = "dummy"

        mem = user_registration.objects.filter(id=tlid)

        dev = user_registration.objects.filter(tl_id=tlid)
        ids = dev.values_list('id', flat="true")

        des = designation.objects.get(designation="developer")
        le = leave.objects.filter(user_id__in=ids.all(
        ), designation_id=des.id, leaveapprovedstatus=0).order_by('-id')
        return render(request, 'TL_leavehistory.html', {'mem': mem, 'le': le})
    else:
        return redirect('/')


def TL_leaveapprovedstatus(request, id):
    if 'tlid' in request.session:
        if request.session.has_key('tlid'):
            tlid = request.session['tlid']
        else:
            variable = "dummy"
        mem = user_registration.objects.filter(id=tlid)

        le = leave.objects.get(id=id)
        le.leaveapprovedstatus = 1
        le.save()
        msg_success = "Leave aprroved Successfully"
        return render(request, 'TL_leavehistory.html', {'mem': mem, 'msg_success': msg_success})
    else:
        return redirect('/')


def TL_rejectedstatus(request, id):
    if 'tlid' in request.session:
        if request.session.has_key('tlid'):
            tlid = request.session['tlid']
        else:
            variable = "dummy"
        mem = user_registration.objects.filter(id=tlid)

        le = leave.objects.get(id=id)
        le.leaveapprovedstatus = 2
        le.leave_rejected_reason = request.POST['review']
        le.save()
        msg_warning = "Leave Rejected Successfully"
        return render(request, 'TL_leavehistory.html', {'mem': mem, 'msg_warning': msg_warning})
    else:
        return redirect('/')


def trainer_leavehistory(request):
    if 'usernametrnr2' in request.session:

        if request.session.has_key('usernametrnr2'):
            usernametrnr2 = request.session['usernametrnr2']
        if request.session.has_key('usernametrnr3'):
            usernametrnr3 = request.session['usernametrnr3']

        mem = user_registration.objects.filter(id=usernametrnr2)
        tr = user_registration.objects.filter(team_id=usernametrnr3)
        ids = tr.values_list('id', flat="true")
        print('haiiii')
        print(usernametrnr3)
        des = designation.objects.get(designation='trainee')
        le = leave.objects.filter(
            designation_id=des.id, leaveapprovedstatus=0).all().order_by('-id')
        return render(request, 'trainer_leavehistory.html', {'le': le, 'mem': mem})

    else:
        return redirect('/')


def trainer_leaveapprovedstatus(request, id):
    if 'usernametrnr2' in request.session:

        if request.session.has_key('usernametrnr2'):
            usernametrnr2 = request.session['usernametrnr2']
        if request.session.has_key('usernametrnr3'):
            usernametrnr3 = request.session['usernametrnr3']

        mem = user_registration.objects.filter(id=usernametrnr2)

        le = leave.objects.get(id=id)
        le.leaveapprovedstatus = 1
        le.save()
        msg_success = "Leave Approved successfully"
        return render(request, 'trainer_leavehistory.html', {'mem': mem, 'msg_success': msg_success})
    else:
        return redirect('/')


def trainer_rejectedstatus(request, id):
    if 'usernametrnr2' in request.session:

        if request.session.has_key('usernametrnr2'):
            usernametrnr2 = request.session['usernametrnr2']
        if request.session.has_key('usernametrnr3'):
            usernametrnr3 = request.session['usernametrnr3']

        mem = user_registration.objects.filter(id=usernametrnr2)

        le = leave.objects.get(id=id)
        le.leaveapprovedstatus = 2
        le.leave_rejected_reason = request.POST['review']
        le.save()
        msg_warning = "Leave Rejected Successfully"
        return render(request, 'trainer_leavehistory.html', {'mem': mem, 'msg_warning': msg_warning})
    else:
        return redirect('/')


def tm_leavehistory(request):
    if 'usernametm2' in request.session:
        if request.session.has_key('usernametm'):
            usernametm = request.session['usernametm']
        if request.session.has_key('usernametm1'):
            usernametm1 = request.session['usernametm1']
        if request.session.has_key('usernametm2'):
            usernametm2 = request.session['usernametm2']
        else:
            usernametm1 = "dummy"
        mem = user_registration.objects.filter(id=usernametm2)
        des = designation.objects.get(designation="trainer")
        des1 = designation.objects.get(designation="trainee")
        le = leave.objects.filter(Q(designation_id=des.id) | Q(
            designation_id=des1.id)).filter(leaveapprovedstatus=0).order_by('-id')

        return render(request, 'tm_leavehistory.html', {'mem': mem, 'le': le})
    else:
        return redirect('/')


def tm_leaveapprovedstatus(request, id):
    if 'usernametm2' in request.session:
        if request.session.has_key('usernametm'):
            usernametm = request.session['usernametm']
        if request.session.has_key('usernametm1'):
            usernametm1 = request.session['usernametm1']
        if request.session.has_key('usernametm2'):
            usernametm2 = request.session['usernametm2']
        else:
            usernametm1 = "dummy"
        mem = user_registration.objects.filter(id=usernametm2)

        le = leave.objects.get(id=id)
        le.leaveapprovedstatus = 1
        le.save()
        msg_success = "Leave Approved successfully"
        return render(request, 'tm_leavehistory.html', {'mem': mem, 'msg_success': msg_success})

    else:
        return redirect('/')


def tm_rejectedstatus(request, id):
    if 'usernametm2' in request.session:
        if request.session.has_key('usernametm'):
            usernametm = request.session['usernametm']
        if request.session.has_key('usernametm1'):
            usernametm1 = request.session['usernametm1']
        if request.session.has_key('usernametm2'):
            usernametm2 = request.session['usernametm2']
        else:
            usernametm1 = "dummy"
        mem = user_registration.objects.filter(id=usernametm2)

        le = leave.objects.get(id=id)
        le.leaveapprovedstatus = 2
        le.leave_rejected_reason = request.POST['review']
        le.save()
        msg_warning = "Leave Rejected Successfully"
        return render(request, 'tm_leavehistory.html', {'mem': mem, 'msg_warning': msg_warning})
    else:
        return redirect('/')


def BRadmin_leavehistory(request):
    if 'Adm_id' in request.session:

        if request.session.has_key('Adm_id'):
            Adm_id = request.session['Adm_id']

        Adm = user_registration.objects.filter(id=Adm_id)
        des = designation.objects.get(designation="trainee")
        le = leave.objects.filter(leaveapprovedstatus=0).exclude(
            designation_id=des.id).order_by('-id')
        return render(request, 'BRadmin_leavehistory.html', {'Adm': Adm, 'le': le})
    else:
        return redirect('/')


def BRadmin_leaveapprovedstatus(request, id):
    if 'Adm_id' in request.session:

        if request.session.has_key('Adm_id'):
            Adm_id = request.session['Adm_id']

        Adm = user_registration.objects.filter(id=Adm_id)

        le = leave.objects.get(id=id)
        le.leaveapprovedstatus = 1
        le.save()
        msg_success = "Leave aprroved Successfully"
        return render(request, 'BRadmin_leavehistory.html', {'Adm': Adm, 'msg_success': msg_success})
    else:
        return redirect('/')


def BRadmin_rejectedstatus(request, id):
    if 'Adm_id' in request.session:

        if request.session.has_key('Adm_id'):
            Adm_id = request.session['Adm_id']

        Adm = user_registration.objects.filter(id=Adm_id)

        le = leave.objects.get(id=id)
        le.leaveapprovedstatus = 2
        le.leave_rejected_reason = request.POST['review']
        le.save()
        msg_warning = "Leave Rejected Successfully"
        return render(request, 'BRadmin_leavehistory.html', {'Adm': Adm, 'msg_warning': msg_warning})
    else:
        return redirect('/')

def accounts_account_salary(request):
    if 'usernameacnt2' in request.session:
        if request.session.has_key('usernameacnt2'):
            usernameacnt2 = request.session['usernameacnt2']
        z = user_registration.objects.filter(id=usernameacnt2)          
        mem1 = user_registration.objects.get(id=usernameacnt2)
        var = acntspayslip.objects.filter(user_id=usernameacnt2)
        return render(request, 'accounts_account_salary.html', {'z': z,'mem1': mem1, 'var': var })
    else:
        return redirect('/')



def accounts_accout_salary_slip(request, id):
    date = datetime.now()
    user = user_registration.objects.get(id=id)
    acc = acntspayslip.objects.get(user_id=id)
    print(acc)
    year = date.today().year
    month = date.today().month

    leave = acnt_monthdays.objects.get(month_fromdate__year__gte=year, month_fromdate__month__gte=month,
                                       month_todate__year__lte=year, month_todate__month__lte=month)
    mm = leave.month_workingdays
    print(mm)
    abc = int(user.confirm_salary)
    print(abc)
    c = abc/mm
    v = acc.leavesno
    mem = mm-v
    print(v)
    conf = abc-c
    template_path = 'accounts_accout_salary_slip.html'
    context = {'acc': acc, 'user': user, 'c': c, 'mm': mm, 'mem': mem, 'conf': conf, 'media_url': settings.MEDIA_URL, 'date': date,
               }
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename="Payslip.pdf"'
    template = get_template(template_path)
    html = template.render(context)
    pisa_status = pisa.CreatePDF(html, dest=response)
    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response


def accounts_salary_pending(request):
    if 'usernameacnt2' in request.session:
        if request.session.has_key('usernameacnt2'):
            usernameacnt2 = request.session['usernameacnt2']
        z = user_registration.objects.filter(id=usernameacnt2)
        year = date.today().year
        month = date.today().month
        vars = acntspayslip.objects.filter(~Q(fromdate__year=year,
                                          fromdate__month=month))

        return render(request, 'accounts_salary_pending.html', {'z': z, 'vars': vars})
    else:
        return redirect('/')


def salarysubmit(request, id):
    if request.method == 'POST':
        m = user_registration.objects.get(id=id)
        m.salary_status = 1
        m.save()
        return redirect('/accounts_salary_pending')
    return redirect('/accounts_salary_pending')


def accounts_salary_given(request):
    if 'usernameacnt2' in request.session:
        if request.session.has_key('usernameacnt2'):
            usernameacnt2 = request.session['usernameacnt2']
        z = user_registration.objects.filter(id=usernameacnt2)
        year = date.today().year
        month = date.today().month

        vars = acntspayslip.objects.filter(fromdate__year=year,
                                          fromdate__month=month)
        
        return render(request, 'accounts_salary_given.html', {'z': z, 'vars': vars})
    else:
        return redirect('/')


def accounts_promissory(request, id):
    if 'usernameacnt2' in request.session:
        if request.session.has_key('usernameacnt2'):
            usernameacnt2 = request.session['usernameacnt2']
        z = user_registration.objects.filter(id=usernameacnt2)
        user = user_registration.objects.get(id=id)

    return render(request, 'accounts_promissory.html', {'z': z, 'user': user})

def accounts_download_promissory(request, id):
    if 'usernameacnt2' in request.session:
        if request.session.has_key('usernameacnt2'):
            usernameacnt2 = request.session['usernameacnt2']
        z = user_registration.objects.filter(id=usernameacnt2)
        user = user_registration.objects.get(id=id)
        
        
        try:
           c = Promissory.objects.filter(user_id=id).latest('id')
        except Promissory.DoesNotExist:
           c = None
           msg_success="No Data in Database Pleace Add Promissory"
           return render(request, 'accounts_promissory.html', {'z': z,'msg_success':msg_success})
        print(c)
    return render(request, 'accounts_download_promissory.html', {'z': z, 'user': user, 'c': c})

def accounts_promissory_complete_pfd(request, id):
    date = datetime.now()
    mem = Promissory.objects.filter(user_id=id).latest('id')
    template_path = 'accounts_promissory_complete_pfd.html'
    context = {'mem': mem,
               'media_url': settings.MEDIA_URL,
               'date': date
               }
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    # response['Content-Disposition'] = 'attachment; filename="certificate.pdf"'
    response['Content-Disposition'] = 'filename="PROMISSORY.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
        html, dest=response)

    # if error then show some funy view
    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response
    # return render(request,'accounts_promissory_complete_pfd.html')


def accounts_promissory_notcomplete_pfd(request, id):
    date = datetime.now()
    mem = Promissory.objects.filter(user_id=id).latest('id')
    a = num2words(mem.user_id.total_pay)
    b = (u'u20B9')

    template_path = 'accounts_promissory_notcomplete_pfd.html'
    context = {'mem': mem, 'a': a, 'b': b,
               'media_url': settings.MEDIA_URL,
               'date': date
               }
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    # response['Content-Disposition'] = 'attachment; filename="certificate.pdf"'
    response['Content-Disposition'] = 'filename="PROMISSORY.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
        html, dest=response)

    # if error then show some funy view
    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response


def accounts_promissory_add(request, id):
    if 'usernameacnt2' in request.session:
        if request.session.has_key('usernameacnt2'):
            usernameacnt2 = request.session['usernameacnt2']
        z = user_registration.objects.filter(id=usernameacnt2)
    mem = user_registration.objects.get(id=id)

    print(mem)
    if request.method == "POST":

        user = Promissory()
        user.user_id = user_registration.objects.get(id=id)
        user.inital_amount = request.POST['in_amt']
        user.inital_paid_on = request.POST['in_paid_on']
        user.inital_paid_amount = request.POST['in_paid_amt']
        user.inital_paid_date = request.POST['in_paid_date']
        user.inital_balance_amount = request.POST['in_bal_amt']
        user.inital_due_date = request.POST['in_due_date']
        user.inital_total_payment = request.POST['in_tot_pay']

        user.second_amount = request.POST['sec_amt']
        user.second_due_on = request.POST['sec_paid_on']
        user.second_paid_amount = request.POST['sec_paid_amt']
        user.second_paid_date = request.POST['sec_paid_date']
        user.second_balance_amount = request.POST['sec_bal_amt']
        user.second_due_date = request.POST['sec_due_date']
        user.second_total_payment = request.POST['sec_tot_pay']

        user.final_amount = request.POST['fnl_amt']
        user.final_due_on = request.POST['fnl_paid_on']
        user.final_paid_amount = request.POST['fnl_paid_amt']
        user.final_paid_date = request.POST['fnl_paid_date']
        user.final_balance_amount = request.POST['fnl_bal_amt']
        user.final_due_date = request.POST['fnl_due_date']
        user.final_total_payment = request.POST['fnl_tot_pay']
        user.save()
        msg_success = "Add Successfully"
        return render(request, 'accounts_promissory_add.html', {'z': z, 'msg_success': msg_success})

    return render(request, 'accounts_promissory_add.html', {'z': z})


def test(request, id):
    if 'usernameacnt2' in request.session:
        if request.session.has_key('usernameacnt2'):
            usernameacnt2 = request.session['usernameacnt2']
        z = user_registration.objects.filter(id=usernameacnt2)
    user = user_registration.objects.get(id=id)
    c = Promissory.objects.filter(user_id=id).latest('id')

    user = Promissory.objects.filter(user_id=id).latest('id')
    user.complete_status = 1
    user.save()
    msg_success = "Status Change To Completed"

    return render(request, 'accounts_download_promissory.html', {'z': z, 'user': user, 'c': c, 'msg_success': msg_success, })


def accounts_workstatus(request):
    if 'usernameacnt2' in request.session:
        if request.session.has_key('usernameacnt2'):
            usernameacnt2 = request.session['usernameacnt2']
        z = user_registration.objects.filter(id=usernameacnt2)
        cous = course.objects.all()
        dep = department.objects.all()
        des = designation.objects.all()
        emp = user_registration.objects.all()

        return render(request,'accounts_workstatus.html',{'z':z, 'cous':cous,'dep':dep,'des':des,'emp':emp,})
    else:
        return redirect('/')

@csrf_exempt
def accounts_designation(request):
    if 'usernameacnt2' in request.session:
        if request.session.has_key('usernameacnt2'):
            usernameacnt2 = request.session['usernameacnt2']
        z = user_registration.objects.filter(id=usernameacnt2)

        dept_id = request.GET.get('dept_id')
        Desig = designation.objects.filter(department = dept_id).exclude(designation = 'HR manager').exclude(designation = 'HR').exclude(designation = 'admin').exclude(designation ='manager').exclude(designation ='trainee').exclude(designation ='project manager').exclude(designation ='tester').exclude(designation ='trainingmanager').exclude(designation ='account').exclude(designation ='trainer')
       
        return render(request,'accounts_designation.html',{'z':z,'Desig': Desig, })
    else:
        return redirect('/')

@csrf_exempt
def accounts_emp_ajax(request):
    if 'usernameacnt2' in request.session:
        if request.session.has_key('usernameacnt2'):
            usernameacnt2 = request.session['usernameacnt2']
        z = user_registration.objects.filter(id=usernameacnt2)
        dept_id = request.GET.get('dept_id')
        courseId = request.GET.get('courseId')
        desigId = request.GET.get('desigId')
        Desig = user_registration.objects.filter(department_id=dept_id, designation_id=desigId)

        return render(request,'accounts_emp_ajax.html',{'z':z,'Desig': Desig,})
    else:
        return redirect('/')

@csrf_exempt
def accounts_project_details(request):
    if 'usernameacnt2' in request.session:
        emp = request.POST['emp']
        fdate = request.POST['fdate']
        tdate = request.POST['tdate']
        names = project_taskassign.objects.filter(developer=emp,startdate__gte=fdate, enddate__lte=tdate) 

        year = date.today().year
        month = date.today().month

        leave = project_taskassign.objects.filter(developer=emp,startdate__year__gte=year,
                                          startdate__month__gte=month,
                                          submitted_date__year__lte=year,
                                          submitted_date__month__lte=month)
        mm = leave.values_list('delay', flat='true')
        a=0
        for i in mm:
            
            a=a+int(i)
        
        return render(request,'accounts_project_details.html', {'names':names,'mm':mm,'a':a ,})
    else:
        return redirect('/')


def accounts_add_bank_acnt_update(request,id):
    if 'usernameacnt2' in request.session:
        if request.session.has_key('usernameacnt2'):
            usernameacnt2 = request.session['usernameacnt2']
        z = user_registration.objects.filter(id=usernameacnt2)
        mem1=user_registration.objects.filter(id=id)
        if request.method == 'POST':
            vars = user_registration.objects.get(id=id)
            vars.account_no = request.POST['account_no']
            vars.ifsc = request.POST['ifsc']
            vars.bank_branch = request.POST['bank_branch']
            vars.bank_name= request.POST['bank_name']
            vars.save()
            msg_success = "Updated"
            return render(request,'accounts_add_bank_acnt_update.html',{'mem1':mem1,'z': z,'msg_success':msg_success})
        return render(request,'accounts_add_bank_acnt_update.html',{'mem1':mem1,'z': z})
    else:
        
        return render(request,'accounts_add_bank_acnt_update.html',{'mem1':mem1,'z': z})

def DEVpayments(request):
    if request.session.has_key('devid'):
        devid = request.session['devid']
    else:
        variable = "dummy"
    dev = user_registration.objects.filter(id=devid)
    mem1 = user_registration.objects.get(id=devid)
    var = acntspayslip.objects.filter(user_id =devid)
    return render(request, 'DEVpayments.html', {'dev': dev, 'var': var,'mem1':mem1})
    
    
def TLpayment(request):
   if 'tlid' in request.session:
        if request.session.has_key('tlid'):
            tlid = request.session['tlid']
        else:
            variable="dummy"
        mem = user_registration.objects.filter(id=tlid)
        mem1 = user_registration.objects.get(id=tlid)
        var = acntspayslip.objects.filter(user_id =tlid)
        return render(request, 'TLpayment.html', {'mem': mem, 'var': var,'mem1':mem1})
   else:
        return redirect('/')

def projectmanager_payment_list(request):
    if 'prid' in request.session:
        if request.session.has_key('prid'):
            prid = request.session['prid']
        else:
            variable = "dummy"
        pro = user_registration.objects.filter(id=prid)
        var = acntspayslip.objects.filter(user_id = prid)
        b = user_registration.objects.get(id=prid)
        return render(request, 'projectmanager_payment_list.html', {'pro': pro, 'var': var, 'b':b })
    else:
        return redirect('/')

############### training manager ###################################

def trainingmanager_payment_list(request):
    if 'usernametm2' in request.session:
        
        if request.session.has_key('usernametm2'):
            usernametm2 = request.session['usernametm2']
       
        mem = user_registration.objects.filter(id=usernametm2)
        var = acntspayslip.objects.filter(user_id = usernametm2)
        return render(request, 'trainingmanager_payment_list.html', {'mem': mem, 'var': var })
    else:
        return redirect('/')

########################### pdf #########################

def paypdf(request,id,tid):
    date = datetime.now()  
    user = user_registration.objects.get(id=tid)
    acc = acntspayslip.objects.get(id=id)
    print(acc)
    
    year = acc.fromdate.year
    month = acc.fromdate.month

    leave = acnt_monthdays.objects.get(month_fromdate__year__gte=year,month_fromdate__month__gte=month,month_todate__year__lte=year,month_todate__month__lte=month)
    mm = leave.month_workingdays
    mem = leave.month_holidays
    v = acc.leavesno
    mam = mm-v
    print(mm)
    abc = int(user.confirm_salary)
    print(abc)
    c = math.ceil(abc/mam)
    print(v)
    
    add = acc.basic_salary+ int(acc.conveyns)+acc.hra+acc.pf_tax+acc.pf+int(acc.esi)+acc.delay+acc.leavesno+acc.incentives
    conf = add-c
    words = num2words(conf)
    template_path = 'paypdf.html'
    context = {'acc':acc, 'user':user,'c':c,'mm':mm,'mam':mam,'conf':conf,'words':words, 'add':add,
    'media_url':settings.MEDIA_URL,
    'date':date,
    }
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename="Payslip.pdf"'
    template = get_template(template_path)
    html = template.render(context)
    pisa_status = pisa.CreatePDF(
       html, dest=response)
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response


########################### manager ######################


def MAN_payment_list(request):
    if 'm_id' in request.session:
        if request.session.has_key('m_id'):
            m_id = request.session['m_id']
        else:
            variable="dummy"
        mem = user_registration.objects.filter(id=m_id)
        var = acntspayslip.objects.filter(user_id = m_id)
        return render(request, 'MAN_payment_list.html', {'mem': mem, 'var': var })
    else:
        return redirect('/')


############################### trainer #############################

def trainer_payment_list(request):
    if 'usernametrnr2' in request.session:
        
        if request.session.has_key('usernametrnr2'):
            usernametrnr2 = request.session['usernametrnr2']
    
        
        z = user_registration.objects.filter(id=usernametrnr2)
    
        var = acntspayslip.objects.filter(user_id = usernametrnr2)
        return render(request, 'trainer_payment_list.html', {'z': z, 'var': var })
    else:
        return redirect('/')

def TSpayment(request):
    if 'usernametsid' in request.session:
        if request.session.has_key('usernamets'):
            usernamets = request.session['usernamets']
        if request.session.has_key('usernametsid'):
            usernametsid = request.session['usernametsid']
        else:
            usernamets1 = "dummy"
        mem=user_registration.objects.filter(designation_id=usernamets).filter(id=usernametsid)
        mem1 = user_registration.objects.get(id=usernametsid)
        var = acntspayslip.objects.filter(user_id = usernametsid)
        return render(request, 'TSpayment.html', {'mem': mem,'mem1': mem1, 'var': var })
    else:
        return redirect('/')
        
        
        
def project_reset(request,id):
    if 'prid' in request.session:
        if request.session.has_key('prid'):
            prid = request.session['prid']
        else:
            return redirect('/')
        pro = user_registration.objects.filter(id=prid)
        x = project_taskassign.objects.get(id = id)
        x.submitted_date ="0101-01-01"
        x.employee_files =""
        x.projectstatus = "in progress"
        x.status=''
        x.delay=0
        x.progress=50
        x.save()
        
        msg_success="success"
        return render(request, 'projectmanager_projectstatus.html', {'pro': pro,'msg_success':msg_success})
    else:
        return redirect('/')
        

def projectmanager_trainee_status(request):
    if 'prid' in request.session:
        if request.session.has_key('prid'):
            prid = request.session['prid']
        else:
            return redirect('/')
        pro = user_registration.objects.filter(id=prid)
        
        des = designation.objects.get(designation="trainee")
        des1 = designation.objects.get(designation="team leader")
        var=user_registration.objects.filter(designation_id=des.id)
        var1=user_registration.objects.filter(designation_id=des1.id)
        return render(request, 'projectmanager_trainee_status.html', {'pro': pro,'var':var,'var1':var1})
    else:
        return redirect('/')
        
@csrf_exempt
def projectmanager_trainee_details(request):
    if 'prid' in request.session:
        if request.session.has_key('prid'):
            prid = request.session['prid']
        else:
            return redirect('/')
        pro = user_registration.objects.filter(id=prid)
        emp = request.POST['emp']
        names = trainer_task.objects.filter(user_id=emp).order_by('-id')                                          
        mm = names.values_list('delay', flat='true')
        a=0
        for i in mm:
            
            a=a+int(i)
        return render(request, 'projectmanager_trainee_details.html', {'pro': pro,'names':names,'a':a})
    else:
        return redirect('/')

# ------------------------------- HR   ------------------------------- #

def HR_Dashboard(request):
    if 'hr_id' in request.session:
        if request.session.has_key('hr_id'):
            hr_id = request.session['hr_id']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(id=hr_id)
        return render(request, 'hr_module/HR_Dashboard.html', {'mem': mem})
    else:
        return redirect('/')

def HR_leave(request):
    if 'hr_id' in request.session:
        if request.session.has_key('hr_id'):
            hr_id = request.session['hr_id']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(id=hr_id)
        return render(request, 'hr_module/HR_leave.html', {'mem': mem})
    else:
        return redirect('/')

def HR_leaveapply(request):
    if 'hr_id' in request.session:
        if request.session.has_key('hr_des_id'):
            hr_des_id = request.session['hr_des_id']
        if request.session.has_key('hr_id'):
            hr_id = request.session['hr_id']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(designation_id=hr_des_id).filter(id=hr_id)
        
        if request.method == 'POST':
            apply_leave = leave()
            apply_leave.from_date = request.POST['from']
            apply_leave.to_date = request.POST['to']
            apply_leave.leave_status = request.POST['haful']
            apply_leave.reason = request.POST['reason']
            apply_leave.user =user_registration.objects.get(id=hr_id)
            apply_leave.designation_id =hr_des_id
            apply_leave.leaveapprovedstatus = 0

            start = datetime.strptime(apply_leave.from_date, '%Y-%m-%d').date() 
            end = datetime.strptime(apply_leave.to_date, '%Y-%m-%d').date()

            diff = (end  - start).days
            
            cnt =  Event.objects.filter(start_time__range=(start,end)).count()
            
            if diff == 0:
                apply_leave.days = 1
            else:
                apply_leave.days = diff - cnt
                apply_leave.save()
            msg_success = "leave applied"
            return render(request, 'hr_module/HR_leaveapply.html',{"msg_success":msg_success})
        else:
            pass
        return render(request, 'hr_module/HR_leaveapply.html',{'mem':mem})
    else:
        return redirect('/')

def HR_appliedleave(request):
    if 'hr_id' in request.session:
        if request.session.has_key('hr_id'):
            hr_id= request.session['hr_id']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(id=hr_id)
        hr_leave = leave.objects.filter(user=hr_id).order_by('-id')
        return render(request, 'hr_module/HR_appliedleave.html', {'mem': mem,'hr':hr_leave})
    else:
        return redirect('/')

def HR_issue(request):
    if 'hr_id' in request.session:
        if request.session.has_key('hr_id'):
            hr_id = request.session['hr_id']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(id=hr_id)
        return render(request, 'hr_module/HR_issue.html', {'mem': mem})
    else:
        return redirect('/')

def HR_reportissue(request):
    if 'hr_id' in request.session:
        if request.session.has_key('hr_des_id'):
            hr_des_id = request.session['hr_des_id']
        if request.session.has_key('hr_id'):
            hr_id = request.session['hr_id']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(designation_id=hr_des_id).filter(id=hr_id)
        issue = reported_issue()
        des = designation.objects.get(designation='admin')
        if request.method == "POST":
            issue.issue = request.POST['issues']
            issue.reported_date = datetime.now()
            issue.reported_to = user_registration.objects.get(designation_id=des.id)
            issue.reporter = user_registration.objects.get(id=hr_id)
            issue.designation_id = hr_des_id
            issue.issuestatus = 0
            issue.save()
            msg_success = "Issue Reported"
            return render(request, 'hr_module/HR_reportissue.html',{'mem':mem,'msg_success':msg_success})
        else:
            pass
        return render(request, 'hr_module/HR_reportissue.html',{'mem':mem})
    else:
        return redirect('/')

def HR_reportedissue(request):
    if 'hr_id' in request.session:
        if request.session.has_key('hr_id'):
            hr_id = request.session['hr_id']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(id=hr_id)
        hr_issue = reported_issue.objects.filter(reporter=hr_id) .order_by('-id')
        return render(request, 'hr_module/HR_reportedissue.html', {'mem': mem,'hr_issue':hr_issue})
    else:
        return redirect('/')

def HR_trainingdepartment(request):
    if 'hr_id' in request.session:
        if request.session.has_key('hr_id'):
            hr_id = request.session['hr_id']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(id=hr_id)
        Dept = department.objects.all()
        Desig = designation.objects.all()
        return render(request, 'hr_module/HR_trainingdepartment.html', {'mem': mem,'Dept':Dept,'Desig':Desig})
    else:
        return redirect('/')

def HR_trainerslist(request,id):
    if 'hr_id' in request.session:
        if request.session.has_key('hr_id'):
            hr_id = request.session['hr_id']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(id=hr_id)
        Dept = department.objects.get(id=id)
        deptid = id
        Trainer = designation.objects.get(designation='Trainer')
        trainers_data = user_registration.objects.filter(designation=Trainer).filter(department=id)
        topics = topic.objects.all()
        return render(request, 'hr_module/HR_trainerslist.html', {'mem': mem,'trainers_data': trainers_data, 'topics': topics, 'Dept': Dept, 'deptid': deptid})
    else:
        return redirect('/')

def HR_trainersteam(request,id):
    if 'hr_id' in request.session:
        if request.session.has_key('hr_id'):
            hr_id = request.session['hr_id']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(id=hr_id)
        user = user_registration.objects.filter(id=id)
        team = create_team.objects.filter(trainer_id=id)
        return render(request, 'hr_module/HR_trainersteam.html', {'mem': mem,'user': user, 'team': team})
    else:
        return redirect('/')

def HR_trainersteamdetails(request,id):
    if 'hr_id' in request.session:
        if request.session.has_key('hr_id'):
            hr_id = request.session['hr_id']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(id=hr_id)
        id = id
        num = previousTeam.objects.filter(teamname=id).count()
        num1 = topic.objects.filter(team=id).count()
        return render(request, 'hr_module/HR_trainersteamdetails.html', {'mem': mem,'num':num, 'num1':num1,'id': id})
    else:
        return redirect('/')

def HR_trainees(request,id):
    if 'hr_id' in request.session:
        if request.session.has_key('hr_id'):
            hr_id = request.session['hr_id']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(id=hr_id)
        trainees_data = previousTeam.objects.filter(teamname=id).order_by('-id')
        return render(request, 'hr_module/HR_trainees.html', {'trainees_data': trainees_data, 'mem': mem})
    else:
        return redirect('/')

def HR_traineestopic(request,id):
    if 'hr_id' in request.session:
        if request.session.has_key('hr_id'):
            hr_id = request.session['hr_id']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(id=hr_id)
        topics = topic.objects.filter(team=id).order_by("-id")
        return render(request, 'hr_module/HR_traineestopics.html', {'topics': topics, 'mem': mem})
    else:
        return redirect('/')

def HR_traineeprofile(request,id):
    if 'hr_id' in request.session:
        if request.session.has_key('hr_id'):
            hr_id = request.session['hr_id']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(id=hr_id)
        trainees_data = user_registration.objects.get(id=id)
        user = user_registration.objects.get(id=id)
        num = trainer_task.objects.filter(user=user).filter(task_status='1').count()
        progress = user_registration.objects.filter(id=id)
        labels = []
        data = []
        queryset = user_registration.objects.filter(id=id)
        for i in queryset:
            labels = [i.workperformance, i.attitude, i.creativity]
            data = [i.workperformance, i.attitude, i.creativity]
        return render(request, 'hr_module/HR_traineesprofile.html', {'trainees_data': trainees_data, 'mem': mem,'num':num,'labels':labels,'data':data,'progress':progress})
    else:
        return redirect('/')

def HR_traineecompletedtask(request,id):
    if 'hr_id' in request.session:
        if request.session.has_key('hr_id'):
            hr_id = request.session['hr_id']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(id=hr_id)
        user = user_registration.objects.get(id=id)
        
        task = trainer_task.objects.filter(user=user).filter(task_status='1')
        return render(request, 'hr_module/HR_traineecompletedtask.html', {'mem': mem,'task':task})
    else:
        return redirect('/')

def HR_employeesdepartment(request):
    if 'hr_id' in request.session:
        if request.session.has_key('hr_id'):
            hr_id = request.session['hr_id']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(id=hr_id)
        Dept = department.objects.all()
        return render(request, 'hr_module/HR_employeesdepartment.html', {'mem': mem,'Dept':Dept})
    else:
        return redirect('/')

def HR_employeeslist(request,id):
    if 'hr_id' in request.session:
        if request.session.has_key('hr_id'):
            hr_id = request.session['hr_id']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(id=hr_id)
        Dept = department.objects.get(id=id)
        deptid = id
        Desig = designation.objects.filter(branch_id=Dept.branch_id).exclude(designation='admin').exclude(designation='manager')
        return render(request, 'hr_module/HR_employeeslist.html', {'mem': mem,'Dept':Dept,'Desig':Desig,'deptid':deptid})
    else:
        return redirect('/')

def HR_viewtrainers(request, id, did):
    if 'hr_id' in request.session:
        if request.session.has_key('hr_id'):
            hr_id = request.session['hr_id']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(id=hr_id)
        userreg = user_registration.objects.filter(designation=id).filter(department=did).order_by("-id")
        return render(request, 'hr_module/HR_viewtrainers.html', {'mem': mem,'userreg':userreg})
    else:
        return redirect('/')

def HR_trainerprofile(request, id):
    if 'hr_id' in request.session:
        if request.session.has_key('hr_id'):
            hr_id = request.session['hr_id']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(id=hr_id)
        userreg = user_registration.objects.get(id=id)
        return render(request, 'hr_module/HR_trainerprofile.html', {'mem': mem,'userreg':userreg})
    else:
        return redirect('/')

def HR_trainercurrenttrainees(request, id):
    if 'hr_id' in request.session:
        if request.session.has_key('hr_id'):
            hr_id = request.session['hr_id']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(id=hr_id)
        team= create_team.objects.filter(trainer_id=id,team_status="0").values_list('id', flat=True)
        user = previousTeam.objects.filter(teamname_id__in=team).values_list('user', flat=True)
        trainees = user_registration.objects.filter(id__in=user)
        return render(request, 'hr_module/HR_trainercurrenttrainees.html', {'mem': mem,'trainees':trainees,'user':user})
    else:
        return redirect('/')

def HR_trainerprevioustrainees(request, id):
    if 'hr_id' in request.session:
        if request.session.has_key('hr_id'):
            hr_id = request.session['hr_id']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(id=hr_id)
        team= create_team.objects.filter(trainer_id=id,team_status="1").values_list('id', flat=True)
        user = previousTeam.objects.filter(teamname_id__in=team).values_list('user', flat=True)
        trainees = user_registration.objects.filter(id__in=user)
        return render(request, 'hr_module/HR_trainerprevioustrainees.html', {'mem': mem,'trainees':trainees,'user':user})
    else:
        return redirect('/')

def HR_trainersattendance(request, id):
    if 'hr_id' in request.session:
        if request.session.has_key('hr_id'):
            hr_id = request.session['hr_id']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(id=hr_id)
        usr = user_registration.objects.get(id=id)
        return render(request, 'hr_module/HR_trainersattendance.html', {'mem': mem,'usr':usr})
    else:
        return redirect('/')

def HR_trainersattendanceview(request, id):
    if 'hr_id' in request.session:
        if request.session.has_key('hr_id'):
            hr_id = request.session['hr_id']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(id=hr_id)
        usr = user_registration.objects.get(id=id)
        if request.method == "POST":
            fromdate = request.POST.get('fromdate')
            todate = request.POST.get('todate')
            adata = attendance.objects.filter(date__range=[fromdate, todate]).filter(user_id=id)
            return render(request, 'hr_module/HR_trainersattendancesort.html', {'mem': mem,'usr':usr,'adata':adata})
    else:
        return redirect('/')

def HR_employeedetails(request,id,did):
    if 'hr_id' in request.session:
        if request.session.has_key('hr_id'):
            hr_id = request.session['hr_id']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(id=hr_id)
        emp_data = user_registration.objects.filter(designation_id=id,department=did)
        return render(request, 'hr_module/HR_employeedetails.html', {'mem': mem,'emp_data':emp_data})
    else:
        return redirect('/')

def HR_employeesprofile(request,id):
    if 'hr_id' in request.session:
        if request.session.has_key('hr_id'):
            hr_id = request.session['hr_id']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(id=hr_id)
        emp_data = user_registration.objects.get(id=id)
        labels = []
        data = []
        queryset = user_registration.objects.filter(id=id)
        for i in queryset:
            labels = [i.workperformance, i.attitude, i.creativity]
            data = [i.workperformance, i.attitude, i.creativity]
        return render(request, 'hr_module/HR_employeesprofile.html', {'mem': mem,'emp_data':emp_data,'labels': labels, 'data': data})
    else:
        return redirect('/')


def HR_employeesinvolvedprojects(request,id,did):
    if 'hr_id' in request.session:
        if request.session.has_key('hr_id'):
            hr_id = request.session['hr_id']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(id=hr_id)
        mem1 = user_registration.objects.filter(id__in=id,designation_id__in=did).values_list('id', flat=True)
        mem2 = designation.objects.get(designation="project manager")
        mem3 = designation.objects.get(designation="team leader")
        mem4 = designation.objects.get(designation="developer")
        des_id = mem2.id
        des1_id=mem3.id
        des2_id=mem4.id
        x_id=int(did)
        if x_id==des_id:
            Pro_data = project.objects.filter(projectmanager_id=id).order_by("-id")
            return render(request, 'hr_module/HR_employeesinvolvedprojects.html', {'mem': mem,'Pro_data': Pro_data})
        elif x_id==des1_id or x_id==des2_id:
            Pro_data = project_taskassign.objects.filter(developer=id).order_by("-id")
            return render(request, 'hr_module/HR_employeesinvolvedprojects.html', {'mem': mem,'Pro_data': Pro_data})
        else:
            return render(request, 'hr_module/HR_employeesinvolvedprojects.html', {'mem': mem})
    else:
        return redirect('/')

def HR_employeesattendance(request,id):
    if 'hr_id' in request.session:
        if request.session.has_key('hr_id'):
            hr_id = request.session['hr_id']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(id=hr_id)
        id = id
        return render(request, 'hr_module/HR_employeesattendance.html', {'mem': mem,'id': id})
    else:
        return redirect('/')

def HR_employeesattendancesort(request,id):
    if 'hr_id' in request.session:
        if request.session.has_key('hr_id'):
            hr_id = request.session['hr_id']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(id=hr_id)
        id = id
        if request.method == "POST":
            fromdate = request.POST.get('fromdate')
            todate = request.POST.get('todate')
            mem1 = attendance.objects.filter(date__range=[fromdate, todate]).filter(user_id=id)
            return render(request, 'hr_module/HR_employeesattendancesort.html', {'mem1': mem1,'id': id,'mem':mem})
    else:
        return redirect('/')

def HR_changepassword(request):
    if 'hr_id' in request.session:

        if request.session.has_key('hr_id'):
            hr_id = request.session['hr_id']
        mem = user_registration.objects.filter(id=hr_id)
        if request.method == 'POST':
            abc = user_registration.objects.get(id=hr_id)
            oldps = request.POST['currentPassword']
            newps = request.POST['newPassword']
            cmps = request.POST.get('confirmPassword')
            if oldps != newps:
                if newps == cmps:
                    abc.password = request.POST.get('confirmPassword')
                    abc.save()
                    msg_success= "password changed"
                    return render(request, 'hr_module/HR_changepassword.html', {'mem': mem,'msg_success':msg_success})
            elif oldps == newps:
                    msg_warning= " current password and new  password are same"
                    return render(request, 'hr_module/HR_changepassword.html', {'mem': mem,'msg_warning':msg_warning})
            elif newps == cmps:
                msg_warning= " new password and confirm same password not matching"
                return render(request, 'hr_module/HR_changepassword.html', {'mem': mem,'msg_warning':msg_warning})
            # return render(request, 'hr_module/HR_changepassword.html', {'mem': mem})
        return render(request, 'hr_module/HR_changepassword.html', {'mem': mem})
    else:
        return redirect('/')

def HR_accountsettings(request):
    if 'hr_id' in request.session:
        if request.session.has_key('hr_id'):
           hr_id = request.session['hr_id']
        mem = user_registration.objects.filter(id=hr_id)
        if request.method == 'POST':
            id = request.GET.get('id')
            abc = user_registration.objects.get(id=id)
            abc.photo = request.FILES['filenamees']
            abc.save()
            msg_success= "image changed"
            return render(request, 'hr_module/HR_accountsettings.html', {'msg_success':msg_success,'mem':mem})
        return render(request, 'hr_module/HR_accountsettings.html',{'mem':mem})
    else:
        return redirect('/')

def HR_imagesettings(request):
    if 'hr_id' in request.session:
        if request.session.has_key('hr_id'):
           hr_id = request.session['hr_id']
        mem = user_registration.objects.filter(id=hr_id)
        print('hr_id')
        return render(request,'hr_module/HR_accountsettings.html', {'mem': mem})
    else:
        return redirect('/')

def HR_logout(request):
    if 'hr_id' in request.session:
        request.session.flush()
        return redirect('/')
    else:
        return redirect('/')

# *******new******************************

def completedteam(request):
    if 'usernametm2' in request.session:
        if request.session.has_key('usernametm'):
            usernametm = request.session['usernametm']
        if request.session.has_key('usernametm1'):
            usernametm1 = request.session['usernametm1']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(designation_id=usernametm).filter(fullname=usernametm1)
        var = create_team.objects.filter(team_status=1).order_by('-id')
        des = designation.objects.get(designation='trainer')
        var1 = user_registration.objects.filter(designation_id=des.id)
        return render(request,'completedteam.html',{'mem':mem,'var':var,'var1':var1})
    return redirect('/')

def completed_team_trainees(request,id):
    if 'usernametm2' in request.session:
        if request.session.has_key('usernametm'):
            usernametm = request.session['usernametm']
        if request.session.has_key('usernametm1'):
            usernametm1 = request.session['usernametm1']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(designation_id=usernametm).filter(fullname=usernametm1)
        var = previousTeam.objects.filter(teamname=id)
       
        return render(request,'completed_team_trainees.html',{'mem':mem,'var':var})
    return redirect('/')

def completed_team_task(request,id,tid):
    if 'usernametm2' in request.session:
        if request.session.has_key('usernametm'):
            usernametm = request.session['usernametm']
        if request.session.has_key('usernametm1'):
            usernametm1 = request.session['usernametm1']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(designation_id=usernametm).filter(fullname=usernametm1)
        var =trainer_task.objects.filter(user=id,team_name=tid).order_by('-id')
      
        return render(request,'completed_team_task.html',{'mem':mem,'var':var})
    return redirect('/')

def probations(request):
    
        if request.session.has_key('usernametm'):
            usernametm = request.session['usernametm']
        if request.session.has_key('usernametm1'):
            usernametm1 = request.session['usernametm1']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(designation_id=usernametm).filter(fullname=usernametm1)
        des= designation.objects.get(designation='trainee')
        var =user_registration.objects.filter(designation_id=des.id).order_by('-id')
        team=create_team.objects.filter(team_status=0)
        pb=probation()
        if request.method == 'POST':
            pb.team=create_team.objects.get(id=int(request.POST['team']))
            ut=create_team.objects.get(id=int(request.POST['team']))
            pb.trainer_id=ut.trainer_id
            print(pb.trainer_id)
            pb.reason=request.POST['extend_reason']
            pb.startdate=request.POST['startdate']
            pb.enddate=request.POST['enddate']
            id = request.GET.get('tid')
            pb.user_id=id
            pb.save()
            msg_success="probation extended"
            return render(request,'probation.html',{'mem':mem,'var':var,'team':team,'msg_success':msg_success})
        
        return render(request,'probation.html',{'mem':mem,'var':var,'team':team})


# def probation_stop(request):  
#     id = request.GET.get('id')
#     var = probation.objects.filter(status=0,user_id=id).latest()   
#     var.stop_reason = request.POST['stop_reason'] 
#     var.status= 1
#     var.stopdate=datetime.now()
#     var.user_id=id 
#     var.save()  
#     print(var)
#     msg_success="stoped succesfully"
#     return render(request, 'probation.html', {'msg_success':msg_success})

# def probation_renew(request):  
#     id = request.GET.get('id')
#     var = probation.objects.filter(status=1,user_id=id).latest() 
    
#     alt = var.stopdate
    
#     print(alt)
#     akm = datetime.now().date()
#     v= (akm-alt).days
#     var.extension = (akm-alt).days
#     var.status= 0
#     var.renewdate=datetime.now() 
#     var.user_id=id
#     var.save()  
#     x=user_registration.objects.get(id=id)
#     del_add = x.trainee_delay
#     x.trainee_delay=del_add+v
#     x.save()
#     msg_success="renew succesfully"
#     return render(request, 'probation.html', {'msg_success':msg_success})


def probation_stop(request):  
    id = request.GET.get('id')
    var = probation() 
    var.stop_reason = request.POST['stop_reason'] 
    var.status= 1
    var.stopdate=datetime.now()
    var.user_id=id 
    var.save()  
    x=user_registration.objects.get(id=id)
    x.status="resigned"
    x.save()
    msg_success="stoped succesfully"
    return render(request, 'probation.html', {'msg_success':msg_success})

def probation_renew(request):  
    id = request.GET.get('id')
    var = probation.objects.filter(status=1,user_id=id).latest() 
    alt = var.stopdate
    akm = datetime.now().date()
    v= (akm-alt).days
    z= (akm-alt).days
    var.extension = (akm-alt).days
    var.status= 0
    var.renewdate=datetime.now()
    var.user_id=id
    var.save()  
    x=user_registration.objects.get(id=id)
    delta =  x.enddate+timedelta(z)
    x.enddate =delta
    del_add = x.trainee_delay
    x.trainee_delay=del_add+v
    x.status='active'
    x.save()
    msg_success="renew succesfully"
    return render(request, 'probation.html', {'msg_success':msg_success})
    
def task_perform(request):
    if request.method == 'POST':
        id = request.GET.get('id')
        abc = trainer_task.objects.get(id=id)
        abc.task_progress = request.POST['sele']
        abc.save()
        msg_success = "progress added"
        return render(request,'trainer_taskgiven.html',{'msg_success':msg_success})
    else:
        pass

def tm_trainee_status(request):
    if 'usernametm2' in request.session:
        if request.session.has_key('usernametm'):
            usernametm = request.session['usernametm']
        if request.session.has_key('usernametm1'):
            usernametm1 = request.session['usernametm1']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(
            designation_id=usernametm).filter(fullname=usernametm1)
        
        des = designation.objects.get(designation="trainee")
        var=user_registration.objects.filter(designation_id=des.id)
        return render(request, 'tm_trainee_status.html', {'mem': mem,'var':var})
    else:
        return redirect('/')
        
        

def tm_trainee_details(request):
    if 'usernametm2' in request.session:
        if request.session.has_key('usernametm'):
            usernametm = request.session['usernametm']
        if request.session.has_key('usernametm1'):
            usernametm1 = request.session['usernametm1']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(
            designation_id=usernametm).filter(fullname=usernametm1)
        emp = request.POST['emp']
        names = trainer_task.objects.filter(user_id=emp).order_by('-id')                                          
        mm = names.values_list('delay', flat='true')
        a=0
        for i in mm:
            
            a=a+int(i)
        return render(request, 'tm_trainee_details.html', {'mem': mem,'names':names,'a':a})
    else:
        return redirect('/')


def manager_trainee_status(request):
    if 'm_id' in request.session:
        if request.session.has_key('m_id'):
            m_id = request.session['m_id']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(id=m_id)
        dep=department.objects.all()
        des = designation.objects.get(designation="trainee")
        var=user_registration.objects.filter(designation_id=des.id)
        return render(request, 'manager_trainee_status.html', {'mem': mem,'var':var,'dep':dep})
    else:
        return redirect('/')


@csrf_exempt
def manager_trainess(request):
    if 'm_id' in request.session:
        if request.session.has_key('m_id'):
            m_id = request.session['m_id']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(id=m_id)
        dept_id = request.GET.get('dept_id')
        des = designation.objects.get(designation="trainee")
        Desig = user_registration.objects.filter(department_id=dept_id,designation_id=des.id)
       
        return render(request,'manager_trainess.html',{'mem': mem,'Desig': Desig, })
    else:
        return redirect('/')

@csrf_exempt
def manager_trainee_details(request):
    if 'm_id' in request.session:
        if request.session.has_key('m_id'):
            m_id = request.session['m_id']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(id=m_id)
        emp = request.POST['emp']
        names = trainer_task.objects.filter(user_id=emp).order_by('-id')                                          
        mm = names.values_list('delay', flat='true')
        a=0
        for i in mm:
            
            a=a+int(i)
        return render(request, 'manager_trainee_details.html', {'mem': mem,'names':names,'a':a})
    else:
        return redirect('/')



def BRadmin_trainee_status(request):
    if 'Adm_id' in request.session:
        if request.session.has_key('Adm_id'):
            Adm_id = request.session['Adm_id']
        else:
            return redirect('/')
        Adm = user_registration.objects.filter(id=Adm_id)
        dep=department.objects.all()
        des = designation.objects.get(designation="trainee")
        var=user_registration.objects.filter(designation_id=des.id)
        return render(request, 'BRadmin_trainee_status.html', {'Adm': Adm,'var':var,'dep':dep})
    else:
        return redirect('/')


@csrf_exempt
def BRadmin_trainess(request):
    if 'Adm_id' in request.session:
        if request.session.has_key('Adm_id'):
            Adm_id = request.session['Adm_id']
        else:
            return redirect('/')
        Adm = user_registration.objects.filter(id=Adm_id)
        dept_id = request.GET.get('dept_id')
        des = designation.objects.get(designation="trainee")
        Desig = user_registration.objects.filter(department_id=dept_id,designation_id=des.id)
       
        return render(request,'BRadmin_trainess.html',{'Adm': Adm,'Desig': Desig, })
    else:
        return redirect('/')

@csrf_exempt
def BRadmin_trainee_details(request):
    if 'Adm_id' in request.session:
        if request.session.has_key('Adm_id'):
            Adm_id = request.session['Adm_id']
        else:
            return redirect('/')
        Adm = user_registration.objects.filter(id=Adm_id)
        emp = request.POST['emp']
        names = trainer_task.objects.filter(user_id=emp).order_by('-id')                                          
        mm = names.values_list('delay', flat='true')
        a=0
        for i in mm:
            
            a=a+int(i)
        return render(request, 'BRadmin_trainee_details.html', {'Adm': Adm,'names':names,'a':a})
    else:
        return redirect('/')

def BRadmin_leavestatus(request):
    if 'Adm_id' in request.session:
        if request.session.has_key('Adm_id'):
            Adm_id = request.session['Adm_id']
        else:
            return redirect('/')
        Adm = user_registration.objects.filter(id=Adm_id)

        cous = course.objects.all()
        dep = department.objects.all()
        des = designation.objects.all()
        emp = user_registration.objects.all()

        return render(request,'BRadmin_leavestatus.html',{'Adm': Adm, 'cous':cous,'dep':dep,'des':des,'emp':emp,})
    else:
        return redirect('/')

@csrf_exempt
def BRadmin_leavedesgn(request):
    if 'Adm_id' in request.session:
        if request.session.has_key('Adm_id'):
            Adm_id = request.session['Adm_id']
        else:
            return redirect('/')
        Adm = user_registration.objects.filter(id=Adm_id)

        dept_id = request.GET.get('dept_id')
        
        br_id = department.objects.get(id=dept_id)
        
        Desig = designation.objects.filter(~Q(designation="admin")).filter(branch_id=br_id.branch_id)
        return render(request,'BRadmin_leavedesgn.html',{'Adm': Adm,'Desig': Desig})
    else:
        return redirect('/')

@csrf_exempt
def BRadmin_leave_details(request):
    
    emp = request.GET.get('emp')
    fdate = request.GET.get('fdate')
    tdate = request.GET.get('tdate')
    leaves = leave.objects.filter(user_id=emp,from_date__gte=fdate,to_date__lte=tdate)
    return render(request,'BRadmin_leave_details.html',{'names':leaves})
   
def BRadmin_workstatus(request):
    if 'Adm_id' in request.session:
        if request.session.has_key('Adm_id'):
            Adm_id = request.session['Adm_id']
        else:
            return redirect('/')
        Adm = user_registration.objects.filter(id=Adm_id)

        cous = course.objects.all()
        dep = department.objects.all()
        des = designation.objects.all()
        emp = user_registration.objects.all()

        return render(request,'BRadmin_workstatus.html',{'Adm': Adm, 'cous':cous,'dep':dep,'des':des,'emp':emp,})
    else:
        return redirect('/')

# ---------------------PM updates------------------------------------------------

def pm_projectcards(request):
    if 'prid' in request.session:
        if request.session.has_key('prid'):
            prid = request.session['prid']
        else:
           return redirect('/')
        pro = user_registration.objects.filter(id=prid)
        return render(request, 'pm_projectcards.html',{'pro':pro})
    else:
        return redirect('/')

def pm_createmodule(request):
    if 'prid' in request.session:
        if request.session.has_key('prid'):
            prid = request.session['prid']
        else:
           return redirect('/')
        pro = user_registration.objects.filter(id=prid)
        project_data = project.objects.filter(projectmanager_id=prid)
        # return render(request, 'pm_createmodule.html',{'pro':pro,'project_data':project_data})
        print(project_data)
        if request.method =='POST':
            var = project_module_assign()
            var.project_name = project.objects.get(id=int(request.POST['project_id']))
            var.module = request.POST['module']
            var.description = request.POST['moduledescription']
            var.save()
            msg_success = "Module created"
            return render(request, 'pm_createmodule.html',{'pro':pro,'project_data':project_data,'msg_success':msg_success})
        return render(request, 'pm_createmodule.html',{'pro':pro,'project_data':project_data})
    else:
        return redirect('/')


def pm_createtable(request):
    if 'prid' in request.session:
        if request.session.has_key('prid'):
            prid = request.session['prid']
        else:
           return redirect('/')
        pro = user_registration.objects.filter(id=prid)
        project_data = project.objects.filter(projectmanager_id = prid)
        var = project_table()
        if request.method == 'POST':
            var.project = project.objects.get(id=int(request.POST['project']))
            var.module_name_id = request.POST['emp']
            var.description = request.POST['table']
            var.save()
            msg_success = "table created"
            return render(request, 'pm_createtables.html',{'pro':pro,'project_data':project_data,'msg_success':msg_success})
        return render(request, 'pm_createtables.html',{'pro':pro,'project_data':project_data})
    else:
        return redirect('/')

@csrf_exempt
def pm_module_data(request):
    if 'prid' in request.session:
        if request.session.has_key('prid'):
            prid = request.session['prid']
        else:
           return redirect('/')
        pro = user_registration.objects.filter(id=prid)
        pro_id = request.GET.get('dept_id')
        Desig = project_module_assign.objects.filter(project_name=pro_id)
        
        return render(request,'pm_module_data.html',{'pro': pro,'Desig': Desig})
    else:
        return redirect('/')

def pm_projectview(request):
    if 'prid' in request.session:
        if request.session.has_key('prid'):
            prid = request.session['prid']
        else:
           return redirect('/')
        pro = user_registration.objects.filter(id=prid)
        pro_data = project.objects.filter(projectmanager_id=prid)
        return render(request,'pm_projectview.html',{'pro': pro,'pro_data':pro_data})
    else:
        return redirect('/')

def pm_prodata(request,id):
    if 'prid' in request.session:
        if request.session.has_key('prid'):
            prid = request.session['prid']
        else:
           return redirect('/')
        pro = user_registration.objects.filter(id=prid)
        pro_data = project.objects.get(id=id)
        return render(request,'pm_prodata.html',{'pro': pro,'pro_data':pro_data})
    else:
        return redirect('/')

def pm_project_assigned(request,id):
    if 'prid' in request.session:
        if request.session.has_key('prid'):
            prid = request.session['prid']
        else:
           return redirect('/')
        pro = user_registration.objects.filter(id=prid)
        pro_data = project.objects.get (id = id)
        display = project_taskassign.objects.filter(project_id=id).values('project_id','tl_id').distinct()
        user = user_registration.objects.all()
        com = project.objects.filter(status = "completed")
        return render(request,'pm_project_assigned.html',{'pro': pro,'pro_data':pro_data,'display':display,'user':user,'com':com})
    else:
        return redirect('/')
# -------------------------------TM ------------------------------------------------
def trainer_progress_add(request,id):
    mem = user_registration.objects.get(id=id)
    if 'usernametm2' in request.session:
        if request.session.has_key('usernametm2'):
            usernametm2 = request.session['usernametm2']
        if request.session.has_key('usernametm1'):
            usernametm1 = request.session['usernametm1']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(id=usernametm2)
        var = user_registration.objects.get(id=id)
        if request.method == 'POST':
            var.attitude = request.POST['sele1']
            var.creativity = request.POST['sele2']
            var.workperformance = request.POST['sele3']
            var.save()
            msg_success = "progress added"
            return render(request, 'trainer_progress_add.html', {'mem': mem,'msg_success':msg_success})
        return render(request, 'trainer_progress_add.html', {'mem': mem})
    else:
        return redirect('/')

# -----------------------------------tester-----------------------------

def tester_leave(request):
    if 'usernametsid' in request.session:
        if request.session.has_key('usernametsid'):
            usernametsid = request.session['usernametsid']
        else:
           return redirect('/')
        mem=user_registration.objects.filter(id=usernametsid)
        return render(request, 'tester_leave.html', {'mem': mem})
    else:
        return redirect('/')

def tester_apply_leave(request):
    if 'usernametsid' in request.session:
        if request.session.has_key('usernametsid'):
            usernametsid = request.session['usernametsid']
        if request.session.has_key('usernamets'):
            usernamets = request.session['usernamets']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(designation_id=usernamets).filter(id=usernametsid)
        if request.method == 'POST':
            apply_leave = leave()
            apply_leave.from_date = request.POST['from']
            apply_leave.to_date = request.POST['to']
            apply_leave.leave_status = request.POST['haful']
            apply_leave.reason = request.POST['reason']
            apply_leave.user =user_registration.objects.get(id=usernametsid)
            apply_leave.designation_id =usernamets
            apply_leave.leaveapprovedstatus = 0
            apply_leave.save()

            start = datetime.strptime(apply_leave.from_date, '%Y-%m-%d').date() 
            end = datetime.strptime(apply_leave.to_date, '%Y-%m-%d').date()

            diff = (end  - start).days
            
            cnt =  Event.objects.filter(start_time__range=(start,end)).count()
            
            if diff == 0:
                apply_leave.days = 1
            else:
                apply_leave.days = diff - cnt
            msg_success = "leave applied"
            return render(request, 'tester_apply_leave.html',{'mem':mem,"msg_success":msg_success})
        else:
            pass
        return render(request, 'tester_apply_leave.html',{'mem':mem})
    else:
        return redirect('/')

def tester_appliedleave(request):
    if 'usernametsid' in request.session:
        if request.session.has_key('usernametsid'):
            usernametsid= request.session['usernametsid']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(id=usernametsid)
        hr_leave = leave.objects.filter(user=usernametsid).order_by('-id')
        return render(request, 'tester_appliedleave.html', {'mem': mem,'hr':hr_leave})
    else:
        return redirect('/')

def tester_employees(request):
    if 'usernametsid' in request.session:
        if request.session.has_key('usernametsid'):
            usernametsid= request.session['usernametsid']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(id=usernametsid)
        return render(request, 'tester_employees.html', {'mem': mem})
    else:
        return redirect('/')

def tester_tllist(request):
    if 'usernametsid' in request.session:
        if request.session.has_key('usernametsid'):
            usernametsid= request.session['usernametsid']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(id=usernametsid)
        p = designation.objects.get(designation="team leader")
        tlfil = user_registration.objects.filter(designation_id=p.id,status="active").order_by("-id")
        return render(request, 'tester_tllist.html', {'mem': mem,'tlfil':tlfil})
    else:
        return redirect('/')

def tester_tldashboard(request,id):
    if 'usernametsid' in request.session:
        if request.session.has_key('usernametsid'):
            usernametsid= request.session['usernametsid']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(id=usernametsid)
        tls = user_registration.objects.filter(id=id) 
        labels = []
        data = []
        queryset = user_registration.objects.filter(id=id)
        for i in queryset:
            labels=[i.workperformance,i.attitude,i.creativity]
            data=[i.workperformance,i.attitude,i.creativity]
        return render(request, 'tester_tldashboard.html',{'labels':labels,'data':data,'mem': mem, 'tls': tls})
    else:
        return redirect('/') 

def ts_ltteaminvolved(request, id):
    if 'usernametsid' in request.session:
        if request.session.has_key('usernametsid'):
            usernametsid= request.session['usernametsid']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(id=usernametsid)
        pri = project_taskassign.objects.filter(developer_id=id).order_by("-id")
        return render(request, 'ts_ltteaminvolved.html',{'mem': mem, 'pri': pri})
    else:
        return redirect('/') 

def tl_currentperformance(request,id):
    if 'usernametsid' in request.session:
        if request.session.has_key('usernametsid'):
            usernametsid= request.session['usernametsid']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(id=usernametsid)
        mem1 = user_registration.objects.get(id=id)
        if request.method == 'POST':
            mem1.attitude = request.POST['sele1']
            mem1.creativity = request.POST['sele2']
            mem1.workperformance = request.POST['sele3']
            mem1.save()
            msg_success="performance added"
            return render(request, 'tl_currentperformanace.html',{'mem': mem,'mem1':mem1,'msg_success':msg_success})
        return render(request, 'tl_currentperformanace.html',{'mem': mem,'mem1':mem1})
    else:
        return redirect('/')

def ts_allocatetl(request):
    if 'usernametsid' in request.session:
        if request.session.has_key('usernametsid'):
            usernametsid= request.session['usernametsid']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(id=usernametsid)
        des_tl = designation.objects.get(designation = "team leader")
        des_dev = designation.objects.get(designation = "developer ")
        devs = user_registration.objects.filter(designation_id=des_dev.id,status="active")
        tls = user_registration.objects.filter(designation_id=des_tl.id,status="active")
        tl_name = user_registration.objects.all()
        if request.method == "POST":
            emp_id = request.POST.get('id')
            tl_id = request.POST.get('team')
            alocate = user_registration.objects.get(id=emp_id)
            alocate.tl_id = tl_id
            alocate.save()
            msg_success="tl added"
            return render(request, 'ts_allocatetl.html',{'mem': mem,'devs':devs,'tls':tls,'tl_name':tl_name,'msg_success':msg_success})
        return render(request, 'ts_allocatetl.html',{'mem': mem,'devs':devs,'tls':tls,'tl_name':tl_name})
    else:
        return redirect('/')

def ts_tl_attandance(request,id):
    if 'usernametsid' in request.session:
        if request.session.has_key('usernametsid'):
            usernametsid= request.session['usernametsid']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(id=usernametsid)
        man = attendance.objects.filter(user_id=id) 
        return render(request, 'ts_tl_attandance.html',{'mem': mem,'man':man})
    else:
        return redirect('/')

def ts_tl_attendance(request,id):
    if 'usernametsid' in request.session:
        if request.session.has_key('usernametsid'):
            usernametsid= request.session['usernametsid']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(id=usernametsid)
        man = user_registration.objects.get(id=id)  
        if request.method == "POST":
            fromdate = request.POST.get('fromdate')
            todate = request.POST.get('todate') 
            mem1 = attendance.objects.filter(date__range=[fromdate, todate]).filter(user_id=id)
            return render(request, 'ts_tl_attandance.html',{'mem': mem,'man':man,'mem1':mem1}) 
        return render(request, 'ts_tl_attendance.html',{'mem': mem,'man':man})
    else:
        return redirect('/')

def ts_dev_team(request, id):
    if 'usernametsid' in request.session:
        if request.session.has_key('usernametsid'):
            usernametsid= request.session['usernametsid']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(id=usernametsid)
        teamid = user_registration.objects.filter(tl_id=id,status="active").order_by("-id") 
        return render(request, 'ts_dev_team.html',{'mem': mem,'teamid': teamid})
    else:
        return redirect('/')  

def ts_dev_team_profile(request, id):
    if 'usernametsid' in request.session:
        if request.session.has_key('usernametsid'):
            usernametsid= request.session['usernametsid']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(id=usernametsid) 
        ind = user_registration.objects.filter(id=id)
        labels = []
        data = []
        queryset = user_registration.objects.filter(id=id)
        for i in queryset:
            labels=[i.workperformance,i.attitude,i.creativity]
            data=[i.workperformance,i.attitude,i.creativity]
        return render(request, 'ts_dev_team_profile.html',{'mem': mem,'ind': ind,'labels':labels,'data':data})
    else:
        return redirect('/')  

def ts_tl_dev_teaminvolved(request, id):
    if 'usernametsid' in request.session:
        if request.session.has_key('usernametsid'):
            usernametsid= request.session['usernametsid']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(id=usernametsid)
        pri = project_taskassign.objects.filter(developer_id=id).order_by("-id")
        return render(request, 'ts_tl_dev_teaminvolved.html',{'mem': mem, 'pri': pri})
    else:
        return redirect('/')

def ts_Devlists(request):
    if 'usernametsid' in request.session:
        if request.session.has_key('usernametsid'):
            usernametsid= request.session['usernametsid']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(id=usernametsid)
        pro_dep = user_registration.objects.get(id=usernametsid)
        des_id = designation.objects.get(designation="developer")
        man = user_registration.objects.filter(designation_id=des_id.id).filter(department_id=pro_dep.department_id,status="active").order_by("-id")
        return render(request, 'ts_Devlists.html',{'mem':mem,'man':man})
    else:
        return redirect('/')

def ts_DevDashboard(request,id):
    if 'usernametsid' in request.session:
        if request.session.has_key('usernametsid'):
            usernametsid= request.session['usernametsid']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(id=usernametsid)
        man = user_registration.objects.get(id=id)
        labels = []
        data = []
        queryset = user_registration.objects.filter(id=id)
        for i in queryset:
            labels=[i.workperformance,i.attitude,i.creativity]
            data=[i.workperformance,i.attitude,i.creativity]
        return render(request, 'ts_DevDashboard.html',{'labels':labels,'data':data,'mem':mem,'man':man})
    else:
        return redirect('/')

# -----------------pm_attendence-----------------------
def projectman_search(request):
    if 'prid' in request.session:
        if request.session.has_key('prid'):
            prid = request.session['prid']
        else:
            return redirect('/')
        pro = user_registration.objects.filter(id=prid)
        des = designation.objects.get(designation = "team leader")
        x = des.id
        tl_data = user_registration.objects.filter(designation_id = x,status = 'active')
        
        return render(request, 'projectman_search.html', {'pro': pro,'tl_data':tl_data})
    else:
        return redirect('/')

@csrf_exempt
def pm_employees_att(request):
    if 'prid' in request.session:
        if request.session.has_key('prid'):
            prid = request.session['prid']
        else:
           return redirect('/')
        pro = user_registration.objects.filter(id=prid)
        pro_id = request.GET.get('dept_id')
        Desig = user_registration.objects.get(id=pro_id)
        return render(request,'pm_employees_att.html',{'pro': pro,'Desig': Desig})
    else:
        return redirect('/')


def pm_attendanceview(request):
    if 'prid' in request.session:
        if request.session.has_key('prid'):
            prid = request.session['prid']
        else:
           return redirect('/')
        pro = user_registration.objects.filter(id=prid)
        project_data = designation.objects.filter(Q(designation = "developer")|Q (designation="team leader"))
        return render(request, 'pm_attendanceview.html',{'pro':pro,'project_data':project_data})
    else:
        return redirect('/')

@csrf_exempt
def pm_employeelist(request):
    if 'prid' in request.session:
        if request.session.has_key('prid'):
            prid = request.session['prid']
        else:
           return redirect('/')
        pro = user_registration.objects.filter(id=prid)
        pro_id = request.GET.get('dept_id')

        Desig = user_registration.objects.filter(designation_id=pro_id,status = "active",projectmanager_id=prid)
        
        return render(request,'pm_employeelist.html',{'pro': pro,'Desig': Desig})
    else:
        return redirect('/')

@csrf_exempt
def pm_employees_attendance_view(request):
    if 'prid' in request.session:
        if request.session.has_key('prid'):
            prid = request.session['prid']
        else:
           return redirect('/')
        pro = user_registration.objects.filter(id=prid)
        pro_id = request.GET.get('des_id')
        
        Desig = attendance.objects.filter(user_id= pro_id)
        return render(request,'pm_employees_attendance_view.html',{'pro': pro,'Desig': Desig})
    else:
        return redirect('/')

def tl_attendanceview(request):
    if 'tlid' in request.session:
        if request.session.has_key('tlid'):
            tlid = request.session['tlid']
        else:
           return redirect('/')
        mem = user_registration.objects.filter(id=tlid)
        Desig = attendance.objects.filter(user_id = tlid)
        return render(request,'tl_attendanceview.html',{'mem': mem,'Desig': Desig})
    else:
        return redirect('/')

def tl_devattendsearch(request):
    if 'tlid' in request.session:
        if request.session.has_key('tlid'):
            tlid = request.session['tlid']
        else:
           return redirect('/')
        mem = user_registration.objects.filter(id=tlid)
        des = designation.objects.get(designation = "developer")
        x = des.id
        tl_data = user_registration.objects.filter(designation_id = x,status = 'active',tl_id=tlid)
        return render(request,'tl_devattendsearch.html',{'mem': mem,'tl_data': tl_data})
    else:
        return redirect('/')
@csrf_exempt
def tl_devattendanceview(request):
    if 'tlid' in request.session:
        if request.session.has_key('tlid'):
            tlid = request.session['tlid']
        else:
           return redirect('/')
        mem = user_registration.objects.filter(id=tlid)
        pro_id = request.GET.get('dept_id')
        x=int(pro_id)
        print(x)
        print(type(x))
        Desig = attendance.objects.filter(user_id= x)
        print(Desig)
        return render(request,'tl_devattendenceview.html',{'mem': mem,'Desig':Desig})
    else:
        return redirect('/')

def tl_devattendanceadd(request):
    if 'tlid' in request.session:
        if request.session.has_key('tlid'):
            tlid = request.session['tlid']
        else:
           return redirect('/')
        mem = user_registration.objects.filter(id=tlid)
        des = designation.objects.get(designation = "developer")
        x = des.id
        tl_data = user_registration.objects.filter(designation_id = x,status = 'active',tl_id=tlid)
        return render(request,'tl_devattendanceadd.html',{'mem': mem,'tl_data': tl_data})
    else:
        return redirect('/')

@csrf_exempt
def tl_employees_att(request):
    if 'tlid' in request.session:
        if request.session.has_key('tlid'):
            tlid = request.session['tlid']
        else:
           return redirect('/')
        mem = user_registration.objects.filter(id=tlid)
        pro_id = request.GET.get('dept_id')
        Desig = user_registration.objects.get(id=pro_id)
        return render(request,'tl_employees_att.html',{'mem': mem,'Desig': Desig})
    else:
        return redirect('/')

def tl_add_attendance(request,id):
    if request.method == 'POST':
        var=attendance()
        var.date=request.POST['date']
        var.user = user_registration.objects.get(id=id)
        var.attendance_status = request.POST['pres']
        var.save()
        msg_success = "attendance added"
        return render(request,'tl_devattendanceadd.html',{'msg_success':msg_success})
    else:
        pass

def pm_add_attendance(request,id):
    if request.method == 'POST':
        var=attendance()
        var.date=request.POST['date']
        var.user = user_registration.objects.get(id=id)
        var.attendance_status = request.POST['pres']
        var.save()
        msg_success = "attendance added"
        return render(request,'projectman_search.html',{'msg_success':msg_success})
    else:
        pass

def current_modules(request,id):
    if 'prid' in request.session:
        if request.session.has_key('prid'):
            prid = request.session['prid']
        else:
           return redirect('/')
        pro = user_registration.objects.filter(id=prid)
        data = project_module_assign.objects.filter(project_name=id)
        tab = project_table.objects.filter(project=id)
        return render(request,'current_modules.html',{'pro': pro,'data': data,'tab':tab})
    else:
        return redirect('/')

def pm_modules_tables(request,id):
    if 'prid' in request.session:
        if request.session.has_key('prid'):
            prid = request.session['prid']
        else:
           return redirect('/')
        pro = user_registration.objects.filter(id=prid)
        
@csrf_exempt
def accounts_leave(request):
    
    emp = request.GET.get('emp')
    fdate = request.GET.get('fdate')
    tdate = request.GET.get('tdate')
    leaves = leave.objects.filter(user_id=emp,from_date__gte=fdate,to_date__lte=tdate)
    return render(request,'accounts_leave.html', {'names':leaves})
    
def pm_leavestatus(request):
    if 'prid' in request.session:
        if request.session.has_key('prid'):
            prid = request.session['prid']
        else:
            return redirect('/')
        pro = user_registration.objects.filter(id=prid)
        dept  = user_registration.objects.get(id=prid)

        dep = department.objects.filter(id=dept.department_id)
        des = designation.objects.all()
        emp = user_registration.objects.all()
        return render(request,'pm_leavestatus.html',{'pro':pro,'dep':dep,'des':des,'emp':emp,})
    else:
        return redirect('/')

@csrf_exempt
def pm_leave(request):
    
    emp = request.GET.get('emp')
    fdate = request.GET.get('fdate')
    tdate = request.GET.get('tdate')
    leaves = leave.objects.filter(user_id=emp,from_date__gte=fdate,to_date__lte=tdate)
    return render(request,'pm_leave.html', {'names':leaves})

@csrf_exempt
def accounts_salary_netsalarydelay(request):
    emp = request.GET.get('empname')
    work_day = request.GET.get('work_day')
    conf_salary = request.GET.get('conf_salary')
    commonleave = request.GET.get('commonleave')
    total_delay = int(emp)+int(commonleave)
    one_day_sal = int(conf_salary) / int(work_day)
    total_delay_amt = float(one_day_sal) * float(total_delay)
    net_salary = float(conf_salary) - float(total_delay_amt)
    if net_salary <= 0:
        net_salary = 0
    return HttpResponse(json.dumps({'net_salary':net_salary}))



@csrf_exempt
def accounts_salary_leave(request):
        fdate = request.GET.get('fdate')
        tdate = request.GET.get('tdate')
        his_id = request.GET.get('his_id')
        global k1
        global d14
        global d13,d15,d16,d17,d18,d19,d20,d21
        try:
            date_exe = acnt_monthdays.objects.get(month_fromdate__gte=fdate,month_todate__lte=tdate)
            if date_exe:
                work_day = date_exe.month_workingdays
                start = datetime.strptime(fdate, '%Y-%m-%d').date()
                end = datetime.strptime(tdate, '%Y-%m-%d').date()
                pro = project_taskassign.objects.filter(startdate__range=(start,end),enddate__range=(start,end), submitted_date__isnull = True).filter(developer_id= his_id, ).values('startdate','enddate')
                pro_start = project_taskassign.objects.filter(startdate__range=(start,end),enddate__range=(start,end),submitted_date__isnull = False).filter(developer_id= his_id, ).values('startdate','enddate','submitted_date')
                print(pro)
                print(pro_start)
                leave_emp = leave.objects.filter(user_id = his_id,from_date__gte = start,to_date__lte = end).values('from_date','to_date')
                k1=0
                for k in leave_emp:
                    k2 = (k['to_date']-k['from_date']).days
                    if k2 == 0:
                        k2 = 1
                    k1 = k1 + k2
                
                d14 =0
                d21 = 0
                d17 = 0
                d20 = 0
                for i in pro:
                    d_start = (i['startdate'])
                    d_end = (i['enddate'])
                    if d_start == d_end:
                       
                        d14 = 0
                    else :

                        diff = (end - d_end).days
                        cnt =  Event.objects.filter(start_time__gte=d_end,start_time__lte=end).values('start_time').count()
                        d14 = diff - cnt
                    
                    d20 = d20 + d14
                
                
                d18 = 0
                d19 = 0
                for i in pro_start:
                    d10 = (i['enddate'])
                    d11 = (i['submitted_date'])
                    diff_date = (d11 - d10).days
                    if diff_date <= 0:
                        d18 = 0
                    else:
                        
                        if d11 <= end:
                            diff = (d11 - d10).days
                            print(diff)
                            cnt =  Event.objects.filter(start_time__gte=d10,start_time__lte=d11).values('start_time').count()
                            d18 = diff - cnt
                            
                        else:
                            diff = (end - d10).days
                            cnt =  Event.objects.filter(start_time__gte=d10,start_time__lte=end).values('start_time').count()
                            d18 = diff - cnt
                          
                    d19 = d19 + d18
                    
                 
                delay_total = d19+d20 
                total_delay =delay_total+k1
                conf = user_registration.objects.get(id=his_id)
                conf_salary = conf.confirm_salary
                if conf_salary == "":
                    conf_salary = 0
                one_day_sal = int(conf_salary) / int(work_day)
                total_delay_amt = float(one_day_sal) * float(total_delay)
                net_salary = float(conf_salary) - float(total_delay_amt)
                if net_salary <= 0:
                    net_salary = 0
                return HttpResponse(json.dumps({'net_salary':net_salary, 'delay_total':delay_total,'k1':k1,'work_day':work_day,'conf_salary':conf_salary}))
            else:
                msg = "please add month days"
                return HttpResponse(json.dumps({'msg':msg}))
        except acnt_monthdays.DoesNotExist:
            msg = "please add month days"
            return HttpResponse(json.dumps({'msg':msg}))






@csrf_exempt
def BRadmin_projects_details(request):
    if 'Adm_id' in request.session:
        emp = request.POST['emp']
        fdate = request.POST['fdate']
        tdate = request.POST['tdate']
        
        names = project_taskassign.objects.filter(developer=emp,startdate__gte=fdate, enddate__lte=tdate) 
        
        start = datetime.strptime(fdate, '%Y-%m-%d').date()
        end = datetime.strptime(tdate, '%Y-%m-%d').date()
        pro = project_taskassign.objects.filter(startdate__range=(start,end),enddate__range=(start,end), submitted_date__isnull = False).filter(developer_id= emp, ).values('startdate','enddate','submitted_date', 'delay')
        pro_false = project_taskassign.objects.filter(startdate__range=(start,end),enddate__range=(start,end), submitted_date__isnull = True).filter(developer_id= emp).values('startdate','enddate')
        tot = 0
        tot1 = 0
        xx=0
        xx1 = 0
        for i in pro:
            d_end = (i['enddate'])
            d_submitted = (i['submitted_date'])
            differ = (d_submitted - d_end).days
            if differ == 0:
                tot=0
            else:

                if d_submitted <= end:
                    diff = (d_submitted - d_end).days
                    cnt =  Event.objects.filter(start_time__gte=d_end,start_time__lte=d_submitted).values('start_time').count()
                    xx = diff - cnt
                else:
                    diff = (end - d_end).days
                    cnt =  Event.objects.filter(start_time__gte=d_end,start_time__lte=end).values('start_time').count()
                    xx = diff - cnt
            tot = tot + xx
                

        for x in pro_false:
            d_end = (x['enddate'])
            diff =  (end - d_end).days
            if diff <= 0:
                tot1=0
            cnt =  Event.objects.filter(start_time__gte=d_end,start_time__lte=end).values('start_time').count()
            xx1 = diff- cnt
            tot1 = tot1 + xx1

        a = tot + tot1


        return render(request,'BRadmin_projects_details.html', {'names':names,'a':a })
    else:
        return redirect('/')



# account payment head page
def accounts_paymenthead(request):
    if 'usernameacnt2' in request.session:
        if request.session.has_key('usernameacnt2'):
            usernameacnt2 = request.session['usernameacnt2']
        z = user_registration.objects.filter(id=usernameacnt2)
        return render(request, 'account_paymenthead.html', {'z': z})
    else:
        return redirect('/')

# add account payment head
def accounts_addpaymenthead(request):
    if 'usernameacnt2' in request.session:
        if request.session.has_key('usernameacnt2'):
            usernameacnt2 = request.session['usernameacnt2']
        z = user_registration.objects.filter(id=usernameacnt2)

        if request.method == "POST":
            pay_table = payment_head()
            pay_table.payment_head = request.POST.get('paymenthead')
            pay_table.description_paymenthead = request.POST.get('description')
            pay_table.save()
            msg_success = "paymenthead successfully created"
            return render(request, 'accounts_addpaymenthead.html', {'z': z, 'msg_success':msg_success})
        else:
            return render(request, 'accounts_addpaymenthead.html', {'z': z})
    else:
        return redirect('/')


# view account payment head
def accounts_viewpaymenthead(request):
    if 'usernameacnt2' in request.session:
        if request.session.has_key('usernameacnt2'):
            usernameacnt2 = request.session['usernameacnt2']
        z = user_registration.objects.filter(id=usernameacnt2)
        vars = payment_head.objects.all().order_by('-id')
        if request.method == "POST":
            uid = request.POST.get('paymenthead')
            ext = payment_head.objects.get(id=uid)
            ext.delete()
            msg_success = "paymenthead deleted successfully"
            return render(request, 'accounts_viewpaymenthead.html', {'z': z, 'msg_success':msg_success})
        else:
            return render(request, 'accounts_viewpaymenthead.html', {'z': z, 'vars':vars})
    else:
        return redirect('/')

#  account income page
def accounts_income(request):
    if 'usernameacnt2' in request.session:
        if request.session.has_key('usernameacnt2'):
            usernameacnt2 = request.session['usernameacnt2']
        z = user_registration.objects.filter(id=usernameacnt2)
        return render(request, 'accounts_income.html', {'z': z})
    else:
        return redirect('/')

# add account income
def accounts_addincome(request):
    if 'usernameacnt2' in request.session:
        if request.session.has_key('usernameacnt2'):
            usernameacnt2 = request.session['usernameacnt2']
        z = user_registration.objects.filter(id=usernameacnt2)
        dep = department.objects.all()
        pay_head = payment_head.objects.all()
        if request.method == "POST":
            income_tab = income()
            income_tab.pay_date = request.POST.get('paydate')
            income_tab.party_name = request.POST.get('pay_name')
            income_tab.amount = request.POST.get('pay_amount')
            income_tab.pay_method = request.POST.get('pay_method')
            income_tab.pay_description = request.POST.get('pay_description')
            income_tab.department_id = request.POST.get('pay_department')
            income_tab.payment_head_id = request.POST.get('pay_type')
            income_tab.save()
            msg_success = "Income added successfully"
            return render(request, 'accounts_addincome.html', {'z': z, 'msg_success':msg_success})

        return render(request, 'accounts_addincome.html', {'z': z, 'pay_head':pay_head,'dep':dep })
    else:
        return redirect('/')


# add account view all income
def accounts_viewallincome(request):
    if 'usernameacnt2' in request.session:
        if request.session.has_key('usernameacnt2'):
            usernameacnt2 = request.session['usernameacnt2']
        z = user_registration.objects.filter(id=usernameacnt2)
        
        inc = income.objects.all().order_by('-id')
        return render(request, 'accounts_viewallincome.html', {'z': z, 'inc':inc})
    else:
        return redirect('/')



# add account filter income
def accounts_filterincome(request):
    if 'usernameacnt2' in request.session:
        if request.session.has_key('usernameacnt2'):
            usernameacnt2 = request.session['usernameacnt2']
        z = user_registration.objects.filter(id=usernameacnt2)
        
        dep = department.objects.all()
        return render(request, 'accounts_filterincome.html', {'z': z, 'dep':dep})
    else:
        return redirect('/')



# add account filter income ajax
def accounts_filterincome_ajax(request):
        dept_id = request.GET.get('dept_id')
        fdate = request.GET.get('fdate')
        tdate = request.GET.get('tdate')

        start = datetime.strptime(fdate, '%Y-%m-%d').date()
        end = datetime.strptime(tdate, '%Y-%m-%d').date()
        inc = income.objects.filter(pay_date__range=(start,end)).filter(department_id=dept_id)
        
        
        tot = 0
        tot_inc = income.objects.filter(pay_date__range=(start,end)).filter(department_id=dept_id).values('amount')
        for x in tot_inc:
            tot = tot + int(x['amount'])

        return render(request, 'accounts_filterincome_ajax.html', {'inc':inc,'tot':tot })




# Bradmin_income
def BRadmin_income(request):
    if 'Adm_id' in request.session:
        if request.session.has_key('Adm_id'):
            Adm_id = request.session['Adm_id']
        else:
            return redirect('/')
        Adm = user_registration.objects.filter(id=Adm_id)
        inc_cont = income.objects.filter(pay_status=0).count()
        return render(request, 'BRadmin_income.html', {'Adm': Adm, 'inc_cont':inc_cont})
    else:
        return redirect('/')


# Bradmin view all income
def BRadmin_viewallincome(request):
    if 'Adm_id' in request.session:
        if request.session.has_key('Adm_id'):
            Adm_id = request.session['Adm_id']
        else:
            return redirect('/')
        Adm = user_registration.objects.filter(id=Adm_id)
        
        inc = income.objects.all().order_by('-id')
        return render(request, 'BRadmin_viewallincome.html', {'Adm': Adm, 'inc':inc})
    else:
        return redirect('/')


# Bradmin view all pending income
def BRadmin_pendingincome(request):
    if 'Adm_id' in request.session:
        if request.session.has_key('Adm_id'):
            Adm_id = request.session['Adm_id']
        else:
            return redirect('/')
        Adm = user_registration.objects.filter(id=Adm_id)

        if request.method=="POST":
            uid = request.POST.get('pay_verify')
            inc = income.objects.get(id=uid)
            inc.pay_status = 1
            inc.save()
            msg_success = "Payment verified"
            return render(request, 'accounts_viewpaymenthead.html', {'Adm': Adm, 'msg_success':msg_success})
            
        else:
            inc = income.objects.filter(pay_status=0)
            return render(request, 'BRadmin_pendingincome.html', {'Adm': Adm, 'inc':inc})
    else:
        return redirect('/')


# Bradmin search income
def BRadmin_searchincome(request):
    if 'Adm_id' in request.session:
        if request.session.has_key('Adm_id'):
            Adm_id = request.session['Adm_id']
        else:
            return redirect('/')
        Adm = user_registration.objects.filter(id=Adm_id)

        dep = department.objects.all()
        return render(request, 'BRadmin_searchincome.html', {'Adm': Adm, 'dep':dep})
    else:
        return redirect('/')



# add account filter income ajax
def BRadmin_filterincome_ajax(request):
    dept_id = request.GET.get('dept_id')
    fdate = request.GET.get('fdate')
    tdate = request.GET.get('tdate')

    start = datetime.strptime(fdate, '%Y-%m-%d').date()
    end = datetime.strptime(tdate, '%Y-%m-%d').date()
    inc = income.objects.filter(pay_date__range=(start,end)).filter(department_id=dept_id)
    
    
    tot = 0
    tot_inc = income.objects.filter(pay_date__range=(start,end)).filter(department_id=dept_id).values('amount')
    for x in tot_inc:
        tot = tot + int(x['amount'])

    return render(request, 'BRadmin_searchincome_ajax.html', {'inc':inc,'tot':tot })


# accounts main expences
def accounts_mainexpenses(request):

    if 'usernameacnt2' in request.session:
        if request.session.has_key('usernameacnt2'):
            usernameacnt2 = request.session['usernameacnt2']
        z = user_registration.objects.filter(id=usernameacnt2)
        
        return render(request, 'accounts_mainexpenses.html', {'z': z})
    else:
        return redirect('/')



# add account filter income
def accounts_salaryexpense(request):
    if 'usernameacnt2' in request.session:
        if request.session.has_key('usernameacnt2'):
            usernameacnt2 = request.session['usernameacnt2']
        z = user_registration.objects.filter(id=usernameacnt2)
        
        dep = department.objects.all()
        return render(request, 'accounts_salaryexpense.html', {'z': z, 'dep':dep})
    else:
        return redirect('/')


def accounts_salaryexpense_ajax(request):

    dept_id = request.GET.get('dept_id')
    fdate = request.GET.get('fdate')
    tdate = request.GET.get('tdate')

    start = datetime.strptime(fdate, '%Y-%m-%d').date()
    end = datetime.strptime(tdate, '%Y-%m-%d').date()

    inc = acntspayslip.objects.filter(fromdate__range=(start,end)).filter(department_id=dept_id)
    
    
    conf = 0
    net_sal = 0
    tot_sum = 0
    tot_inc = acntspayslip.objects.filter(fromdate__range=(start,end)).filter(department_id=dept_id).values('basic_salary','net_salary','hra','incentives', 'conveyns', 'other_allovance')
    for x in tot_inc:
        conf = conf + int(x['basic_salary']) + int(x['hra']) + int(x['other_allovance']) + int(x['conveyns'])
        net_sal = net_sal + int(x['net_salary'])
        
    tot_sum = conf - net_sal

    return render(request, 'accounts_salaryexpense_ajax.html', {'inc':inc,'conf':conf, 'net_sal':net_sal, 'tot_sum':tot_sum })




# BRadmin main expences
def BRadmin_mainexpenses(request):

    if 'Adm_id' in request.session:
        if request.session.has_key('Adm_id'):
            Adm_id = request.session['Adm_id']
        else:
            return redirect('/')

        Adm = user_registration.objects.filter(id=Adm_id)
        
        return render(request, 'BRadmin_mainexpenses.html', {'Adm': Adm})
    else:
        return redirect('/')



# BRadmin filter income
def BRadmin_salaryexpense(request):
    if 'Adm_id' in request.session:
        if request.session.has_key('Adm_id'):
            Adm_id = request.session['Adm_id']
        else:
            return redirect('/')

        Adm = user_registration.objects.filter(id=Adm_id)
        
        dep = department.objects.all()
        return render(request, 'BRadmin_salaryexpense.html', {'Adm': Adm, 'dep':dep})
    else:
        return redirect('/')


def verify_all_income(request):
    if 'Adm_id' in request.session:
        if request.session.has_key('Adm_id'):
            Adm_id = request.session['Adm_id']
        else:
            return redirect('/')
        Adm = user_registration.objects.filter(id=Adm_id)
        ver = income.objects.filter(pay_status=0).update(pay_status=1)

        msg_success = "verify All Income successfully"
        return render(request, 'BRadmin_pendingincome.html', {'Adm': Adm, 'msg_success':msg_success})
    else:
        return redirect('/')