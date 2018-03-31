# Generated by Django 2.0 on 2018-02-04 20:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('resoluteqa', '0005_testresult'),
    ]

    operations = [
        migrations.CreateModel(
            name='Error',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('error_message', models.TextField()),
                ('stack_trace', models.TextField()),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('insert_date', models.DateTimeField(auto_now_add=True)),
                ('test_result', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='resoluteqa.TestResult')),
            ],
        ),
    ]