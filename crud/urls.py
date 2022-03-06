from django.contrib import admin
from django.urls import path
from students.views import home_page, student_create_page, student_detail_page, student_update_page, student_all_page, cool_stuff_page

urlpatterns = [
    path('', home_page),
    path('admin/', admin.site.urls),
    path('student/all/', student_all_page),
    path('student/<int:pk>/', student_detail_page),
    path('student/create/', student_create_page),
    path('student/<int:pk>/update/', student_update_page),
    path('cool_stuff/', cool_stuff_page),
]
