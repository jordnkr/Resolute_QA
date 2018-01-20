from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render


def index(request):
    return render(request, 'resoluteqa/index.html')

def summary(request, project_id):
    return render(request, 'resoluteqa/summary.html')

def dailyresults(request, suite_id):
    return render(request, 'resoluteqa/dailyresults.html')

def bugs(request, suite_id):
    return render(request, 'resoluteqa/bugs.html')
