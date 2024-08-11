from django.contrib import admin
from .models import School, Classroom, Teacher, Student

# Register your models here.
admin.site.register(School)
admin.site.register(Classroom)
admin.site.register(Teacher)
admin.site.register(Student)