# Generated by Django 2.0 on 2018-02-09 03:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resoluteqa', '0007_testbug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='test',
            name='test_category',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
