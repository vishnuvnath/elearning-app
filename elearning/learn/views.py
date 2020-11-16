
from tkinter import *
from tkinter import messagebox
from django.shortcuts import render,redirect
import datetime
import requests
from django.http import HttpResponse, HttpResponseRedirect
from . models import *
from bs4 import BeautifulSoup
from django.contrib import messages
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.models import User, auth


def index(request):
    return render(request,'index1.html')

def add_blog(request):
    return render(request,'add_blog.html')

def view_blog(request):
    return render(request,'display_blog.html')

def contact(request):
    return render(request,'contact.html')

def course_single(request):
    return render(request,'course_single.html')

def news(request):
    page =requests.get('https://www.indiatoday.in/education-today')
    soup = BeautifulSoup(page.content,'html.parser')
    week = soup.find(class_ = 'special-top-news')
    wm = week.find(class_ = 'itg-listing')
    w = wm.find_all('a')
    ww = []
    for x in w:
        ww.append(x.get_text())
    x = datetime.datetime.now()
    return render(request,'news.html',{'ww':ww,'x':x})


def about(request):
    df = Registration.objects.get(User_role = 'admin')
    gt = Registration.objects.filter(User_role = 'teacher')
    return render(request,'about.html',{'df':df,'gt':gt})

def registration(request):
    pass

def sec_reg(request):
    request.session['email'] = request.POST.get('email')
    psw = request.POST.get('psw')
    rpsw = request.POST.get('rpsw')
    category = request.POST.get('category')
    if psw != rpsw:
        messages.success(request, 'passwords are not matching')
        return render(request, 'index1.html')
    lk = Registration.objects.all()
    for t in lk:
        if (t.User_role == 'admin') and (category == 'admin'):
            messages.info(request, 'you are not allowed to be registered as admin')
            return render(request, 'index1.html')
    request.session['password'] = psw
    request.session['category'] = category
    if category == 'admin':
        return render(request, 'reg_admin.html')
    if category == 'teacher':
        return render(request, 'reg_teacher.html')
    if category == 'student':
        return render(request, 'reg_student.html')

