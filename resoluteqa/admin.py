from django.contrib import admin
from .models import Environment, Project, ProjectEnvironment, Suite, SuiteRun, Test, Bug, TestBug, Error

class ProjectEnvironmentInline(admin.TabularInline):
    model = ProjectEnvironment
    extra = 1

class ProjectAdmin(admin.ModelAdmin):
    inlines = (ProjectEnvironmentInline,)

class EnvironmentAdmin(admin.ModelAdmin):
    inlines = (ProjectEnvironmentInline,)

class TestBugInline(admin.TabularInline):
    model = TestBug
    extra = 1

class TestAdmin(admin.ModelAdmin):
    inlines = (TestBugInline,)

class BugAdmin(admin.ModelAdmin):
    inlines = (TestBugInline,)

# Register your models here.
admin.site.register(Environment, EnvironmentAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Suite)
admin.site.register(SuiteRun)
admin.site.register(Test, TestAdmin)
admin.site.register(Bug, BugAdmin)
admin.site.register(Error)
