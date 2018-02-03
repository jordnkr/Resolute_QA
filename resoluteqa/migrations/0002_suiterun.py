# Generated by Django 2.0 on 2018-02-03 06:38

from decimal import Decimal
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('resoluteqa', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SuiteRun',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_tests', models.IntegerField(default=0)),
                ('passed_tests', models.IntegerField(default=0)),
                ('failed_tests', models.IntegerField(default=0)),
                ('inconclusive_tests', models.IntegerField(default=0)),
                ('ignored_tests', models.IntegerField(default=0)),
                ('result_precentage', models.DecimalField(decimal_places=2, default=Decimal('0.00'), max_digits=5)),
                ('start_time', models.DateTimeField(auto_now_add=True)),
                ('end_time', models.DateTimeField(auto_now_add=True)),
                ('total_execution_time', models.DecimalField(decimal_places=2, default=Decimal('0.00'), max_digits=10)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('insert_date', models.DateTimeField(auto_now_add=True)),
                ('suite', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='resoluteqa.Suite')),
            ],
        ),
    ]
