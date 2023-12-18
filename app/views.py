from django.shortcuts import render
from app.models import *
from django.http import HttpResponse
from django.db.models.functions import Length

# Create your views here.
def index(request):
    QLTO=Topic.objects.all()
    QLTO=Topic.objects.filter(topic_name='kho-kho')
    d={'topic':QLTO}

    return render(request,'index.html',d)

def second(request):
    QLTO=WebPages.objects.all()
    # QLTO=WebPages.objects.all().order_by('name')
    # QLTO=WebPages.objects.all().order_by('-name')
    # QLTO=WebPages.objects.all().order_by(Length('name'))
    # QLTO=WebPages.objects.all().order_by(Length('name').desc())
    # QLTO=WebPages.objects.all()[3:5:]
    # QLTO=WebPages.objects.filter(topic_name='kho-kho')
    QLTO=WebPages.objects.exclude(topic_name='kho-kho')
    
    d={'topic':QLTO}

    return render(request,'second.html',d)

def in_top(request):
    tn=input("enter the topic name ")
    nto=Topic.objects.get_or_create(topic_name=tn)[0]
    nto.save()
    HttpResponse("topick is created Succesfully.....")
    QLTO=Topic.objects.all()
    d={'topic':QLTO}

    return render(request,'index.html',d)
    
def in_web(request):
    tn=input("Enter topic name ")
    n=input("enter player Name ")
    url=input("Enter url ")

    tno=Topic.objects.get(topic_name=tn)
    wo=WebPages.objects.get_or_create(topic_name=tno,name=n,url=url)[0]
    wo.save()
    HttpResponse("webpages create succesfully...")

    QLTO=WebPages.objects.all()
    
    d={'topic':QLTO}

    return render(request,'second.html',d)

def in_acc(request):
    pk=int(input('enter the number '))
    d=input("enter the date ")
    a=input('ente the author name')
    wo=WebPages.objects.get(pk=pk)
    ato=AccessRecord.objects.get_or_create(name=wo,date=d,author=a)[0]
    ato.save()
    return HttpResponse("accessrecord is created.....")