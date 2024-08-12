from apis.serializers import TeacherCreateUpdateSerializer, StudentCreateUpdateSerializer
from .base import BaseTestCase

class TeacherSerializerTestCase(BaseTestCase):

    def test_valid_serializer(self):
        """
        Test that the serializer validates correctly with valid data.
        """
        data = {
            'first_name': 'Alice',
            'last_name': 'Clark',
            'gender': 'F',
            'school': self.school_1.id,
            'classroom': [self.classroom_1.id]
        }
        serializer = TeacherCreateUpdateSerializer(data=data)
        self.assertTrue(serializer.is_valid())
        self.assertEqual(serializer.validated_data['first_name'], 'Alice')
        self.assertEqual(serializer.validated_data['last_name'], 'Clark')

    def test_invalid_serializer_different_school(self):
        """
        Test that the serializer raises a validation error when school id and classroom school id are not the same.
        """
        data = {
            'first_name': 'Alice',
            'last_name': 'Clark',  
            'gender': 'F',
            'school': self.school_1.id,
            'classroom': [self.classroom_4.id] # This should trigger a validation error
        }
        serializer = TeacherCreateUpdateSerializer(data=data)
        self.assertFalse(serializer.is_valid())
        self.assertIn('non_field_errors', serializer.errors)
        self.assertEqual(
            serializer.errors['non_field_errors'][0],
            "Classrooms must belong to the teacher's school."
        )
        
        
        
class StudentSerializerTestCase(BaseTestCase):

    def test_valid_serializer(self):
        """
        Test that the serializer validates correctly with valid data.
        """
        data = {
            'first_name': 'Alice',
            'last_name': 'Clark',
            'gender': 'F',
            'school': self.school_1.id,
            'classroom': self.classroom_1.id
        }
        serializer = StudentCreateUpdateSerializer(data=data)
        self.assertTrue(serializer.is_valid())
        self.assertEqual(serializer.validated_data['first_name'], 'Alice')
        self.assertEqual(serializer.validated_data['last_name'], 'Clark')

    def test_invalid_serializer_different_school(self):
        """
        Test that the serializer raises a validation error when school id and classroom school id are not the same.
        """
        data = {
            'first_name': 'Alice',
            'last_name': 'Clark',  
            'gender': 'M',
            'school': self.school_1.id,
            'classroom': self.classroom_4.id # This should trigger a validation error
        }
        serializer = StudentCreateUpdateSerializer(data=data)
        self.assertFalse(serializer.is_valid())
        self.assertIn('non_field_errors', serializer.errors)
        self.assertEqual(
            serializer.errors['non_field_errors'][0],
            "Classrooms must belong to the student's school."
        )
