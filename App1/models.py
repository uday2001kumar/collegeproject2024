from django.db import models

class SigninModel(models.Model):
    email = models.EmailField(primary_key=True)
    username = models.CharField(max_length=20, unique=True, null=False)
    pas = models.CharField(max_length=10)
    cpas = models.CharField(max_length=10)
    def __str__(self):
        return self.email

class Course(models.Model):
    c_id = models.IntegerField(primary_key=True)
    img_course = models.ImageField(upload_to='images/')
    c_title = models.CharField(max_length=100)
    c_name = models.CharField(unique=True, max_length=50, null=False)
    c_branch = models.CharField(null=False, max_length=50)
    c_duration = models.CharField(max_length=10, null=False)
    c_fee = models.DecimalField(max_digits=20, decimal_places=4, null=False)
    hostal = [('Available', 'Available'), ('Unavailable', 'Unavailable')]
    c_hostal = models.CharField(max_length=50, null=False, choices=hostal)
    def __str__(self):
        return self.c_name

#Faculty Models
class Faculty(models.Model):
    fac_id=models.CharField(max_length=1000)
    fac_name=models.CharField(max_length=100)
    fac_dep=models.CharField(max_length=100)
    fac_sub=models.CharField(max_length=100)
    fac_profile=models.ImageField(upload_to="")
    fac_exp=models.DecimalField(max_digits=10,decimal_places=2)
    



'''______________________________________________________________________________________________________________________'''
'''______________________________________________________________________________________________________________________'''
#Student Application
from datetime import datetime

class Student(models.Model):
    s_roll = models.IntegerField(primary_key=True)
    first_name=models.CharField(max_length=50,null=False)
    last_name=models.CharField(max_length=50,null=False)
    photo=models.ImageField(upload_to="media/",null=False)
    course=models.ForeignKey(Course,on_delete=models.CASCADE)
    year=models.IntegerField(null=False,default=0)
    email = models.OneToOneField(SigninModel, on_delete=models.CASCADE)
    mobile=models.IntegerField(unique=True,null=False)
    state=models.CharField(max_length=100,null=False)
    city=models.CharField(max_length=100,null=False)
    address=models.TextField()
    def __int__(self):
        return self.s_roll
class StudentLogin(models.Model):
    s_roll=models.OneToOneField(Student,on_delete=models.CASCADE)
    s_dob = models.DateField()
    def __int__(self):
        return self.s_roll  
    