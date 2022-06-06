from django.db import models
from multiselectfield import MultiSelectField

from ckeditor.fields import RichTextField


# Create your models here.


JOB_TYPE = [
    ('FULL TIME', 'Full Time'),
    ('PART TIME', 'Part Time'),
    ('INTERNSHIP', 'Internship'),
]

HIRING_PROCESS= [
    ('FACE TO FACE', 'Face to Face'),
    ('WRITTEN', 'Written'),
    ('TELEPHONIC', 'Telephonic'),
    ('GROUP DISCUSSION', 'Group Discussion'),
    ('WALK-IN', 'Walk-In'),
    ]

WORK_FROM = [
    ('WORK FROM HOME','Work From Home')
]


class Post(models.Model):
    job_title = models.CharField(max_length=200)
    company_name = models.CharField(max_length=200)
    job_type = models.CharField(max_length=20, choices=JOB_TYPE)
    qualification = models.CharField(max_length=200)
    job_location = models.CharField(max_length=200)
    monthly_salary = models.CharField(max_length=200)
    hiring_process = MultiSelectField(max_choices=5, choices=HIRING_PROCESS)
    # job_description = models.CharField(max_length=200)
    job_description = RichTextField(blank=True, null=True)
    company_website = models.URLField(max_length=200)
    about_company = models.CharField(max_length=200)
    last_date = models.CharField(max_length=20)
    work_from = MultiSelectField(max_choices=1, choices=WORK_FROM, null=True, blank=True)
    apply_link = models.URLField(max_length=200)


    
   