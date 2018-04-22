from django.db import models
from decimal import Decimal

# Create your models here.
class Environment(models.Model):
    environment_name = models.CharField(max_length=25)
    updated_on = models.DateTimeField(auto_now=True)
    insert_date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.environment_name

    class Meta:
        ordering = ('environment_name',)

class Project(models.Model):
    environments = models.ManyToManyField(Environment, through='ProjectEnvironment')
    project_name = models.CharField(max_length=50)
    updated_on = models.DateTimeField(auto_now=True)
    insert_date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.project_name

class ProjectEnvironment(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    environment = models.ForeignKey(Environment, on_delete=models.CASCADE)
    def __str__(self):
        return self.project.project_name + ' ' + self.environment.environment_name

class Suite(models.Model):
    project_environment = models.ForeignKey(ProjectEnvironment, on_delete=models.CASCADE)
    suite_name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    updated_on = models.DateTimeField(auto_now=True)
    insert_date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.suite_name

class SuiteRun(models.Model):
    suite = models.ForeignKey(Suite, on_delete=models.CASCADE)
    total_tests = models.IntegerField(default=0)
    passed_tests = models.IntegerField(default=0)
    failed_tests = models.IntegerField(default=0)
    inconclusive_tests = models.IntegerField(default=0)
    ignored_tests = models.IntegerField(default=0)
    result_precentage = models.DecimalField(max_digits=5,decimal_places=2,default=Decimal('0.00'))
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    total_execution_time = models.DecimalField(max_digits=10,decimal_places=2,default=Decimal('0.00'))
    updated_on = models.DateTimeField(auto_now=True)
    insert_date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.suite.suite_name + ' ' + str(self.insert_date)

class Bug(models.Model):
    source_control = models.CharField(max_length=20)
    source_control_id = models.IntegerField(default=0)
    title = models.CharField(max_length=200)
    url = models.CharField(max_length=200)
    updated_on = models.DateTimeField(auto_now=True)
    insert_date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.source_control + ' - ' + str(self.source_control_id)

class Test(models.Model):
    bugs = models.ManyToManyField(Bug)
    suite = models.ForeignKey(Suite, on_delete=models.CASCADE)
    test_name = models.CharField(max_length=50)
    test_category = models.CharField(max_length=50, blank=True)
    class_name = models.CharField(max_length=50)
    namespace = models.CharField(max_length=200)
    updated_on = models.DateTimeField(auto_now=True)
    insert_date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.test_name + ' - ' + str(self.id)

class TestResult(models.Model):
    suite_run = models.ForeignKey(SuiteRun, on_delete=models.CASCADE)
    test = models.ForeignKey(Test, on_delete=models.CASCADE)
    result = models.CharField(max_length=20)
    host = models.CharField(max_length=50)
    start_time = models.DateTimeField(auto_now_add=True)
    end_time = models.DateTimeField(auto_now_add=True)
    total_execution_time = models.DecimalField(max_digits=10,decimal_places=2,default=Decimal('0.00'))
    console_output = models.TextField()
    updated_on = models.DateTimeField(auto_now=True)
    insert_date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.test.test_name + ' - ' + self.suite_run.suite.suite_name + ' - ' + str(self.insert_date)

class Error(models.Model):
    test_result = models.ForeignKey(TestResult, on_delete=models.CASCADE)
    error_message = models.TextField()
    stack_trace = models.TextField()
    updated_on = models.DateTimeField(auto_now=True)
    insert_date = models.DateTimeField(auto_now_add=True)
