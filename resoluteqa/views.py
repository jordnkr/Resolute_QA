from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from .models import Environment, Project, Suite, ProjectEnvironment, SuiteRun

def index(request):
    project_list = Project.objects.all()
    context = {'project_list': project_list}
    return render(request, 'resoluteqa/index.html', context)

def summary(request, projenv_id):
    projectenvironment = get_object_or_404(ProjectEnvironment, pk=projenv_id)
    suite_list = Suite.objects.filter(project_environment_id=projenv_id)

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

def dailyresults(request, suite_id):
    suite = get_object_or_404(Suite, pk=suite_id)
    suite_list = Suite.objects.filter(project_environment_id=suite.project_environment.id)
    context = {
        'suite': suite,
        'suite_list': suite_list
    }
    return render(request, 'resoluteqa/dailyresults.html', context)

def bugs(request, projenv_id):
    projectenvironment = get_object_or_404(ProjectEnvironment, pk=projenv_id)
    suite_list = Suite.objects.filter(project_environment_id=projenv_id)
    context = {
        'projectenvironment': projectenvironment,
        'suite_list': suite_list
    }
    return render(request, 'resoluteqa/bugs.html', context)
