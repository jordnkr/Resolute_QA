from django.core import serializers
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.views.decorators.csrf import csrf_exempt
import xml.etree.ElementTree as ET
from django.utils.dateparse import parse_datetime
from django.utils.timezone import is_aware, make_aware
from .models import Environment, Project, Suite, ProjectEnvironment, SuiteRun, Bug, TestResult, Error, Test

def index(request):
    project_list = Project.objects.all()
    context = {'project_list': project_list}
    return render(request, 'resoluteqa/index.html', context)

def uploadresults(request, projenv_id):
    projectenvironment = get_object_or_404(ProjectEnvironment, pk=projenv_id)
    suite_list = Suite.objects.filter(project_environment_id=projenv_id).order_by('suite_name')

    # Used for navbar daily results links
    suite_runs = []
    for suite in suite_list:
        try:
            suite_runs.append(SuiteRun.objects.filter(suite_id=suite.id).latest('start_time'))
        except Exception:
            pass # Do nothing, suite_runs will stay empty and page will load correctly

    context = {
        'projectenvironment': projectenvironment,
        'suite_runs': suite_runs
    }

    return render(request, 'resoluteqa/upload.html', context)

def summary(request, projenv_id):
    projectenvironment = get_object_or_404(ProjectEnvironment, pk=projenv_id)
    suite_list = Suite.objects.filter(project_environment_id=projenv_id).order_by('suite_name')

    passed_tests = 0
    failed_tests = 0
    inconclusive_tests = 0
    ignored_tests = 0
    total_tests = 0
    pass_percentage = 0
    fail_percentage = 0

    suite_runs = []
    for suite in suite_list:
        try:
            run = SuiteRun.objects.filter(suite_id=suite.id).latest('start_time')
            passed_tests += run.passed_tests
            failed_tests += run.failed_tests
            inconclusive_tests += run.inconclusive_tests
            ignored_tests += run.ignored_tests
            total_tests += run.total_tests
            suite_runs.append(run)
        except Exception:
            pass # Do nothing, suite_runs will stay empty and page will load correctly


    if total_tests > 0:
        pass_percentage = round(100 * (float(passed_tests) / total_tests), 2)
        fail_percentage = round(100 - pass_percentage, 2)

    context = {
        'projectenvironment': projectenvironment,
        'suite_list': suite_list,
        'suite_runs': suite_runs,
        'passed_tests': passed_tests,
        'failed_tests': failed_tests,
        'inconclusive_tests': inconclusive_tests,
        'ignored_tests': ignored_tests,
        'total_tests': total_tests,
        'pass_percentage': pass_percentage,
        'fail_percentage': fail_percentage
    }
    return render(request, 'resoluteqa/summary.html', context)

@csrf_exempt
def dailyresults(request, suite_run_id):
    request_suite_run = get_object_or_404(SuiteRun, pk=suite_run_id)
    request_suite = Suite.objects.get(id=request_suite_run.suite.id)
    suite_list = Suite.objects.filter(project_environment_id=request_suite.project_environment.id).order_by('suite_name')
    historical_suite_runs = SuiteRun.objects.filter(suite__id=request_suite.id).order_by('-insert_date')
    test_results = TestResult.objects.filter(suite_run__id=suite_run_id)
    bug_list = Bug.objects.filter(test__suite__project_environment_id=request_suite.project_environment.id).distinct()

    # Used for navbar daily results links
    suite_runs = []
    for suite in suite_list:
        suite_runs.append(SuiteRun.objects.filter(suite_id=suite.id).latest('start_time'))

    context = {
        'request_suite_run': request_suite_run,
        'suite': request_suite,
        'suite_list': suite_list,
        'historical_suite_runs': historical_suite_runs,
        'test_results': test_results,
        'suite_runs': suite_runs,
        'bug_list': bug_list
    }
    return render(request, 'resoluteqa/dailyresults.html', context)

