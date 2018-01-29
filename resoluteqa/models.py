from django.db import models

# Create your models here.
class Environment(models.Model):
    environment_name = models.CharField(max_length=25)
    updated_on = models.DateTimeField(auto_now=True)
    insert_date = models.DateTimeField(auto_now_add=True)
