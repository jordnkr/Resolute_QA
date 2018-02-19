from django.urls import path

from . import views

app_name = 'resoluteqa'
urlpatterns = [
    # ex: /resoluteqa/
    path('', views.index, name='index'),
    # ex: /resoluteqa/project/2/summary
    path('project/<int:projenv_id>/summary', views.summary, name='summary'),
    # ex: /resoluteqa/suiterun/3/dailyresults
    path('suiterun/<int:suite_run_id>/dailyresults', views.dailyresults, name='dailyresults'),
    # ex: /resoluteqa/suite/3/bugs
    path('project/<int:projenv_id>/bugs', views.bugs, name='bugs'),
    path('individualresult/<int:test_result_id>', views.individualresult, name="individualresult")
]