def bugs(request, projenv_id):
    projectenvironment = get_object_or_404(ProjectEnvironment, pk=projenv_id)
    suite_list = Suite.objects.filter(project_environment_id=projenv_id).order_by('suite_name')
    bug_list = Bug.objects.filter(test__suite__project_environment_id=projenv_id).distinct()

    # Used for navbar daily results links
    suite_runs = []
    for suite in suite_list:
        try:
            suite_runs.append(SuiteRun.objects.filter(suite_id=suite.id).latest('start_time'))
        except Exception:
            pass # Do nothing. suite_runs will remain blank and page will load without data

    context = {
        'projectenvironment': projectenvironment,
        'suite_list': suite_list,
        'bug_list': bug_list,
        'suite_runs': suite_runs
    }
    return render(request, 'resoluteqa/bugs.html', context)

def testbugs(request, test_id):
    if request.method == 'GET':
        test = Test.objects.get(id=test_id)
        #bug_list = Bug.objects.filter(testbug__test__id=test_id)
        bug_list = test.bugs.all()
        bug_list = serializers.serialize("json", bug_list)
        data = {
            "bug_list": bug_list
        }
        return JsonResponse(data)

def projectbugs(request, projenv_id):
    if request.method == 'GET':
        bug_list = Bug.objects.filter(test__suite__project_environment_id=projenv_id).distinct().order_by('source_control_id')
        bug_list = serializers.serialize("json", bug_list)
        data = {
            "bug_list": bug_list
        }
        return JsonResponse(data)

def individualresult(request, test_result_id):
    if request.method == 'GET':
        result = TestResult.objects.filter(id=test_result_id)
        error_list = result[0].error_set.all()
        result = serializers.serialize("json", result)
        error_list = serializers.serialize("json", error_list)
        data = {
            "result": result,
            "error_list": error_list
        }
        return JsonResponse(data)

@csrf_exempt
def bug_create(request):
    try:
        if request.method == "POST":
            bug = Bug.objects.create(source_control_id=request.POST["source_control_id"], source_control=request.POST["source_control"], title=request.POST["title"], url=request.POST["url"])
            test_ids = request.POST.getlist("test_ids[]")
            for test_id in test_ids:
                test = Test.objects.get(id=test_id)
                test.bugs.add(bug)
            return JsonResponse({'success': True})
        else:
            return JsonResponse({'error': True})
    except Exception as e:
        return JsonResponse({'error': True})

@csrf_exempt
def bug_update(request, bug_id):
    try:
        if request.method == "POST":
            bug = Bug.objects.get(id=bug_id)
            bug.source_control_id = request.POST["source_control_id"]
            bug.title = request.POST["title"]
            bug.source_control = request.POST["source_control"]
            bug.url = request.POST["url"]
            bug.save()
            return JsonResponse({'success': True})
        else:
            return JsonResponse({'error': True})
    except Exception as e:
        return JsonResponse({'error': True})

@csrf_exempt
def bug_delete(request, bug_id):
    try:
        if request.method == "POST":
            bug = Bug.objects.get(id=bug_id)
            bug.delete()
            return JsonResponse({'success': True})
        else:
            return JsonResponse({'error': True})
    except Exception as e:
        return JsonResponse({'error': True})

@csrf_exempt
def bug_add(request):
    try:
        if request.method == "POST":
            bug_id = request.POST["bug_id"]
            test_ids = request.POST.getlist("test_ids[]")
            for test_id in test_ids:
                bug = Bug.objects.get(id=bug_id)
                test = Test.objects.get(id=test_id)
                test.bugs.add(bug)
            return JsonResponse({'success': True})
        else:
            return JsonResponse({'error': True})
    except Exception as e:
        return JsonResponse({'error': True})

@csrf_exempt
def bug_remove(request, bug_id, test_id):
    try:
        if request.method == "POST":
            bug = Bug.objects.get(id=bug_id)
            test = Test.objects.get(id=test_id)
            test.bugs.remove(bug)
            return JsonResponse({'success': True, 'bugCount':test.bugs.count()})
        else:
            return JsonResponse({'error': True})
    except Exception as e:
        return JsonResponse({'error': True})

