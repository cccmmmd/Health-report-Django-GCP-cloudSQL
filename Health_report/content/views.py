from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Report



def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render({}, request))

def add(request):
  template = loader.get_template('add.html') 
  return HttpResponse(template.render({}, request)) 

def select(request):
    reports = Report.objects.all().values()
    template = loader.get_template('select.html') 
    context = {
        'reports': reports
    }
    return HttpResponse(template.render(context, request)) 

def addreport(request):
    report_name = request.POST['report_name'] 
    report_year = request.POST['report_year'] 
    blood_pressure = request.POST['blood_pressure'] 
    pulse = request.POST['pulse'] 
    glucose_ac = request.POST['glucose_ac'] 
    hba1c = request.POST['hba1c'] 
    t_cho = request.POST['t_cho'] 
    tg = request.POST['tg'] 
    hdl_c = request.POST['hdl_c'] 
    ldl_c = request.POST['ldl_c'] 
    abstract = request.POST['abstract'] 
    diastolic_pressure = blood_pressure.split("/")[0]
    systolic_pressure = blood_pressure.split("/")[1]

    report = Report(
        report_name = report_name,
        report_year = report_year,
        diastolic_pressure = diastolic_pressure,
        systolic_pressure = systolic_pressure,
        pulse = pulse,
        glucose_ac = glucose_ac,
        hba1c = hba1c,
        t_cho = t_cho,
        tg = tg,
        hdl_c = hdl_c,
        ldl_c = ldl_c,
        abstract = abstract,
    )
    report.save()
    # member = Members(firstname=x, lastname=y) 
    # member.save() 
    return HttpResponseRedirect(reverse('select'))


def analysis(request):
  template = loader.get_template('analysis.html') 
  return HttpResponse(template.render({}, request)) 

