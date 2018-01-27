from django.urls import path

from . import views

app_name = 'resoluteqa'
urlpatterns = [
    # ex: /resoluteqa/
    path('', views.index, name='index'),
    # ex: /resoluteqa/project/2/summary
    path('project/<int:project_id>/summary', views.summary, name='summary'),
    # ex: /resoluteqa/suite/3/dailyresults
    path('suite/<int:suite_id>/dailyresults', views.dailyresults, name='dailyresults'),
    # ex: /resoluteqa/suite/3/bugs
    path('suite/<int:suite_id>/bugs', views.bugs, name='bugs'),
]
