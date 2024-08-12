from .base import BaseTestCase
from apis.models import School, Classroom, Teacher, Student


class SchoolModelTest(BaseTestCase):
    
    def test_string_representation(self):
        self.assertEqual(str(self.school_1), f'โรงเรียน {self.school_1.name}')

    def test_create_school(self):
        self.assertEqual(School.objects.count(), 2)
        
        
class ClassroomModelTest(BaseTestCase):
    
    def test_string_representation(self):
        self.assertEqual(str(self.classroom_1), 
                         f'โรงเรียน {self.classroom_1.school.name}, ชั้น {self.classroom_1.get_grade_display()}/{self.classroom_1.room}')

    def test_create_classroom(self):
        self.assertEqual(Classroom.objects.count(), 4)
        
        
class TeacherModelTest(BaseTestCase):
    
    def test_string_representation(self):
        self.assertEqual(str(self.teacher_1), 
                         f'ครู {self.teacher_1.first_name} {self.teacher_1.last_name}, โรงเรียน {self.teacher_1.school.name}')

    def test_create_teacher(self):
        self.assertEqual(Teacher.objects.count(), 2)
        
        
class StudentModelTest(BaseTestCase):
    
    def test_string_representation(self):
        self.assertEqual(str(self.student_1), 
                         f'นักเรียน {self.student_1.first_name} {self.student_1.last_name}, โรงเรียน {self.student_1.classroom.school.name}')

    def test_create_student(self):
        self.assertEqual(Student.objects.count(), 5)