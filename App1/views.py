from django.shortcuts import render,redirect
from django.views import View
from .models import SigninModel,Course,Faculty
from django.conf import settings
from django.core.mail import send_mail
from django.http import HttpResponse
# Create your views here.
class IndexView(View):
    def get(self,r):
        return render(r,template_name='home/index.html')
class SigninView(View):
    def get(self,r):
        return render(r,template_name='home/signin.html')
class Signin(View):
    def post(self,r):
        email=r.POST.get('email')
        username=r.POST.get('username')
        pas=r.POST.get('password')
        cpas=r.POST.get('confirm-password')
        s1=SigninModel.objects.filter(email=email)
        s1_msg="Email Id Already Exits!"
        s2=SigninModel.objects.filter(username=username)
        s2_msg="Username Already Exits!"
        if s1.exists():
            return render(r,'home/signin.html',{'s1':s1_msg})
        elif s2.exists():
            return render(r,'home/signin.html',{'s2':s2_msg})
        else:
            s3=SigninModel(email=email,username=username,pas=pas,cpas=cpas)
            s3.save()
            s3_msg="Signup Successful!"
            return render(r,'home/login.html',{'s3':s3_msg})
class LoginView(View):
    def get(self,r):
        return render(r,template_name='home/login.html')
class Login(View):
    def post(self, r):
        user = r.POST.get('username')
        password = r.POST.get('password')  
        try:
            user = SigninModel.objects.get(username=user, pas=password)
            return redirect('home')
        except SigninModel.DoesNotExist:
            return render(r, 'home/login.html', {'error': "Invalid email or password"})

class ForgetView(View):
    def get(self,r):
        return render(r,template_name='home/forget.html')
class Forget(View):
    def post(self,r):
        email=r.POST.get('email')
        try:
            s2=SigninModel.objects.get(email=email)
            subject='WELCOME TO OUPG COLLEGE'
            msg=str(s2.pas)
            email_from=settings.DEFAULT_FROM_EMAIL
            recipient_list = [email]
            send_mail(subject, msg, email_from, recipient_list)
            return render(r, 'home/login.html', {'success': "Password has been sent to your email."})
        except SigninModel.DoesNotExist:
            return render(r,'home/forget.html',{'fail': "Enter valid Email"})
class Home(View):
    def get(self,r):
        return render(r,template_name='main/home.html')
    
class CourseView(View):
    def get(self,r):
        c1=Course.objects.all()
        return render(r,'main/course.html',{'c1':c1})

class FacultyView(View):
    def get(self,r):
        f1=Faculty.objects.all()
        return render(r,'main/faculty.html',{'f':f1})
class About(View):
    def get(self,r):
        return render(r,template_name='main/about.html')
'''______________________________________________________________________________________________________________________'''
'''______________________________________________________________________________________________________________________'''
'''______________________________________________________________________________________________________________________'''
'''______________________________________________________________________________________________________________________'''
'''______________________________________________________________________________________________________________________'''

#Student Application
from .models import StudentLogin,Student
class StudentLoginView(View):
    def get(self,r):
        return render(r,template_name='student/login.html')
class StudentLoginV2(View):
    def post(self,r):
        roll=r.POST.get("roll_number")
        dob=r.POST.get("dob")
        s1=StudentLogin.objects.filter(s_roll=roll).exists()
        s2=StudentLogin.objects.filter(s_dob=dob).exists()
        if s1:
            if s2:
                students=StudentLogin.objects.get(s_roll=roll)
                return render(r,'student/shome.html',{'student':students})
            else:
                msg2='Enter Valid DataBirth'
                return render(r,'student/login.html',{'msg2':msg2})
        else:
            msg1='Enter Valid Roll number'
            return render(r,'student/login.html',{'msg1':msg1})
        
class Shome(View):
    def get(self,r):
        return render(r,'student/shome.html')
class Timetable(View):
    def get(self,r):
        return render(r,template_name='student/timetable.html')
class Library(View):
    def get(self,r):
        return render(r,template_name='student/library.html')
class ExamResult(View):
    def get(self,r):
        return render(r,template_name='student/examresult.html')