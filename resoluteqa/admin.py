from django.contrib import admin
from .models import Environment, Project, ProjectEnvironment, Suite, SuiteRun, Test, Bug

class ProjectEnvironmentInline(admin.TabularInline):
    model = ProjectEnvironment
    extra = 1

class ProjectAdmin(admin.ModelAdmin):
    inlines = (ProjectEnvironmentInline,)

class EnvironmentAdmin(admin.ModelAdmin):
    inlines = (ProjectEnvironmentInline,)

# Register your models here.
admin.site.register(Environment, EnvironmentAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Suite)
admin.site.register(SuiteRun)
admin.site.register(Test)
admin.site.register(Bug)
