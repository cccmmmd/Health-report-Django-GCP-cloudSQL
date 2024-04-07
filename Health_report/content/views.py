from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Report, User, Arg
from .modules import gemini
import json


excloud_list = ['csrfmiddlewaretoken', 'report_name', 'report_year', 'blood_pressure', 'created_at' ]
def index(request):
    reports = Report.objects.all().values()
    template = loader.get_template('index.html')
    problem_report = 0
    count_problem = {}
    latest_year = 0
    for r in reports:
        if int(r['report_year']) > latest_year:
            latest_year = int(r['report_year'])
        if(r['problems'] != ''):
            problem_report += 1
        
        temp = r['problems'].split(',')
        for t in temp:
            if t != '':
                if t not in count_problem:
                    count_problem[t] = 1
                else:
                    count_problem[t] += 1
    context = {
        'latest_year': latest_year,
        'count_problem': json.dumps(count_problem),
        'reports_len': reports.count(),
        'problem_report':  problem_report,
    }
    return HttpResponse(template.render(context, request))

def create(request):
    if request.session.get('report_data'):
        del request.session['report_data']
    if request.session.get('problem_values'):
        del request.session['problem_values']


    template = loader.get_template('add.html') 
    return HttpResponse(template.render({}, request)) 

def select(request):
    reports = Report.objects.all().values().order_by('-report_year')
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
    arg = Arg.objects.all().values() 
    print(arg)
    report_data = {}
    for p in request.POST:
        report_data[p] = request.POST[p]
    report_data['diastolic_pressure'] = request.POST['blood_pressure'].split("/")[1]
    report_data['systolic_pressure'] = request.POST['blood_pressure'].split("/")[0]
    problem_values = {}
    for r in report_data:
        for a in arg:
            if (r == a['name'] == 'hba1c'):
                if((a['max'] and float(report_data[r]) > a['max']) or
                    (a['min'] and float(report_data[r]) < a['min'])):

                    print(r,'@@@', a)
                    problem_values[r] = (float(report_data[r]))
            else:   
                if(r == a['name']):
                    if((a['max'] and int(float(report_data[r])) > a['max']) or 
                    (a['min'] and int(float(report_data[r])) < a['min']) or 
                       (a['m_min'] and int(float(report_data[r])) < a['m_min'])):
                    # (a['f_min'] and int(float(report_data[r])) < a['f_min'])):
                        problem_values[r] =int(float(report_data[r]))

    prompt = ['You are a medical report assistant who use Traditional Chinese. You need to read the following values from the health examination report. They are abnormal:']
    for r,i in problem_values.items():
        if r not in excloud_list :
            prompt.append(f'{r} is {i}.')
    prompt.append('Please give me overall health improvement suggestions for diet and exercise based on the above abnormal values. No need to display abnormal values')
    prompt.append('Must use Traditional Chinese.')
    
    try:                     
        result = gemini.Gemini().askGemini(prompt) 
        report_data['abstract'] = result.text
    except:                   
        report_data['abstract'] = '抱歉！無法順利生成摘要'
    
    request.session['report_data'] = report_data
    request.session['problem_values'] = problem_values
    
    return HttpResponseRedirect(reverse('one_result'))


def one_result(request):    
    template = loader.get_template('one_result.html')  
    report = request.session['report_data']
    problem = request.session['problem_values']
    args = Arg.objects.all().values() 

    units = {}
    normal = {}
    for a in args:
        st = '正常值為'
        units[a['name']] = a['unit']
        if a['max']: st += '低於' + str(a['max'])
        if a['min']: st += '高於' + str(a['min'])
        if a['m_min']: st += '男性高於' + str(a['m_min'])
        if a['f_min']: st += '女性高於' + str(a['f_min'])
        normal[a['name']] = st

    
    context = {
        'report': report,
        'problem': problem,
        'units': units,
        'normal': normal
    }
    return HttpResponse(template.render(context, request)) 

def savereport(request):
    report_data = request.session['report_data']
    problem = request.session['problem_values']
    arg = Arg.objects.all().values() 
    save_problem = ''
    for p in problem:
        for a in arg:
            if p == a['name']:
                save_problem += a['c_name'] + ','
   
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
        problems = save_problem,
        abstract = report_data['abstract'],
    )
    report.save()
    del request.session['report_data']
    del request.session['problem_values']
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

def login(request):
    template = loader.get_template('login.html') 
    return HttpResponse(template.render({}, request)) 