from rest_framework import viewsets, response, status

from apis.filters import StudentFilter
from apis.models import Student
from apis.serializers import (StudentSerializer,
                              StudentCreateUpdateSerializer)

    
    
class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    filterset_class = StudentFilter
    
    def get_serializer_class(self):
        if self.action in ['create', 'update', 'partial_update']:
            return StudentCreateUpdateSerializer
        return StudentSerializer
    
    # Override create method to change API response
    def perform_create(self, serializer):
        return serializer.save()
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        instance = self.perform_create(serializer)
        instance_serializer = StudentSerializer(instance)
        return response.Response(instance_serializer.data, status=status.HTTP_201_CREATED)
    
    # Override update method to change API response
    def perform_update(self, serializer):
        return serializer.save()
    
    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        student_instance = self.perform_update(serializer)
        student_instance_serializer = StudentSerializer(student_instance)

        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        return response.Response(student_instance_serializer.data)