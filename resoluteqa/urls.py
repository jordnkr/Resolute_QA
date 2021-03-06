from django.urls import path

from . import views

app_name = 'resoluteqa'
urlpatterns = [
    # ex: /resoluteqa/
    path('', views.index, name='index'),
    path('uploadresults', views.uploadresults, name='uploadresults'),
    # ex: /resoluteqa/project/2/summary
    path('project/<int:projenv_id>/summary', views.summary, name='summary'),
    # ex: /resoluteqa/suiterun/3/dailyresults
    path('suiterun/<int:suite_run_id>/runresults', views.dailyresults, name='dailyresults'),
    # ex: /resoluteqa/suite/3/bugs
    path('project/<int:projenv_id>/bugs', views.bugs, name='bugs'),
    path('project/<int:projenv_id>/upload', views.uploadresults, name='uploadresults'),
    path('test/<int:test_id>/bugs', views.testbugs, name='testbugs'),
    path('project/<int:projenv_id>/allbugs', views.projectbugs, name='projectbugs'),
    path('individualresult/<int:test_result_id>', views.individualresult, name='individualresult'),
    path('bug/create', views.bug_create, name='bug_create'),
    path('bug/<int:bug_id>/update', views.bug_update, name='bug_update'),
    path('bug/<int:bug_id>/delete', views.bug_delete, name='bug_delete'),
    path('bug/add', views.bug_add, name='bug_add'),
    path('bug/<int:bug_id>/remove/<int:test_id>', views.bug_remove, name='bug_remove'),
    path('upload_mstest', views.upload_mstest, name='upload_mstest')
]
