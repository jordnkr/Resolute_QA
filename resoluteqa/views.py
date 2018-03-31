from django.core import serializers
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import get_object_or_404, render
from .models import Environment, Project, Suite, ProjectEnvironment, SuiteRun, Bug, TestResult, Error

def index(request):
    project_list = Project.objects.all()
    context = {'project_list': project_list}
    return render(request, 'resoluteqa/index.html', context)

def summary(request, projenv_id):
    projectenvironment = get_object_or_404(ProjectEnvironment, pk=projenv_id)
    suite_list = Suite.objects.filter(project_environment_id=projenv_id).order_by('suite_name')

    passed_tests = 0
    failed_tests = 0
    inconclusive_tests = 0
    ignored_tests = 0
    total_tests = 0

    suite_runs = []
    for suite in suite_list:
        run = SuiteRun.objects.filter(suite_id=suite.id).latest('id')
        passed_tests += run.passed_tests
        failed_tests += run.failed_tests
        inconclusive_tests += run.inconclusive_tests
        ignored_tests += run.ignored_tests
        total_tests += run.total_tests
        suite_runs.append(run)

    pass_percentage = round(100 - (100 * (failed_tests / float(passed_tests))), 2)

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
        'fail_percentage': round(100 - pass_percentage, 2)
    }
    return render(request, 'resoluteqa/summary.html', context)

def dailyresults(request, suite_run_id):
    request_suite_run = get_object_or_404(SuiteRun, pk=suite_run_id)
    request_suite = Suite.objects.get(id=request_suite_run.suite.id)
    suite_list = Suite.objects.filter(project_environment_id=request_suite.project_environment.id).order_by('suite_name')
    suite_runs = SuiteRun.objects.filter(suite__id=request_suite.id).order_by('-insert_date')
    test_results = TestResult.objects.filter(suite_run__id=suite_run_id)
    context = {
        'request_suite_run': request_suite_run,
        'suite': request_suite,
        'suite_list': suite_list,
        'suite_runs': suite_runs,
        'test_results': test_results
    }
    return render(request, 'resoluteqa/dailyresults.html', context)

def bugs(request, projenv_id):
    projectenvironment = get_object_or_404(ProjectEnvironment, pk=projenv_id)
    suite_list = Suite.objects.filter(project_environment_id=projenv_id).order_by('suite_name')

    bug_list = Bug.objects.filter(testbug__test__suite__project_environment_id=projenv_id)

    context = {
        'projectenvironment': projectenvironment,
        'suite_list': suite_list,
        'bug_list': bug_list
    }
    return render(request, 'resoluteqa/bugs.html', context)

def testbugs(request, test_id):
    if request.method == 'GET':
        bug_list = Bug.objects.filter(testbug__test__id=test_id)
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
