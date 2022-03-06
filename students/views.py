from multiprocessing import context
from urllib import request
from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Student
from .forms import StudentModelForm

def home_page(request):
    return HttpResponse("Hello homepage")

def cool_stuff_page(request):
    students = Student.objects.all()
    context= {
        "students": students
    }
    return render(request, "cool_stuff.html", context)

def student_all_page(request):
    students = Student.objects.all()
    context= {
        "students": students
    }
    return render(request, "student_all.html", context)

def student_detail_page(request, pk):
        student = Student.objects.get(id=pk)
        context = {
            "student": student
        }
        return render(request, "student_detail.html", context)

def student_create_page(request):
    form = StudentModelForm()
    if request.method == "POST":
        form = StudentModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/student/all")
    context = {
        "form": form
    }
    return render(request, "student_create.html", context)

def student_update_page(request, pk):
    student = Student.objects.get(id=pk)
    form = StudentModelForm(instance=student)
    if request.method == "POST":
        form = StudentModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/student/all")
    context = {
        "form": form,
        "student": student
    }
    return render(request, "student_update.html", context)