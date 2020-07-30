from django.shortcuts import render,redirect
from django.conf import settings
from django.contrib.auth.models import User,auth
from .models import contact_table,services_table,index_table,works_table,subservice,works_done
from django.contrib import messages
from django.core.mail import send_mail,EmailMultiAlternatives
from django.template.loader import get_template
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
import math, random 
import os

def index(request):
    data=index_table.objects.all()
    l=[]
    for i in data:
        l.append(i.name)
        l.append(i.designation)
        l.append(i.img)
        l.append(i.description)
    return render(request,'index.html',{'l':l})

def services(request):
    data=services_table.objects.all()
    serv=subservice.objects.all()
    dic={}
    for i in serv:
        if i.service_name in dic:
            dic[i.service_name]+=1
        else:
            dic[i.service_name]=1
    return render(request,'services.html',{'data':data,'serv':serv,'dic':dic})

def works(request):
    data=works_table.objects.all()
    return render(request,'works.html',{'data':data})

def contact(request):
    data=contact_table.objects.all()
    l=[]
    for i in data:
        l.append(i.email)
        l.append(i.phone_number)
        l.append(i.Address)
    return render(request,'contact.html',{'l':l})

def service(request,value):
    data=subservice.objects.filter(service_name=value)
    return render(request,'service.html',{'data':data,'value':value})

def work(request,val):
    images = works_done.objects.filter(work_name=val)
    data = works_table.objects.filter(work_name=val)
    l=[]
    for i in data:
        l.append(i.work_name)
        l.append(i.description)
    return render(request,'work.html',{'images':images,'val':val,'l':l})

def login(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        strin=""
        try:
            user=auth.authenticate(username=username,password=password)
        except:
            strin="Invalid Credentials"
        if user is not None:
            auth.login(request,user)
            return redirect('/admin')
        else:
            strin="Invalid Creadentials"
            return render(request,'login.html',{'strin':strin})
    else:
        return render(request,'login.html')

def logout(request):
    auth.logout(request)
    return render(request,'index.html')