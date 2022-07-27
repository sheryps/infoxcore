from django.http import request
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'index.html')

def profiledash(request):
    return render(request,'profiledash.html')

def Training(request):
    return render(request,'Training.html')

def trainingteam1(request):
    return render(request,'trainingteam1.html')
def trainerstable(request):
    return render(request,'trainerstable.html')
def topictable(request):
    return render(request,'topictable.html')
def completedtasktable(request):
    return render(request,'completedtasktable.html')
def trainingprofile(request):
    return render(request,'trainingprofile.html')
def traineestable(request):
    return render(request,'traineestable.html')      


def man_projects(request):
    return render(request,'man_projects.html')
def man_proj_list(request):
    return render(request,'man_proj_list.html')
def man_proj_det(request):
    return render(request,'man_proj_det.html')
def man_proj_mngrs(request):
    return render(request,'man_proj_mngrs.html')
def man_proj_mangrs1(request):
    return render(request,'man_proj_mangrs1.html')
def man_proj_mangrs2(request):
    return render(request,'man_proj_mangrs2.html')
def man_proj_cmpltd(request):
    return render(request,'man_proj_cmpltd.html')
def man_cmpltd_proj_det(request):
    return render(request,'man_cmpltd_proj_det.html')
def man_daily_report(request):
    return render(request,'man_daily_report.html')


def man_employees(request):
    return render(request,'man_employees.html')
def man_python(request):
    return render(request,'man_python.html')
def man_projectman(request):
    return render(request,'man_projectman.html')
def man_proname(request):
    return render(request,'man_proname.html')
def man_proinvolve(request):
    return render(request,'man_proinvolve.html')
def man_promanatten(request):
    return render(request,'man_promanatten.html')


def man_HRlist(request):
    return render(request,'man_HRlist.html')
def man_HRprofile(request):
    return render(request,'man_HRprofile.html')
def man_HRattendance(request):
    return render(request,'man_HRattendance.html')
def man_TLlist(request):
    return render(request,'man_TLlist.html')
def man_TLprofile(request):
    return render(request,'man_TLprofile.html')
def man_TLip(request):
    return render(request,'man_TLip.html')
def man_TLattendance(request):
    return render(request,'man_TLattendance.html')    


def MANViewTrainerprofile(request):
    return render(request,'MAN_View_Trainerprofile.html')
def MANViewCurrenttraineesoftrainer(request):
    return render(request,'MAN_View_Currenttraineesoftrainer.html')
def MANViewPrevioustraineesoftrainer(request):
    return render(request,'MAN_View_Previoustraineesoftrainer.html')
def ManViewCurrenttraineeprofile(request):
    return render(request,'MAN_View_Currenttraineeprofile.html')
def ManViewPrevioustraineeprofile(request):
    return render(request,'MAN_View_Previoustraineeprofile.html')
def ManViewCurrenttraineetasks(request):
    return render(request,'MAN_View_Currenttraineetasks.html')
def ManViewPrevioustraineetasks(request):
    return render(request,'MAN_View_Previoustraineetasks.html')
def ManViewTrainerattendance(request):
    return render(request,'MAN_View_Trainerattendance.html')
def ManViewCurrenttraineeattendance(request):
    return render(request,'MAN_View_Currenttraineeattendance.html')
def ManViewPrevioustraineeattendance(request):
    return render(request,'MAN_View_Previoustraineeattendance.html')
def MANViewTrainers(request):
    return render(request,'MAN_View_Trainers.html')      


def details(request):
    return render(request,'man_dev_details.html')
def man_dev_profile(request):
    return render(request,'man_dev_profile.html')
def invo_projects(request):
    return render(request,'man_dev_involvedprojects.html')
def dev_attendance (request):
    return render(request,'man_dev_attendance.html')


def MANReportedissue(request):
    return render(request, 'MANReportedissue.html')
def MANReportedissueTrainees(request):
    return render(request, 'MANReportedissueTrainees.html')   
def MANReportedissueTrainees1(request):
    return render(request, 'MANReportedissueTrainees1.html') 
def MANReportedissueTrainer(request):
    return render(request, 'MANReportedissueTrainer.html')   
def MANReportedissueTrainer1(request):
    return render(request, 'MANReportedissueTrainer1.html') 
def MANReportedissueProjectManager(request):
    return render(request, 'MANReportedissueProjectManager.html') 
def MANReportedissueProjectManager1(request):
    return render(request, 'MANReportedissueProjectManager1.html') 
def MANReportedissueTeamLeader(request):
    return render(request, 'MANReportedissueTeamLeader.html') 
def MANReportedissueTeamLeader1(request):
    return render(request, 'MANReportedissueTeamLeader1.html') 
def MANReportedissueDevelopers(request):
    return render(request, 'MANReportedissueDevelopers.html') 
def MANReportedissueDevelopers1(request):
    return render(request, 'MANReportedissueDevelopers1.html')     


def upcoming(request):
    return render(request,'upcomingprojects.html')
def tasks(request):
    return render(request,'tasks.html')
def viewprojectform(request):
    return render(request,'viewprojects.html')
def acceptedprojects(request):
    return render(request,'acceptedprojects.html')
def rejected(request):
    return render(request,'rejectedprojectes.html')
def givetask(request):
    return render(request,'givetask.html')
def currenttasks(request):
    return render(request,'currenttasks.html')    
def previoustasks(request):
    return render(request,'previoustasks.html')

#*****************************Registration**********************
def manindex(request):
    return render(request, 'manindex.html')

def man_registration(request):
    return render(request,'man_registration.html')

def man_registration_update(request):
    return render(request,'man_registration_update.html')

def man_registration_form(request):
    return render(request,'man_registration_form.html')

#*****************************Internship***********************

def man_internship_view(request):
    return render(request,'man_internship_view.html')

def man_internship(request):
    return render(request,'man_internship.html')

def man_internship_date(request):
    return render(request,'man_internship_date.html')

def internship(request):
    return render(request,'internship.html')

def man_internship_update(request):
    return render(request,'man_internship_update.html')

#*******************************Leave**************************

def man_leave(request):
    return render(request,'man_leave.html')

def leave(request):
    return render(request,'leave.html')

#*************************************************************************************************