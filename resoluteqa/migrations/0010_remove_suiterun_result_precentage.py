# Generated by Django 2.0 on 2018-03-31 22:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('resoluteqa', '0009_auto_20180208_2220'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='suiterun',
            name='result_precentage',
        ),
    ]
