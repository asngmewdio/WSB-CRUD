from django.views import View
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Student

class StudentBaseView(View):
    model = Student
    fields = '__all__'
    success_url = reverse_lazy('students:all')

class StudentListView(StudentBaseView, ListView):
    """View to list all students.
    Use the 'student_list' variable in the template
    to access all Student objects"""

class StudentDetailView(StudentBaseView, DetailView):
    """View to list the details from one Student.
    Use the 'Student' variable in the template to access
    the specific Student here and in the Views below"""

class StudentCreateView(StudentBaseView, CreateView):
    """View to create a new student"""

class StudentUpdateView(StudentBaseView, UpdateView):
    """View to update a student"""

class StudentDeleteView(StudentBaseView, DeleteView):
    """View to delete a student"""