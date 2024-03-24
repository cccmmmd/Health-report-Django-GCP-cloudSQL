from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.add, name='add'), 
    path('add/addreport/', views.addreport, name='addreport'), 
    path('select/', views.select, name='select'), 
    path('analysis/', views.analysis, name='analysis'), 
]