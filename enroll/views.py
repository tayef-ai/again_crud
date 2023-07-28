from django.shortcuts import render
from .models import Student
from .forms import StudentForm
from django.http import HttpResponseRedirect
# Create your views here.

def insertshowview(request):
    query = Student.objects.all()
    if request.method == 'POST':
        fm = StudentForm(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            pw = fm.cleaned_data['password']
            reg = Student(name=nm, email=em, password=pw)
            reg.save()
            fm = StudentForm()
    else:
        fm = StudentForm()
    return render(request, 'home.html', {'form':fm, 'qr': query})

def deleteview(request, id):
    query = Student.objects.get(pk=id)
    query.delete()
    return HttpResponseRedirect('/')

def editview(request, id):
    query = Student.objects.get(pk=id)
    if request.method == 'POST':
        fm = StudentForm(request.POST, instance=query)
        if fm.is_valid():
            fm.save()
            return HttpResponseRedirect('/')
    else:
        fm = StudentForm(instance=query)
    return render(request, 'edit.html', {'form': fm})