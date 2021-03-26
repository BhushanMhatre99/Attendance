from django.shortcuts import render,redirect,render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.db import connection
from django.contrib.auth import authenticate
from django.contrib import auth
from django.contrib.sessions.models import Session
from django.contrib import messages

# Create your views here.

def login(request):
    return render_to_response("login.html")

def logout(request):
   try:
      del request.session['is_logged']
   except:
      pass
   return render_to_response("login.html")



def admin_view(request):
    logged = 1
    if request.session.has_key('is_logged'):
        return render_to_response("admin_view.html")
    else:
        return render_to_response('login.html', {'logged': logged})

def teacher_view(request):

    if request.session.has_key('is_logged'):
        username = request.session['is_logged']

        cursor = connection.cursor()

        query = "SELECT name FROM user where username = '"+username+"'"
        cursor.execute(query)
        result = cursor.fetchone()[0]

        a = "SELECT name,class_div,id FROM user where class_teacher = '"+result+"' "
        cursor.execute(a)
        res = cursor.fetchall()


        teachers = []
        for teacher in res:
            attendance = {"name" : teacher[0],"class_div" : teacher[1],'id':teacher[2]}
            teachers.append(attendance)

    return render_to_response("teacher_view.html",{'teachers' : teachers})

def add_teacher(request):
    logged = 1
    if request.session.has_key('is_logged'):
        return render_to_response("admin_view.html")
    else:
        return render_to_response("login.html",{'logged' : logged})

def add_student(request):
    cursor = connection.cursor()

    query = "SELECT name,id FROM user WHERE type = 'teacher' "
    cursor.execute(query)
    res = cursor.fetchall()
    teacher_list = []
    for teacher in res:
        teacher_list.append(teacher[0])



    return render_to_response("add_student.html",{'result' : teacher_list})

def view_teacher(request):

    cursor = connection.cursor()


    query = "SELECT name,address,mobile,email,gender,dob FROM user where type = 'teacher' "
    cursor.execute(query)
    res = cursor.fetchall()
    teacher_list = []
    for teacher in res:
        teacher_info = {"name" : teacher[0],"address" : teacher[1],"mobile" : teacher[2],"email" : teacher[3],"gender" : teacher[4],"dob" : teacher[5]}
        teacher_list.append(teacher_info)



    return render_to_response("view_teacher.html",{'teacher_list' : teacher_list})

def view_student(request):

    cursor = connection.cursor()

    query = "SELECT name,address,mobile,email,gender,dob,class_div FROM user where type = 'student' "
    cursor.execute(query)
    res = cursor.fetchall()
    student_list= []
    for student in res:
        student_info = {"name" : student[0],"address" : student[1] , "mobile" : student[2], "email" : student[3], "gender" : student[4] , "dob" : student[5], "class_div" : student[6]}
        student_list.append(student_info)

    return render_to_response("view_student.html",{'student_list' : student_list})



@csrf_exempt
def validate_login(request):

    if request.method =='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        cursor = connection.cursor()
        query = "SELECT * FROM user WHERE username = '" + username + "'"
        cursor.execute(query)
        result = cursor.fetchone()
        login_falied = 1
        if result is None:
            return render_to_response("login.html", {'login_falied': login_falied})
        else:
            if result[2]==username and result[3]==password:
                request.session['is_logged'] = username
                if result[4]=='admin':
                    return HttpResponseRedirect("/admin_view/")
                elif result[4]=='teacher':
                    return HttpResponseRedirect("/teacher_view/")
                elif result[4]=='student':
                    return HttpResponseRedirect("/add_student/")
                else:
                    return render_to_response("login.html",{'login_falied': login_falied})
            else:
                return render_to_response("login.html",{'login_falied': login_falied})

    else:
        return HttpResponseRedirect("/login/")

@csrf_exempt
def register_teacher(request):
    if request.session.has_key('is_logged'):
        if request.method == 'POST':
            name = request.POST.get('name')
            address = request.POST.get('address')
            username = request.POST.get('username')
            password = request.POST.get('password')
            subject = request.POST.get('subject')
            mobile = request.POST.get('mobile')
            dob = request.POST.get('dob')
            gender = request.POST.get('gender')
            email = request.POST.get('email')

            cursor = connection.cursor()

                                        # check for user already exist

            a = "SELECT username from user where username='"+username+"'"
            cursor.execute(a)
            res = cursor.rowcount
            if res == 0:
                                        # insert teacher data in database

                query = "insert into user (name,username,password,subject,mobile,dob,gender,email,type,address) values ('" + name + "' , '" + username + "' , '" + password + "' , '" + subject + "' , '" + mobile + "' , '" + dob + "' , '" + gender + "' , '" + email + "' , 'teacher', '" + email + "')"
                cursor.execute(query)

            else:
                user_already_exist = 1
                return render_to_response('admin_view.html',{'user_already_exist' : user_already_exist})

    registered_successfully = 1
    return render_to_response('admin_view.html',{'registered_successfully' : registered_successfully})



@csrf_exempt
def admin_add_student(request):
    if request.session.has_key('is_logged'):
        if request.method == 'POST':
            name = request.POST.get('name')
            address = request.POST.get('address')
            mobile = request.POST.get('mobile')
            dob = request.POST.get('dob')
            gender = request.POST.get('gender')
            email = request.POST.get('email')
            class_div = request.POST.get('class_div')
            class_teacher = request.POST.get('class_teacher')
            username = request.POST.get('username')
            password = request.POST.get('password')

            cursor = connection.cursor()

            query = "SELECT username from user where username='"+username+"'"
            cursor.execute(query)
            res = cursor.rowcount
            if res == 0:

                sql = "insert into user (name,address,mobile,dob,gender,email,class_div,username,password,class_teacher,type) values ('"+name+"','"+address+"','"+mobile+"','"+dob+"','"+gender+"','"+email+"','"+class_div+"','"+username+"','"+password+"','"+class_teacher+"','student')"
                cursor.execute(sql)

            else:
                user_already_exist = 1
                return HttpResponseRedirect('/add_student/',{'user_already_exist' : user_already_exist})

        registered_successfully = 1
        return render_to_response("add_student.html",{'registered_successfully' : registered_successfully})



def attendance(request):

    if request.method == 'POST':
        name = request.POST.get('present')
        if request.session.has_key('is_logged'):
            username = request.session['is_logged']

            cursor = connection.cursor()

            query = "SELECT name FROM user where username = '" + username + "'"
            cursor.execute(query)
            result = cursor.fetchone()[0]

            a = "SELECT name,class_div,id FROM user where class_teacher = '" + result + "' "
            cursor.execute(a)
            res = cursor.fetchall()

            teachers = []
            for teacher in res:
                attendance = {"name": teacher[0], "class_div": teacher[1], 'id': teacher[2]}
                teachers.append(attendance)

                print(attendance,request.POST.get('present_'+str(teacher[2])))
                sql = "INSERT INTO present(name"
    return render_to_response("teacher_view.html")



