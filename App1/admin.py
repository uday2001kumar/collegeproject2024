from django.contrib import admin
from .models import SigninModel,Course,StudentLogin,Faculty,Student
# Register your models here.
class SigninAdminModel(admin.ModelAdmin):
    list_display=['email','username','pas','cpas']
admin.site.register(SigninModel,SigninAdminModel)
class CourseAdmin(admin.ModelAdmin):
    list_display=['c_id','c_name','c_branch','c_duration','c_fee']
admin.site.register(Course,CourseAdmin)

class FacultyAdmin(admin.ModelAdmin):
    list_display=['fac_id','fac_name','fac_dep','fac_sub','fac_profile','fac_exp']
admin.site.register(Faculty,FacultyAdmin)

# #Student App
class StudentLoginAdmin(admin.ModelAdmin):
    list_display=['s_roll','s_dob']
admin.site.register(StudentLogin,StudentLoginAdmin)

class StudentAdmin(admin.ModelAdmin):
    list_display=['s_roll','first_name','last_name','year','photo','course','email','mobile',
    'state','city','address']
admin.site.register(Student,StudentAdmin)
