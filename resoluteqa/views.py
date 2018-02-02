from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from .models import Environment, Project, Suite

def index(request):
    project_list = Project.objects.all()
    context = {'project_list': project_list}
    return render(request, 'resoluteqa/index.html', context)

def summary(request, project_id):
    return render(request, 'resoluteqa/summary.html')

def dailyresults(request, suite_id):
    return render(request, 'resoluteqa/dailyresults.html')

def bugs(request, suite_id):
    return render(request, 'resoluteqa/bugs.html')
