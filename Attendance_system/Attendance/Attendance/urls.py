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
from myapp.views import login,admin_view,add_teacher,validate_login,register_teacher,add_student,admin_add_student,view_teacher,view_student,teacher_view,logout

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^login/',login),
    url('admin_view/',admin_view),
    url('add_teacher/',add_teacher),
    url('validate_login/',validate_login),
    url('register_teacher/',register_teacher),
    url('add_student/',add_student),
    url('admin_add_student',admin_add_student),
    url('view_teacher/',view_teacher),
    url('view_student/',view_student),
    url('teacher_view/',teacher_view),
    url('logout/',logout)

]
