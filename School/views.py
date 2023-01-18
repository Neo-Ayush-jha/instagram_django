from django.shortcuts import render,redirect
from .forms import StudentForm
from .models import *
def home(req):
    form = StudentForm(req.POST,req.FILES or None)
    if req.method =="POST":
        form.save()
        return redirect(home)
    return render(req,"index.html",{"form":form,"stu":Student.objects.all()})

def insta(req,id):
    data={}
    data['st']=Student.objects.get(pk=id)
    data['et'] = Student.objects.exclude(pk=id)
    return render(req,"account.html",data)

def deleteStudent(req,id):
    student=Student.objects.get(pk=id)
    student.delete()
    return redirect(home)

def accountHome(req):
    return render(req,"home.html",{"stu":Student.objects.all()})

def editAccount(req,id):
    account=Student.objects.get(pk=id)
    form= StudentForm(req.POST or None , instance=account)
    if req.method=="POST":
        if form.is_valid():
            form.save()
            return redirect(home)
    return render(req,"edit.html",{'form':form})