from django.core.exceptions import ValidationError
from rest_framework import serializers

from apis.models import School, Classroom, Teacher, Student


# code here

# School Serializer
class SchoolListSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = School
        fields = '__all__'
        
class SchoolDetailSerializer(serializers.ModelSerializer):
    classrooms_count = serializers.SerializerMethodField()
    teachers_count = serializers.SerializerMethodField()
    students_count = serializers.SerializerMethodField()

    class Meta:
        model = School
        fields = '__all__'

    def get_classrooms_count(self, obj):
        return obj.classrooms.count()

    def get_teachers_count(self, obj):
        return Teacher.objects.filter(classroom__school=obj).distinct().count()

    def get_students_count(self, obj):
        return Student.objects.filter(classroom__school=obj).count()
    
    
# Teacher Serializer
class TeacherListSerializer(serializers.ModelSerializer):
    gender = serializers.SerializerMethodField()
    classroom = serializers.SerializerMethodField()
    
    class Meta:
        model = Teacher
        fields = '__all__'
        
    def get_gender(self, obj):
        return obj.get_gender_display()
    
    def get_classroom(self, obj):
        return [str(classroom) for classroom in obj.classroom.all()]
        
class TeacherDetailSerializer(serializers.ModelSerializer):
    gender = serializers.SerializerMethodField()
    classroom = serializers.SerializerMethodField()
    school = serializers.CharField(source='school.name')

    class Meta:
        model = Teacher
        fields = '__all__'
        
    def get_gender(self, obj):
        return obj.get_gender_display()

    def get_classroom(self, obj):
        return [str(classroom) for classroom in obj.classroom.all()]
    
class TeacherCreateUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Teacher
        fields = ['first_name', 'last_name', 'gender', 'school', 'classroom']
        

    def validate(self, data):
        school = data.get('school')
        classrooms = data.get('classroom')
        
        if school and classrooms:
            classroom_schools = list(set(classroom.school.id for classroom in classrooms))

            if len(classroom_schools) > 1 or classroom_schools[0] != school.id:
                raise ValidationError("Classrooms must belong to the teacher's school.")

        return data
    
    
    
# Student Serializer
class StudentSerializer(serializers.ModelSerializer):
    gender = serializers.SerializerMethodField()
    classroom = serializers.SerializerMethodField()
    school = serializers.CharField(source='school.name')
    
    class Meta:
        model = Student
        fields = '__all__'
        
    def get_gender(self, obj):
        return obj.get_gender_display()
    
    def get_classroom(self, obj):
        return str(obj.classroom)
    
class StudentCreateUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Student
        fields = ['first_name', 'last_name', 'gender', 'school', 'classroom']
        
    
    def validate(self, data):
        school = data.get('school')
        classroom = data.get('classroom')

        if classroom.school.id != school.id:
            raise ValidationError("Classrooms must belong to the student's school.")

        return data
    
    
# Classroom Serializer
class ClassroomListSerializer(serializers.ModelSerializer):
    grade = serializers.SerializerMethodField()
    school = serializers.CharField(source='school.name')
    
    class Meta:
        model = Classroom
        fields = '__all__'
        
    def get_grade(self, obj):
        return obj.get_grade_display()
        
class ClassroomDetailSerializer(serializers.ModelSerializer):
    teachers = TeacherListSerializer(many=True, read_only=True)
    students = StudentSerializer(many=True, read_only=True)
    grade = serializers.SerializerMethodField()
    school = serializers.CharField(source='school.name')

    class Meta:
        model = Classroom
        fields = '__all__'
        
    def get_grade(self, obj):
        return obj.get_grade_display()
    
class ClassroomCreateUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Classroom
        fields = ['grade', 'room', 'school']
        
    
class ClassroomAfterSaveSerializer(serializers.ModelSerializer):
    grade = serializers.SerializerMethodField()
    school = serializers.CharField(source='school.name')

    class Meta:
        model = Classroom
        fields = '__all__'
        
    def get_grade(self, obj):
        return obj.get_grade_display()