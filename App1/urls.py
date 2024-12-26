from django.urls import path
from .views import *

urlpatterns = [
    path('', IndexView.as_view(), name='indexview'),
    path('signinview', SigninView.as_view(), name='signinview'),
    path('signin', Signin.as_view(), name='signin'),
    path('loginview', LoginView.as_view(), name='loginview'),
    path('login', Login.as_view(), name='login'),
    path('forgetview', ForgetView.as_view(), name='forgetview'),
    path('forget',Forget.as_view(),name='forget'),  
    path('home', Home.as_view(), name='home'),
    path('courseview',CourseView.as_view(),name='courseview'),
    path('faculty',FacultyView.as_view(),name='faculty'),
    path('about',About.as_view(),name='about'),

    # Student urls
    path('sloginview',StudentLoginView.as_view(),name='sloginview'),
    path('slv2',StudentLoginV2.as_view(),name='slv2'),
    path('shome',Shome.as_view(),name='shome'),
    path('timet',Timetable.as_view(),name='timet'),
    path('library',Library.as_view(),name='lb'),
    path('exam',ExamResult.as_view(),name='er'),
]

from django.conf.urls.static import static
from django.conf import settings
urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)