from django.shortcuts import redirect, render
from django.http import *
from .models import students


# Create your views here.

def home(request):
    obj=students.objects.all()
    if request.method == 'POST':
        name = request.POST['name']
        age = request.POST['age']
        salary = request.POST['salary']
        city = request.POST['city']

        ob=students()
    
        ob.name = name
        ob.age = age
        ob.salary = salary
        ob.city = city
        ob.save()
        return redirect('/',)
    return render(request,'home.html',{'obj':obj})



def update(request):
    if request.method == 'POST':
        id=request.POST['id']
        obj=students.objects.get(id=id)
        return render(request,'update.html',{'obj':obj})
    
    return render(request,'update.html')


def updated(request):
    if request.method == 'POST':

        id=request.POST['id']
        name=request.POST['name']
        age=request.POST['age']
        salary=request.POST['salary']
        city=request.POST['city']
        ob = students()
        obj=students.objects.get(id=id)
                                                                                                                                                                                                                     
        obj.name=name
        obj.age=age
        obj.salary=salary
        obj.city=city
        obj.save()


        return redirect('/')



def delete(request):
    if request.method =='POST':
        id = request.POST['id']
        obj = students.objects.get(id=id)
        obj.delete()
        return redirect('/')


    return render(request,'delete.html')

    