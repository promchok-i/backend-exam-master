from django.urls import reverse
from rest_framework import status

from apis.models import School, Classroom, Teacher, Student
from .base import BaseTestCase



class SchoolAPITestCase(BaseTestCase):
        
    def test_create_school(self):
        school_count_before = School.objects.count()
        url = reverse('school-list')
        data = {"name": "Third School", "abbrevation": "TS", "address": "5678 Bangkok, Thailand"}
        response = self.client.post(url, data, format='json')
        
        new_school = School.objects.last()
        school_count_after = School.objects.count()
        
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['name'], new_school.name)
        self.assertEqual(school_count_after, school_count_before + 1)
    
    
    def test_get_list_school(self):
        url = reverse('school-list')
        response = self.client.get(url, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['name'], self.school_1.name)
        
        
    def test_get_detail_school(self):
        url = reverse('school-detail', args=[self.school_1.id])
        response = self.client.get(url, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['classrooms_count'], 2)
        self.assertEqual(response.data['teachers_count'], 1)
        self.assertEqual(response.data['students_count'], 3)
        
        
    def test_update_school(self):
        url = reverse('school-detail', args=[self.school_2.id])
        data = {"name": "Second School (Updated)", "abbrevation": "TSU"}
        response = self.client.patch(url, data, format='json')
        
        # Fetch the updated school from the database
        self.school_2.refresh_from_db()
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(self.school_2.name, data['name'])
        self.assertEqual(self.school_2.abbrevation, data['abbrevation'])
        
        
    def test_delete_school(self):
        school_count_before = School.objects.count()
        url = reverse('school-detail', args=[self.school_2.id])
        response = self.client.delete(url, format='json')
        
        school_count_after = School.objects.count()
        
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(school_count_after, school_count_before - 1)
        
        
        
class ClassroomAPITestCase(BaseTestCase):

    def test_create_classroom(self):
        classroom_count_before = Classroom.objects.count()
        url = reverse('classroom-list')
        data = {"grade": "G8", "room": "8", "school": self.school_2.id}
        response = self.client.post(url, data, format='json')
        
        new_classroom = Classroom.objects.last()
        classroom_count_after = Classroom.objects.count()
        
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['grade'], new_classroom.get_grade_display())
        self.assertEqual(response.data['room'], new_classroom.room)
        self.assertEqual(response.data['school'], new_classroom.school.name)
        self.assertEqual(classroom_count_after, classroom_count_before + 1)
    
    
    def test_get_list_classroom(self):
        url = reverse('classroom-list')
        response = self.client.get(url, format='json')
        classroom_count = Classroom.objects.count()
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), classroom_count)
        
        
    def test_get_detail_classroom(self):
        url = reverse('classroom-detail', args=[self.classroom_1.id])
        response = self.client.get(url, format='json')
        
        teachers_count = self.classroom_1.teachers.count()
        students_count = self.classroom_1.students.count()

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['teachers']), teachers_count)
        self.assertEqual(len(response.data['students']), students_count)
        
        
    def test_update_classroom(self):
        url = reverse('classroom-detail', args=[self.classroom_2.id])
        data = {"room": "3", "school": self.school_2.id}
        response = self.client.patch(url, data, format='json')
        
        # Fetch the updated school from the database
        self.classroom_2.refresh_from_db()
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(self.classroom_2.room, data['room'])
        

    def test_delete_classroom(self):
        classroom_count_before = Classroom.objects.count()
        url = reverse('classroom-detail', args=[self.classroom_2.id])
        response = self.client.delete(url, format='json')
        
        classroom_count_after = Classroom.objects.count()
        
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(classroom_count_after, classroom_count_before - 1)
        
        
        
class TeacherAPITestCase(BaseTestCase):

    def test_create_teacher(self):
        teacher_count_before = Teacher.objects.count()
        url = reverse('teacher-list')
        data = {
                "first_name": "Linda",
                "last_name": "Green",
                "gender": "F",
                "school": self.school_2.id,
                "classroom": [self.classroom_3.id, self.classroom_4.id]
            }
        response = self.client.post(url, data, format='json')
        
        new_teacher = Teacher.objects.last()
        teacher_count_after = Teacher.objects.count()
        classroom_teacher_count = new_teacher.classroom.all().count()
        
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(len(response.data['classroom']), classroom_teacher_count)
        self.assertEqual(response.data['school'], new_teacher.school.name)
        self.assertEqual(teacher_count_after, teacher_count_before + 1)
    
    
    def test_get_list_teacher(self):
        url = reverse('teacher-list')
        response = self.client.get(url, format='json')
        
        teacher_count = Teacher.objects.count()
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), teacher_count)
        
        
    def test_get_detail_teacher(self):
        url = reverse('teacher-detail', args=[self.teacher_1.id])
        response = self.client.get(url, format='json')
        
        classrooms_count = self.teacher_1.classroom.count()

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['classroom']), classrooms_count)
        
        
    def test_update_teacher(self):
        url = reverse('teacher-detail', args=[self.teacher_2.id])
        data = {"last_name": "Red", "classroom": [self.classroom_4.id]}
        response = self.client.patch(url, data, format='json')
        
        # Fetch the updated school from the database
        self.teacher_2.refresh_from_db()
        classrooms_count = self.teacher_2.classroom.count()
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['classroom']), classrooms_count)
        

    def test_delete_teacher(self):
        teacher_count_before = Teacher.objects.count()
        url = reverse('teacher-detail', args=[self.teacher_2.id])
        response = self.client.delete(url, format='json')
        
        teacher_count_after = Teacher.objects.count()
        
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(teacher_count_after, teacher_count_before - 1)
        
        
        
class StudentAPITestCase(BaseTestCase):

    def test_create_student(self):
        student_count_before = Student.objects.count()
        url = reverse('student-list')
        data = {
                "first_name": "Linda",
                "last_name": "Green",
                "gender": "F",
                "school": self.school_2.id,
                "classroom": self.classroom_4.id
            }
        response = self.client.post(url, data, format='json')
        
        new_student = Student.objects.last()
        student_count_after = Student.objects.count()
        
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['school'], new_student.school.name)
        self.assertEqual(student_count_after, student_count_before + 1)
    
    
    def test_get_list_student(self):
        url = reverse('student-list')
        response = self.client.get(url, format='json')
        
        student_count = Student.objects.count()
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), student_count)
        
        
    def test_get_detail_student(self):
        url = reverse('student-detail', args=[self.student_1.id])
        response = self.client.get(url, format='json')
        

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['first_name'], self.student_1.first_name)
        self.assertEqual(response.data['classroom'], str(self.student_1.classroom))
        
        
    def test_update_student(self):
        url = reverse('student-detail', args=[self.student_2.id])
        data = {"last_name": "Red", "classroom": self.classroom_1.id, "school": self.school_1.id}
        response = self.client.patch(url, data, format='json')
        
        # Fetch the updated school from the database
        self.student_2.refresh_from_db()
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['last_name'], self.student_2.last_name)
        self.assertEqual(response.data['classroom'], str(self.student_2.classroom))
        

    def test_delete_student(self):
        student_count_before = Student.objects.count()
        url = reverse('student-detail', args=[self.student_2.id])
        response = self.client.delete(url, format='json')
        
        student_count_after = Student.objects.count()
        
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(student_count_after, student_count_before - 1)