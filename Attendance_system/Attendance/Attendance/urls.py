"""Attendance URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from myapp.views import login,admin_view,add_teacher,validate_login,register_teacher,add_student,admin_add_student,view_teacher,view_student,teacher_view,logout,attendance

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^login/',login),
    url(r'^admin_view/',admin_view),
    url(r'^add_teacher/',add_teacher),
    url(r'^validate_login/',validate_login),
    url(r'^register_teacher/',register_teacher),
    url(r'^add_student/',add_student),
    url(r'^admin_add_student/',admin_add_student),
    url(r'^view_teacher/',view_teacher),
    url(r'^view_student/',view_student),
    url(r'^teacher_view/',teacher_view),
    url(r'^logout/',logout),
    url(r'^attendance/',attendance)

]
