from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Report, User



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
 
def selectreport(request):
    selected_reports = []
    reports = Report.objects.all().values()
    for r in reports:
        if request.POST.get('report_%s' % r['id']):
            selected_reports.append(r)

    request.session['selected_reports'] = selected_reports
   
    return HttpResponseRedirect(reverse('analysis'))

def addreport(request):
    report_data = {}
    for p in request.POST:
        report_data[p] = request.POST[p]
    report_data['diastolic_pressure'] = request.POST['blood_pressure'].split("/")[1]
    report_data['systolic_pressure'] = request.POST['blood_pressure'].split("/")[0]
    request.session['report_data'] = report_data
    
    # member = Members(firstname=x, lastname=y) 
    # member.save() 
    return HttpResponseRedirect(reverse('one_result'))


def one_result(request):    
    template = loader.get_template('one_result.html')
    context = {
        'reports': request.session['report_data']
    }
    return HttpResponse(template.render(context, request)) 

def savereport(request):
    one_report = request.session['report_data']
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
    return HttpResponseRedirect(reverse('create'))


def analysis(request):
    template = loader.get_template('analysis.html') 
    selected_reports = request.session['selected_reports']
    context = {
        'selected_reports': selected_reports
    }
    return HttpResponse(template.render(context, request)) 

