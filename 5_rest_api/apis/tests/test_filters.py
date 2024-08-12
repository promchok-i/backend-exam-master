from apis.filters import SchoolFilter, ClassroomFilter, TeacherFilter, StudentFilter
from .base import BaseTestCase



class FilterTestCase(BaseTestCase):
    
    def test_school_filter(self):
        filter = SchoolFilter(data={'name': 'First'})
        queryset = filter.qs
        self.assertEqual(queryset.count(), 1)
        self.assertIn(self.school_1, queryset)
        self.assertNotIn(self.school_2, queryset)
    
    
    def test_classroom_filter(self):
        filter = ClassroomFilter(data={'school': 'Sec'})
        queryset = filter.qs
        self.assertEqual(queryset.count(), 2)
        self.assertIn(self.classroom_3, queryset)
        self.assertNotIn(self.classroom_1, queryset)
    
    
    def test_teacher_filter(self):
        # Filter with firstname
        filter = TeacherFilter(data={'first_name': 'John'})
        queryset = filter.qs
        self.assertEqual(queryset.count(), 1)
        self.assertIn(self.teacher_1, queryset)
        self.assertNotIn(self.teacher_2, queryset)
        
        # Filter with lastname
        filter = TeacherFilter(data={'last_name': 'Maj'})
        queryset = filter.qs
        self.assertEqual(queryset.count(), 1)
        self.assertIn(self.teacher_2, queryset)
        self.assertNotIn(self.teacher_1, queryset)
        
        # Filter with gender
        filter = TeacherFilter(data={'gender': 'F'})
        queryset = filter.qs
        self.assertEqual(queryset.count(), 1)
        self.assertIn(self.teacher_2, queryset)
        self.assertNotIn(self.teacher_1, queryset)
        
        # Filter with school
        filter = TeacherFilter(data={'school': 'Sec'})
        queryset = filter.qs
        self.assertEqual(queryset.count(), 1)
        self.assertIn(self.teacher_2, queryset)
        self.assertNotIn(self.teacher_1, queryset)
        
        # Filter with classroom
        filter = TeacherFilter(data={'grade': 'K1', 'room': '1'})
        queryset = filter.qs
        self.assertEqual(queryset.count(), 1)
        self.assertIn(self.teacher_1, queryset)
        self.assertNotIn(self.teacher_2, queryset)
        
        # Combined Filter with firstname, lastname, gender, school, classroom
        filter = TeacherFilter(data={
                                'first_name': 'John', 
                                'last_name': 'Do', 
                                'gender': 'M', 
                                'school': 'st', 
                                'grade': 'K1',
                                'room': '1'})
        queryset = filter.qs
        self.assertEqual(queryset.count(), 1)
        self.assertIn(self.teacher_1, queryset)
        self.assertNotIn(self.teacher_2, queryset)
        
        
    def test_student_filter(self):
        # Filter with firstname
        filter = StudentFilter(data={'first_name': 'Ric'})
        queryset = filter.qs
        self.assertEqual(queryset.count(), 1)
        self.assertIn(self.student_1, queryset)
        self.assertNotIn(self.student_2, queryset)
        
        # Filter with lastname
        filter = StudentFilter(data={'last_name': 'joh'})
        queryset = filter.qs
        self.assertEqual(queryset.count(), 1)
        self.assertIn(self.student_2, queryset)
        self.assertNotIn(self.student_1, queryset)
        
        # Filter with gender
        filter = StudentFilter(data={'gender': 'F'})
        queryset = filter.qs
        self.assertEqual(queryset.count(), 2)
        self.assertIn(self.student_2, queryset)
        self.assertNotIn(self.student_1, queryset)
        
        # Filter with school
        filter = StudentFilter(data={'school': 'Sec'})
        queryset = filter.qs
        self.assertEqual(queryset.count(), 2)
        self.assertIn(self.student_4, queryset)
        self.assertNotIn(self.student_1, queryset)
        
        # Filter with classroom
        filter = StudentFilter(data={'grade': 'K1', 'room': '1'})
        queryset = filter.qs
        self.assertEqual(queryset.count(), 2)
        self.assertIn(self.student_1, queryset)
        self.assertNotIn(self.student_4, queryset)
        
        # Combined Filter with firstname, lastname, gender, school, classroom
        filter = StudentFilter(data={
                                'first_name': 'Ric', 
                                'last_name': 'oe', 
                                'gender': 'M', 
                                'school': 'st', 
                                'grade': 'K1',
                                'room': '1'})
        queryset = filter.qs
        self.assertEqual(queryset.count(), 1)
        self.assertIn(self.student_1, queryset)
        self.assertNotIn(self.student_2, queryset)
