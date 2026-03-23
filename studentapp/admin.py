from django.contrib import admin
from .models import Student  

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('student_name', 'age', 'email_id', 'date_of_birth', 'enrolled_in')
