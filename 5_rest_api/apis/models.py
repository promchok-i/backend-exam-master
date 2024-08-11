from typing import Iterable
from django.db import models
from django.core.exceptions import ValidationError
from django.utils import timezone


# Create your models here.
class BaseModel(models.Model):
    created_at = models.DateTimeField(db_index=True, default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        abstract = True
    
    # Soft delete, flag a record as inactive    
    def delete(self):
        self.is_active = False
        self.save()


class BaseModelManager(models.Manager):
    
    # Handle soft delete to get only active records
    def get_queryset(self):
        return super().get_queryset().filter(is_active=True)
    
        
# Choices for Teacher and Student
GENDER_CHOICES = [
    ('M', 'Male'),
    ('F', 'Female'),
]


class School(BaseModel):
    objects = BaseModelManager()
    
    name = models.CharField(max_length=30)
    abbrevation = models.CharField(max_length=10)
    address = models.TextField()
    
    def __str__(self):
        return f'โรงเรียน {self.name}'
    

class Classroom(BaseModel):
    GRADE_CHOICES = [
        ('K1', 'อนุบาล 1'),      # Kindergarten 1
        ('K2', 'อนุบาล 2'),      # Kindergarten 2
        ('K3', 'อนุบาล 3'),      # Kindergarten 3
        ('G1', 'ประถม 1'),       # Grade 1
        ('G2', 'ประถม 2'),       # Grade 2
        ('G3', 'ประถม 3'),       # Grade 3
        ('G4', 'ประถม 4'),       # Grade 4
        ('G5', 'ประถม 5'),       # Grade 5
        ('G6', 'ประถม 6'),       # Grade 6
        ('G7', 'มัธยม 1'),       # Grade 7
        ('G8', 'มัธยม 2'),       # Grade 8
        ('G9', 'มัธยม 3'),       # Grade 9
        ('G10', 'มัธยม 4'),      # Grade 10
        ('G11', 'มัธยม 5'),      # Grade 11
        ('G12', 'มัธยม 6'),      # Grade 12
    ]
    
    objects = BaseModelManager()
     
    grade = models.CharField(max_length=3, choices=GRADE_CHOICES, default='K1')
    room = models.CharField(max_length=10)
    school = models.ForeignKey(School, on_delete=models.CASCADE, related_name='classrooms')
    
    def __str__(self):
        return f'โรงเรียน {self.school.name}, ชั้น {self.get_grade_display()}/{self.room} '
    
    
class Teacher(BaseModel):
    objects = BaseModelManager()
    
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    school = models.ForeignKey(School, on_delete=models.CASCADE, related_name='teachers')
    classroom = models.ManyToManyField(Classroom, related_name='teachers')
    
    def __str__(self):
        return f'ครู {self.first_name} {self.last_name}, โรงเรียน {self.school.name}'
    
    
class Student(BaseModel):
    objects = BaseModelManager()
    
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    school = models.ForeignKey(School, on_delete=models.CASCADE, related_name='students')
    classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE, related_name='students')
    
    def __str__(self):
        return f'นักเรียน {self.first_name} {self.last_name}, โรงเรียน {self.classroom.school.name}'