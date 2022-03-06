from django.contrib import admin
from .models import User, Student, Representative

admin.site.register(User)
admin.site.register(Student)
admin.site.register(Representative)