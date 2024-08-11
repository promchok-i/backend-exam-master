from django_filters import FilterSet, filters
from apis.models import School, Classroom, Teacher, Student


# code here
class BasePersonFilter(FilterSet):
    school = filters.CharFilter(field_name="classroom__school__name", lookup_expr='icontains')
    grade = filters.CharFilter(field_name="classroom__grade", lookup_expr='icontains')
    room = filters.CharFilter(field_name="classroom__room", lookup_expr='icontains')
    first_name = filters.CharFilter(field_name="first_name", lookup_expr='icontains')
    last_name = filters.CharFilter(field_name="last_name", lookup_expr='icontains')
    gender = filters.CharFilter(field_name="gender", lookup_expr='icontains')
    
    class Meta:
        fields = ['school', 'grade', 'room', 'first_name', 'last_name', 'gender']


class SchoolFilter(FilterSet):
    name = filters.CharFilter(field_name="name", lookup_expr='icontains')
    
    class Meta:
        model = School
        fields = ['name']
        
        
class ClassroomFilter(FilterSet):
    school = filters.CharFilter(field_name="school__name", lookup_expr='icontains')
    
    class Meta:
        model = Classroom
        fields = ['school']
        
        
class TeacherFilter(BasePersonFilter):

    class Meta:
        model = Teacher
        fields = BasePersonFilter.Meta.fields

class StudentFilter(BasePersonFilter):

    class Meta:
        model = Student
        fields = BasePersonFilter.Meta.fields
