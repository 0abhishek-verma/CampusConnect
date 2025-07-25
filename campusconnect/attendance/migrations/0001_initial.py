# Generated by Django 5.2.4 on 2025-07-19 05:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core', '0001_initial'),
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('status', models.CharField(choices=[('present', 'Present'), ('absent', 'Absent')], max_length=50)),
                ('Subjects', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.subjects')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='students.studentprofile')),
            ],
        ),
    ]
