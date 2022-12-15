from django.db import models
import datetime
#from django.contrib.auth.models import User

# Create your models here.
GENDER_CHOICES = (
    (0, 'male'),
    (1, 'female'),
    (2, 'not specified'),
)



class patient(models.Model):
    first_name  =models.CharField(max_length=30)
    last_name   =models.CharField(max_length=30)
    class meta:
        db_table="patient"
    def __str__(self):
        return self.first_name


class issue(models.Model):
    patient        =models.ForeignKey('patient' ,on_delete=models.CASCADE,null=True,blank=True)
    issue_name     =models.CharField(max_length=20,null=True, blank=True)
    join_date      =models.DateField(null=True,blank=True)
    Discharge_date =models.DateField(null=True,blank=True)
    


class detail(models.Model):
    patient    =models.ForeignKey('patient' ,on_delete=models.CASCADE,null=True,blank=True)
    gender     =models.IntegerField(choices=GENDER_CHOICES,null=True, blank=True)
    age        =models.PositiveIntegerField(null=True, blank=True)
    email      =models.EmailField(null=True, blank=True)
    mobile_no  =models.CharField(max_length=12,null=True, blank=True)    
    
