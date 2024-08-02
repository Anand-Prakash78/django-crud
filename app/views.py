from django.shortcuts import render,redirect
from django.http import HttpResponse,request
from django.template import loader
from .models import *
from django.core.mail import send_mail
import random
from django.conf import settings
# Create your views here.
def app(request):
    temp=loader.get_template('index.html')
    # return HttpResponse(temp.render())
    return redirect(showNews)
    
def insertpage(request):
    return render(request,'insertpage.html')

def insert(request):
    first=request.POST['fname']
    last=request.POST['lname']
    Course=request.POST['course']
    Number=request.POST['number']
    Email=request.POST['email']
    
    Student.objects.create(fname=first,lname=last,course=Course,mob=Number,email=Email)
    return redirect(showpage)
def showpage(request):
    all_data=Student.objects.all()
    return render(request,'show.html',{'key1':all_data})

def editpage(request,pk):
    data=Student.objects.get(id=pk)
    return render(request,'editpage.html',{'key2':data})


def deletedata(request,pk):
    get_data=Student.objects.get(id=pk)
    get_data.delete()
    return redirect(showpage)

def update(request,pk):
    uname=Student.objects.get(id=pk)
    uname.fname=request.POST['fname']
    uname.lname=request.POST['lname']
    uname.course=request.POST['course']
    uname.mob=request.POST['number']
    uname.email=request.POST['email']
    uname.save()
    return redirect(showpage)

def insertNewsPage(request):    
    return render(request, 'insertNews.html',)

def inserNews(request):
    if request.method=='POST':
        n_title=request.POST['ntitle']
        n_date=request.POST['ndate']
        n_desc=request.POST['desc']
        n_image=request.FILES['image']
        News.objects.create(news_title=n_title,new_date=n_date,news_description=n_desc,news_image=n_image)
    
    return redirect(showNews)

def showNews(request):
    show=News.objects.all()
    return render(request,'showNews.html',{'key1':show})

def descriptionNews(request,title):
    data=News.objects.filter(news_title=title)
    return render(request,'descriptionNews.html',{'key1':data})

def sendOtp(request):
    
    send_mail(
        "This is Testing Mail",
        "Dear Customer Your verification code is " +str(int(random.randrange(100000,999999))) + " . Please Don't share this otp to any one ",
        settings.EMAIL_HOST_USER,
        ["anandprakash783057@gmail.com"],
        fail_silently=False,
    )
    return HttpResponse("OTP send SucessFully")
        