def admin_reg(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        photo = request.FILES['photo']
        pic = FileSystemStorage()
        pic.save(photo.name, photo)
        email = request.POST.get('email')
        username = request.POST.get('username')
        psw = request.POST.get('password')
        c = User.objects.all()
        for i in c:
            if i.username == username:
                messages.info(request, 'Username already exists. Please try another')
                return render(request, 'index1.html')

        user = User.objects.create_user(username = username, password = psw, email = email, first_name = first_name, last_name = last_name)
        user.save()
        x = datetime.datetime.now()
        y = x.strftime("%Y-%m-%d")
        a = Registration()
        a.Registration_date = y
        a.Email = email
        a.Password = psw
        a.User_role = 'admin'
        a.Num_of_enrolled_students = 0
        a.Average_review_rating = 0
        a.Num_of_reviews = 0
        a.First_name = first_name
        a.Last_name = last_name
        a.Image = photo
        a.Qualification = 'Nil'
        a.Introduction_brief = 'Nil'
        a.About_website = 'Nil'
        a.user = user
        a.save()
        messages.success(request,'You have successfully registered as admin')
        return render(request,'index1.html')
    else :
        return render(request,'reg_admin.html')


def login(request):
    if request.method == 'POST':
        uss = request.POST.get('uss')
        try:
            User.objects.get(username = uss)
        except:
            messages.info(request,'Invalid credentials')
            return render(request,'login.html')
        g = User.objects.get(username = uss)
        c = Registration.objects.filter(user = g)
        for i in c:
            if i.User_role == 'admin':
                return render(request, 'adminhome.html',{'c':c})
            if i.User_role == 'teacher':
                return render(request, 'teacherhome.html',{'c':c})
            if i.User_role == 'student':
                return render(request, 'studenthome.html',{'c':c})
            else:
                messages.info(request, 'Your account to the website is blocked')
                return render(request,'login.html')
    else:
        return render(request,'login.html')


def login1(request):
    if request.method == 'POST':
        uss = request.method == 'uss'

def adminhome(request):
    return render(request, 'adminhome.html')


def teacher_reg(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        qualification = request.POST.get('qualification')
        Introduction_brief= request.POST.get('Introduction_brief')
        Num_of_enrolled_students = request.POST.get('enroll')
        photo = request.FILES['photo']
        pic = FileSystemStorage()
        pic.save(photo.name, photo)
        email = request.POST.get('email')
        psw = request.POST.get('psw')
        c = User.objects.all()
        for i in c:
            if i.username == username:
                messages.info(request, 'Username already exists. Please try another')
                return render(request, 'index1.html')

        b = User()
        b.username = username
        b.first_name = first_name
        b.last_name = last_name
        b.password = psw
        b.email = email
        b.save()
        x = datetime.datetime.now()
        y = x.strftime("%Y-%m-%d")
        a = Registration()
        a.Registration_date = y
        a.Email = email
        a.Password = psw
        a.User_role = 'teacher'
        a.Num_of_enrolled_students = Num_of_enrolled_students
        a.Average_review_rating = 0
        a.Num_of_reviews = 0
        a.First_name = first_name
        a.Last_name = last_name
        a.Image = photo
        a.Qualification = qualification
        a.Introduction_brief = Introduction_brief
        a.About_website = 'Nil'
        a.user = b
        a.save()
        messages.success(request,'You have successfully registered as teacher')
        return render(request,'index1.html')
    else :
        return render(request,'reg_teacher.html')


def student_reg(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        photo = request.FILES['photo']
        pic = FileSystemStorage()
        pic.save(photo.name, photo)
        email = request.POST.get('email')
        psw = request.POST.get('password')
        c = User.objects.all()
        for i in c:
            if i.username == username:
                messages.info(request, 'Username already exists. Please try another')
                return render(request, 'index1.html')
        b = User()
        b.username = username
        b.first_name = first_name
        b.last_name = last_name
        b.password = psw
        b.email = email
        b.save()
        x = datetime.datetime.now()
        y = x.strftime("%Y-%m-%d")
        a = Registration()
        a.Registration_date = y
        a.Email = email
        a.Password = psw
        a.User_role = 'student'
        a.Num_of_enrolled_students = 0
        a.Average_review_rating = 0
        a.Num_of_reviews = 0
        a.First_name = first_name
        a.Last_name = last_name
        a.Image = photo
        a.Qualification = 'Nil'
        a.Introduction_brief = 'Nil'
        a.About_website = 'Nil'
        a.user = b
        a.save()
        messages.success(request,'You have successfully registered as student')
        return render(request,'index1.html')
    else:
        return render(request, 'reg_student.html')


def admin(request):
    return render(request,'admin.html')

def add_blog(request):
    if request.method == 'POST':
        nam = request.POST.get('nam')
        c_b = request.POST.get('c_b')
        photo = request.FILES['photo']
        fs = FileSystemStorage()
        fs.save(photo.name, photo)
        date1 = request.POST.get('date1')
        b = Blogs()
        b.Name = nam
        b.Blog_content = c_b
        b.Image = photo
        b.Date_blog = date1
        b.Approval_status = 'Rejected'
        b.save()
        messages.success(request, 'Blog added successfully. Please wait for approval')
        return render(request, 'index1.html')
    return render(request,'add_blog.html')


def view_blog(request):
    dc = Blogs.objects.filter(Approval_status = 'Approved')
    return render(request,'view_blog.html',{'dc':dc})

def update_prof(request):
    gtt = Registration.objects.filter(User_role = 'admin')
    return render(request, 'update_prof.html',{'gtt':gtt})

def adm_prof(request):
    gtt = Registration.objects.filter(User_role = 'admin')
    return render(request, 'adm_prof.html',{'gtt':gtt})

def del_admin(request, id):
    Registration.objects.get(id = id).delete()
    messages.success(request, 'You have successfully resigned from administration')
    return render(request, 'index1.html')

def edit_admin(request):
    bb1 = Registration.objects.get(User_role = 'admin')
    return render(request, 'update_admin.html',{'bb1':bb1})


def bnb(request):
    if request.method == 'POST':
        first = request.POST.get('first')
        last = request.POST.get('last')

def blogs_admin(request):
    dm = Blogs.objects.all()
    return render(request,'blogs_admin.html',{'dm':dm})



def blog_approves(request,id):
    sas = Blogs.objects.get(id=id)
    sas.Approval_status = 'Approved'
    sas.save()
    dm = Blogs.objects.all()
    return render(request, 'blogs_admin.html', {'dm': dm})

def blog_rejects(request, id):
    sas = Blogs.objects.get(id=id)
    sas.Approval_status = 'Rejected'
    sas.save()
    dm = Blogs.objects.all()
    return render(request, 'blogs_admin.html', {'dm': dm})

def blog_delete(request, id):
    Blogs.objects.get(id=id).delete()
    dm = Blogs.objects.all()
    return render(request, 'blogs_admin.html', {'dm': dm})

def upload_cert(request):
    return render(request,'upload_cert.html')

def delete_cert(request):
    return render(request,'delete_cert.html')

def about_content(request):
    return render(request,'about_content.html')

def block(request):
    return render(request,'block.html')

def feedbak(request):
    return render(request,'feedbak.html')

def pass_req(request):
    return render(request,'pass_req.html')

def member_messages(request):
    return render(request,'messages.html')

def guest_messages(request):
    return render(request,'guest_message.html')

def subject_ad(request):
    return render(request,'sub_ad.html')

def chapter_ad(request):
    return render(request,'chapter_ad.html')

def cont_ad(request):
    return render(request,'cont_ad.html')

def logout(request):
    return render(request,'logout')






