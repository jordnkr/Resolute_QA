# Generated by Django 2.0 on 2018-02-04 20:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('resoluteqa', '0002_suiterun'),
    ]

    operations = [
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('test_name', models.CharField(max_length=50)),
                ('test_category', models.CharField(max_length=50)),
                ('class_name', models.CharField(max_length=50)),
                ('namespace', models.CharField(max_length=200)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('insert_date', models.DateTimeField(auto_now_add=True)),
                ('suite', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='resoluteqa.Suite')),
            ],
        ),
    ]
