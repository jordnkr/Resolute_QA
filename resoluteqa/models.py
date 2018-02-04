from django.db import models
from decimal import Decimal

# Create your models here.
class Environment(models.Model):
    environment_name = models.CharField(max_length=25)
    updated_on = models.DateTimeField(auto_now=True)
    insert_date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.environment_name

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
    start_time = models.DateTimeField(auto_now_add=True)
    end_time = models.DateTimeField(auto_now_add=True)
    total_execution_time = models.DecimalField(max_digits=10,decimal_places=2,default=Decimal('0.00'))
    updated_on = models.DateTimeField(auto_now=True)
    insert_date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.suite.suite_name + ' ' + str(self.insert_date)
