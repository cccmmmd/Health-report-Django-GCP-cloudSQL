from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='add'), 
    path('create/addreport/', views.addreport, name='addreport'), 
    path('one_result/', views.one_result, name='one_result'), 
    path('one_result/savereport/', views.savereport, name='savereport'), 
    path('reports/', views.select, name='select'), 
    path('reports/selectreport/', views.selectreport, name='selectreport'), 
    path('analysis/', views.analysis, name='analysis'), 
    path('assistant/', views.assistant, name='assistant'), 
    path('login/', views.login, name='login'), 
]