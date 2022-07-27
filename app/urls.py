
from django.urls import re_path
from .import views

urlpatterns = [
    re_path(r'^index$', views.index, name='index'),
    re_path(r'^$', views.profiledash,name='profiledash'),
    re_path(r'^Training$', views.Training,name='Training'),
    re_path(r'^trainingteam1$', views.trainingteam1,name='trainingteam1'),
    re_path(r'^trainerstable$', views.trainerstable,name='trainerstable'),
    re_path(r'^topictable$', views.topictable,name='topictable'),
    re_path(r'^completedtasktable$', views.completedtasktable,name='completedtasktable'),
    re_path(r'^trainingprofile$', views.trainingprofile,name='trainingprofile'),
    re_path(r'^traineestable$', views.traineestable,name='traineestable'),

    re_path(r'^man_projects$', views.man_projects, name='man_projects'),
    re_path(r'^man_proj_list$', views.man_proj_list, name='man_proj_list'),
    re_path(r'^man_proj_det$', views.man_proj_det, name='man_proj_det'),
    re_path(r'^man_proj_mngrs$', views.man_proj_mngrs, name='man_proj_mngrs'),
    re_path(r'^man_proj_mangrs1$', views.man_proj_mangrs1, name='man_proj_mangrs1'),
    re_path(r'^man_proj_mangrs2$', views.man_proj_mangrs2, name='man_proj_mangrs2'),
    re_path(r'^man_proj_cmpltd$', views.man_proj_cmpltd, name='man_proj_cmpltd'),
    re_path(r'^man_cmpltd_proj_det$', views.man_cmpltd_proj_det, name='man_cmpltd_proj_det'),
    re_path(r'^man_daily_report$', views.man_daily_report, name='man_daily_report'),


    re_path(r'^man_employees$', views.man_employees, name='man_employees'),
    re_path(r'^man_python$', views.man_python, name='man_python'),
    re_path(r'^man_projectman$', views.man_projectman, name='man_projectman'),
    re_path(r'^man_proname$', views.man_proname, name='man_proname'),
    re_path(r'^man_proinvolve$', views.man_proinvolve, name='man_proinvolve'),
    re_path(r'^man_promanatten$', views.man_promanatten, name='man_promanatten'),

     re_path(r'^man_HRattendance$', views.man_HRattendance, name='man_HRattendance'),
    re_path(r'^man_HRlist$', views.man_HRlist, name='man_HRlist'),
    re_path(r'^man_HRprofile$', views.man_HRprofile, name='man_HRprofile'),
    re_path(r'^man_TLattendance$', views.man_TLattendance, name='man_TLattendance'),
    re_path(r'^man_TLip$', views.man_TLip, name='man_TLip'),
    re_path(r'^man_TLlist$', views.man_TLlist, name='man_TLlist'),
    re_path(r'^man_TLprofile$', views.man_TLprofile, name='man_TLprofile'),

    re_path(r'^MANViewTrainerprofile$', views.MANViewTrainerprofile, name='MANViewTrainerprofile'),
    re_path(r'^MANViewCurrenttraineesoftrainer$', views.MANViewCurrenttraineesoftrainer, name='MANViewCurrenttraineesoftrainer'),
    re_path(r'^MANViewPrevioustraineesoftrainer$', views.MANViewPrevioustraineesoftrainer, name='MANViewPrevioustraineesoftrainer'),
    re_path(r'^ManViewCurrenttraineeprofile$', views.ManViewCurrenttraineeprofile, name='ManViewCurrenttraineeprofile'),
    re_path(r'^ManViewPrevioustraineeprofile$', views.ManViewPrevioustraineeprofile, name='ManViewPrevioustraineeprofile'),
    re_path(r'^ManViewCurrenttraineetasks$', views.ManViewCurrenttraineetasks, name='ManViewCurrenttraineetasks'),
    re_path(r'^ManViewPrevioustraineetasks$', views.ManViewPrevioustraineetasks, name='ManViewPrevioustraineetasks'),
    re_path(r'^ManViewTrainerattendance$', views.ManViewTrainerattendance, name='ManViewTrainerattendance'),
    re_path(r'^ManViewCurrenttraineeattendance$', views.ManViewCurrenttraineeattendance, name='ManViewCurrenttraineeattendance'),
    re_path(r'^ManViewPrevioustraineeattendance$', views.ManViewPrevioustraineeattendance, name='ManViewPrevioustraineeattendance'),
    re_path(r'^MANViewTrainers$', views.MANViewTrainers, name='MANViewTrainers'),


    re_path(r'^details$',views.details,name='details'),
    re_path(r'^man_dev_profile$',views.man_dev_profile,name='man_dev_profile'),
    re_path(r'^invo_projects$',views.invo_projects,name='invo_projects'),
    re_path(r'^dev_attendance$',views.dev_attendance,name='dev_attendance'),


    re_path(r'^MANReportedissue$', views.MANReportedissue, name='MANReportedissue'),
    re_path(r'^MANReportedissueTrainees$', views.MANReportedissueTrainees, name='MANReportedissueTrainees'),
    re_path(r'^MANReportedissueTrainees1$', views.MANReportedissueTrainees1, name='MANReportedissueTrainees1'),
    re_path(r'^MANReportedissueTrainer$', views.MANReportedissueTrainer, name='MANReportedissueTrainer'),
    re_path(r'^MANReportedissueTrainer1$', views.MANReportedissueTrainer1, name='MANReportedissueTrainer1'),
    re_path(r'^MANReportedissueProjectManager$', views.MANReportedissueProjectManager, name='MANReportedissueProjectManager'),
    re_path(r'^MANReportedissueProjectManager1$', views.MANReportedissueProjectManager1, name='MANReportedissueProjectManager1'),
    re_path(r'^MANReportedissueTeamLeader$', views.MANReportedissueTeamLeader, name='MANReportedissueTeamLeader'),
    re_path(r'^MANReportedissueTeamLeader1$', views.MANReportedissueTeamLeader1, name='MANReportedissueTeamLeader1'),
    re_path(r'^MANReportedissueDevelopers$', views.MANReportedissueDevelopers, name='MANReportedissueDevelopers'),
    re_path(r'^MANReportedissueDevelopers1$', views.MANReportedissueDevelopers1, name='MANReportedissueDevelopers1'),


    re_path(r'^upcoming$', views.upcoming, name='upcoming'),
    re_path(r'^tasks$', views.tasks, name='tasks'),
    re_path(r'^viewprojectform$', views.viewprojectform, name='viewprojectform'),
    re_path(r'^acceptedprojects$', views.acceptedprojects, name='acceptedprojects'),
    re_path(r'^rejected$', views.rejected, name='rejected'),
    re_path(r'^givetask$', views.givetask, name='givetask'),
    re_path(r'^currenttasks$', views.currenttasks, name='currenttasks'),
    re_path(r'^previoustasks$', views.previoustasks, name='previoustasks'),
    


     re_path(r'^$', views.manindex, name="manindex"),
    re_path(r'^man_registration$', views.man_registration, name="man_registration"),
    re_path(r'^man_registration_update$', views.man_registration_update, name="man_registration_update"),
    re_path(r'^man_registration_form$', views.man_registration_form, name="man_registration_form"),
    
    re_path(r'^man_internship_view$', views.man_internship_view, name="man_internship_view"),
    re_path(r'^man_internship$', views.man_internship, name="man_internship"),
    re_path(r'^man_internship_date$', views.man_internship_date, name="man_internship_date"),
    re_path(r'^man_internship_update$', views.man_internship_update, name="man_internship_update"),
    re_path(r'^internship$', views.internship, name="internship"),

    re_path(r'^man_leave$', views.man_leave, name="man_leave"),
    re_path(r'^leave$', views.leave, name="leave"),
]

