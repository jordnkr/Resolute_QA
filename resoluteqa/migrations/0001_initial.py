# Generated by Django 2.0 on 2018-01-31 02:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Environment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('environment_name', models.CharField(max_length=25)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('insert_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_name', models.CharField(max_length=50)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('insert_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='ProjectEnvironment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('environment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='resoluteqa.Environment')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='resoluteqa.Project')),
            ],
        ),
        migrations.CreateModel(
            name='Suite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('suite_name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=200)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('insert_date', models.DateTimeField(auto_now_add=True)),
                ('project_environment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='resoluteqa.ProjectEnvironment')),
            ],
        ),
        migrations.AddField(
            model_name='project',
            name='environments',
            field=models.ManyToManyField(through='resoluteqa.ProjectEnvironment', to='resoluteqa.Environment'),
        ),
    ]
