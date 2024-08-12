from django.test import TestCase
from rest_framework.test import APITestCase
from django.contrib.auth.models import User

from apis.models import School, Classroom, Teacher, Student


class BaseTestCase(APITestCase):
    
    def setUp(self):
        # Create User to login in API test
        self.user_1 = User.objects.create_user("admin")
        self.client.force_authenticate(user=self.user_1)
        
        # Log out with this code
        # self.client.force_authenticate(user=None)
        
        # Create Schools
        self.school_1 = School.objects.create(name="First School", abbrevation="FS", address="123 Test St")
        self.school_2 = School.objects.create(name="Second School", abbrevation="HS", address="456 Test St")
        
        # Create Classrooms
        self.classroom_1 = Classroom.objects.create(grade="K1", room="1", school=self.school_1)
        self.classroom_2 = Classroom.objects.create(grade="G2", room="2", school=self.school_1)
        self.classroom_3 = Classroom.objects.create(grade="G5", room="5", school=self.school_2)
        self.classroom_4 = Classroom.objects.create(grade="G10", room="10", school=self.school_2)
        
        # Create Teachers
        self.teacher_1 = Teacher.objects.create(first_name="John", last_name="Doe", gender="M", school=self.school_1)
        self.teacher_1.classroom.add(self.classroom_1)
        self.teacher_2 = Teacher.objects.create(first_name="Mary", last_name="Major", gender="F", school=self.school_2)
        self.teacher_2.classroom.add(self.classroom_3, self.classroom_4)
        
        # Create Students
        self.student_1 = Student.objects.create(first_name="Richard", last_name="Roe", gender="M", school=self.school_1, classroom=self.classroom_1)
        self.student_2 = Student.objects.create(first_name="Emily", last_name="Johnson", gender="F", school=self.school_1, classroom=self.classroom_1)
        self.student_3 = Student.objects.create(first_name="David", last_name="Davis", gender="M", school=self.school_1, classroom=self.classroom_2)
        self.student_4 = Student.objects.create(first_name="Sarah", last_name="Miller", gender="F", school=self.school_2, classroom=self.classroom_3)
        self.student_4 = Student.objects.create(first_name="Robert", last_name="Brown", gender="M", school=self.school_2, classroom=self.classroom_4)