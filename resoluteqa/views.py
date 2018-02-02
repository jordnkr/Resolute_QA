from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from .models import Environment, Project, Suite, ProjectEnvironment

def index(request):
    project_list = Project.objects.all()
    context = {'project_list': project_list}
    return render(request, 'resoluteqa/index.html', context)

def summary(request, projenv_id):
    projectenvironment = get_object_or_404(ProjectEnvironment, pk=projenv_id)
    suite_list = Suite.objects.filter(project_environment_id=projenv_id)
    context = {
        'projectenvironment': projectenvironment,
        'suite_list': suite_list
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
