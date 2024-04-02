from django.db import models
from django.contrib.auth.models import User
import datetime
from django.utils.translation import gettext_lazy as _

class Student(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=10)
    email_id = models.EmailField()
    doj = models.DateField()
    address = models.CharField(max_length=255, blank=True)
    aadhar_number = models.CharField(max_length=12)
    #photograph = models.ImageField(upload_to='images/')
    father_name = models.CharField(max_length=255)
    date_of_birth = models.DateField()
   
    current_year = datetime.date.today().year
    PASSED_OUT_YEAR_CHOICES = [(year, str(year)) for year in range(2000, current_year + 1)]
    PASSED_OUT_YEAR_CHOICES.insert(0, ('', 'Select Year'))  

    DATE_CHOICES = [(year, str(year)) for year in range(1900, current_year + 1)]
    DATE_CHOICES.insert(0, ('', 'Select Date'))



    STREAM_CHOICES = (
        ('ECE', 'ECE'),
        ('CSE', 'CSE'),
        ('IT', 'IT'),
        ('CIVIL', 'CIVIL'),
        ('MECHANICAL', 'MECHANICAL'),
        ('EEE', 'EEE'),
        ('DS', 'DS'),
        ('other', 'Other'),
    )
    COURSE_TYPE_CHOICES = (
        ('python_full_stack', 'Python Full Stack'),
        ('java_full_stack', 'Java Full Stack'),
        ('testing', 'Testing'),
        ('devops', 'DevOps'),
        ('other', 'Other'),
    )
    GENDER_CHOICES = (
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    )
    BLOOD_GROUP_CHOICES = (
        ('A+', 'A+'),
        ('A-', 'A-'),
        ('B+', 'B+'),
        ('B-', 'B-'),
        ('O+', 'O+'),
        ('O-', 'O-'),
        ('AB+', 'AB+'),
        ('AB-', 'AB-'),
        ('other', 'Other'),
    )
    GRADUATION_TYPE_CHOICES = (
        ('degree', 'Degree'),
        ('b.tech', 'B.Tech'),
        ('mca', 'MCA'),
        ('other', 'Other'),
    )

    stream = models.CharField(max_length=20, choices=STREAM_CHOICES)
    course_type = models.CharField(max_length=20, choices=COURSE_TYPE_CHOICES)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    blood_group = models.CharField(max_length=5, choices=BLOOD_GROUP_CHOICES)
    graduation_type = models.CharField(max_length=20, choices=GRADUATION_TYPE_CHOICES)
    passed_out_year = models.IntegerField(choices=PASSED_OUT_YEAR_CHOICES)

    username = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)

    