@csrf_exempt
def upload_mstest(request, projenv_id):
    xmlfile = request.FILES.get('resultfile')
    if xmlfile is not None:
        upload_project_name = request.POST.get('project')
        upload_environment = request.POST.get('environment')
        upload_suite_name = request.POST.get('suite_name')

        tree = ET.parse(xmlfile)
        for test_run in tree.iter('TestRun'):
            test_settings = test_run.find('TestSettings')
            result_summary = test_run.find('ResultSummary')
            test_definitions = test_run.find('TestDefinitions')
            results = test_run.find('Results')

            # SUITE INFO
            project, project_created = Project.objects.get_or_create(project_name=upload_project_name)
            environment, environment_created = Environment.objects.get_or_create(environment_name=upload_environment)
            projectenvironment, projenv_create = ProjectEnvironment.objects.get_or_create(
                project=project,
                environment=environment
            )
            description = test_settings.find('Description').text
            suite, suite_created = Suite.objects.get_or_create(
                project_environment=projectenvironment,
                suite_name=upload_suite_name,
                defaults={'description': description}
            )

            # SUITE_RUN INFO
            total_tests = int(result_summary.find('Counters').attrib['total'])
            executed_tests = int(result_summary.find('Counters').attrib['executed']) #doesn't go to the database. used for calculation only
            passed_tests = int(result_summary.find('Counters').attrib['passed'])
            failed_tests = int(result_summary.find('Counters').attrib['failed']) + int(result_summary.find('Counters').attrib['error'])
            inconclusive_tests = int(result_summary.find('Counters').attrib['inconclusive'])
            ignored_tests = int(result_summary.find('Counters').attrib['notExecuted'])
            result_precentage = 100 * (passed_tests/executed_tests)
            suite_start_time = get_aware_datetime(test_run.find('Times').attrib['start'])
            suite_end_time = get_aware_datetime(test_run.find('Times').attrib['finish'])
            total_execution_time = (suite_end_time-suite_start_time).total_seconds()/60 # store time in minutes
            suite_run = SuiteRun.objects.create(suite=suite, total_tests=total_tests, passed_tests=passed_tests, failed_tests=failed_tests, inconclusive_tests=inconclusive_tests, ignored_tests=ignored_tests, result_precentage=result_precentage, start_time=suite_start_time, end_time=suite_end_time, total_execution_time=total_execution_time)

            for test_result in results.iter('UnitTestResult'):
                # TEST INFO
                test_id = test_result.attrib['testId'] # not stored in database. Used to query other fields within the results file only.
                test_name = test_result.attrib['testName']
                test_category = '' #left blank for now
                unit_test = test_definitions.findall(".//UnitTest[@id='" + test_id + "']") # not stored in database. Used for other values only.
                class_name_path = unit_test[0].find('TestMethod').attrib['className'].split(',')[0] # not stored in database. Used for other values only.
                pathArray = class_name_path.rsplit('.', 1) # not stored in database. Used for other values only.
                class_name = pathArray[1]
                namespace = pathArray[0]
                test, test_created = Test.objects.get_or_create(
                    suite=suite,
                    test_name=test_name,
                    class_name=class_name,
                    namespace=namespace
                )

                # TEST_RESULT INFO
                result = test_result.attrib['outcome']
                host = test_result.attrib['computerName']
                test_start_time = get_aware_datetime(test_result.attrib['startTime'])
                test_end_time = get_aware_datetime(test_result.attrib['endTime'])
                test_total_execution_time = parse_seconds(test_result.attrib['duration']) # store time in seconds
                console_output = test_result.find('Output').find('StdOut').text
                tr = TestResult.objects.create(suite_run=suite_run, test=test, result=result, host=host, start_time=test_start_time, end_time=test_end_time, total_execution_time=test_total_execution_time, console_output=console_output)

                # ERROR INFO
                for error in test_result.find('Output').iter('ErrorInfo'):
                    error_message = error.find('Message').text
                    stack_trace = error.find('StackTrace').text
                    Error.objects.create(test_result=tr, error_message=error_message, stack_trace=stack_trace)

    fromForm = False #make form upload this value
    if fromForm:
        return redirect('resoluteqa:uploadresults', projenv_id)
    else:
        return JsonResponse({'success': True})

def get_aware_datetime(date_str):
    ret = parse_datetime(date_str)
    if not is_aware(ret):
        ret = make_aware(ret)
    return ret

def parse_seconds(time_str):
    h, m, s = time_str.split(':')
    return float(h) * 3600 + float(m) * 60 + float(s)
