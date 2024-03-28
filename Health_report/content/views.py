from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Report, User, Arg
from .modules import gemini
import json


excloud_list = ['csrfmiddlewaretoken', 'report_name', 'report_year', 'blood_pressure', 'created_at' ]
def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render({}, request))

def add(request):
    if request.session.get('report_data'):
        del request.session['report_data']
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

    request.session['selected_reports'] = json.dumps(selected_reports, indent = 4, sort_keys = True, default = str)
    return HttpResponseRedirect(reverse('analysis'))

def addreport(request):
    global excloud_list
    report_data = {}
    for p in request.POST:
        report_data[p] = request.POST[p]
    report_data['diastolic_pressure'] = request.POST['blood_pressure'].split("/")[1]
    report_data['systolic_pressure'] = request.POST['blood_pressure'].split("/")[0]
    prompt = ['You are a medical report assistant who use Traditional Chinese. You need to read the following values from the health examination:']
    for r, i in report_data.items():
        if r not in excloud_list :
            prompt.append(f'{r} is {i}.')
    prompt.append('Check whether the values are normal based on the above values. If there are any abnormal values, please give me overall health improvement suggestions for diet and exercise.')
    prompt.append('Must use Traditional Chinese.')
    try:                     
        result = gemini.Gemini().askGemini(prompt) 
        report_data['abstract'] = result.text
    except:                   
        report_data['abstract'] = '抱歉！無法順利生成摘要'

    request.session['report_data'] = report_data
    
    return HttpResponseRedirect(reverse('one_result'))


def one_result(request):    
    template = loader.get_template('one_result.html')    
    context = {
        'reports': request.session['report_data']
    }
    return HttpResponse(template.render(context, request)) 

def savereport(request):
    report_data = request.session['report_data']
    report = Report(
        report_name = report_data['report_name'],
        report_year = report_data['report_year'],
        diastolic_pressure = report_data['diastolic_pressure'],
        systolic_pressure = report_data['systolic_pressure'],
        pulse = report_data['pulse'],
        glucose_ac = report_data['glucose_ac'],
        hba1c = report_data['hba1c'],
        t_cho = report_data['t_cho'],
        tg = report_data['tg'],
        hdl_c = report_data['hdl_c'],
        ldl_c = report_data['ldl_c'],
        abstract = report_data['abstract'],
    )
    report.save()
    del request.session['report_data']
    return HttpResponseRedirect(reverse('add'))


def analysis(request):

    report_summary = ''
    template = loader.get_template('analysis.html') 
    selected_reports = request.session['selected_reports']
    json_reports = json.loads(selected_reports)
    prompt = ['您是使用繁體中文的醫療報告助理。 對以下健康報告的「建議」部分進行重點總結：']
    for jr in json_reports:
        prompt.append(jr['abstract'])
    prompt.append('只需要對「建議」部分進行重點總結')
    prompt.append('一定要用繁體中文！')
    # print(prompt)
    try:                     
        result = gemini.Gemini().askGemini(prompt) 
        report_summary = result.text
    except:                   
        report_summary = '抱歉！無法順利生成摘要'

    context = {
        'selected_reports': selected_reports,
        'reports': json_reports,
        'report_summary': report_summary

    }
    return HttpResponse(template.render(context, request)) 

def assistant(request):
    template = loader.get_template('assistant.html') 
    return HttpResponse(template.render({}, request)) 