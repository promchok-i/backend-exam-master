from rest_framework import viewsets, response, status

from apis.filters import SchoolFilter, ClassroomFilter
from apis.models import School, Classroom
from apis.serializers import (SchoolListSerializer, 
                              SchoolDetailSerializer, 
                              ClassroomListSerializer,
                              ClassroomCreateSerializer, 
                              ClassroomUpdateSerializer, 
                              ClassroomDetailSerializer,
                              ClassroomAfterSaveSerializer)

    
    
class SchoolViewSet(viewsets.ModelViewSet):
    queryset = School.objects.all()
    filterset_class = SchoolFilter

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return SchoolDetailSerializer
        return SchoolListSerializer
    
    
class ClassroomViewSet(viewsets.ModelViewSet):
    queryset = Classroom.objects.all()
    filterset_class = ClassroomFilter
    
    def get_serializer_class(self):
        if self.action == 'retrieve':
            return ClassroomDetailSerializer
        elif self.action == 'create':
            return ClassroomCreateSerializer
        elif self.action in ['update', 'partial_update']:
            return ClassroomUpdateSerializer
        return ClassroomListSerializer
    
    # Override create method to change API response
    def perform_create(self, serializer):
        return serializer.save()
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        instance = self.perform_create(serializer)
        instance_serializer = ClassroomAfterSaveSerializer(instance)
        return response.Response(instance_serializer.data, status=status.HTTP_201_CREATED)
    
    # Override update method to change API response
    def perform_update(self, serializer):
        return serializer.save()
    
    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        classroom_instance = self.perform_update(serializer)
        classroom_instance_serializer = ClassroomAfterSaveSerializer(classroom_instance)

        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        return response.Response(classroom_instance_serializer.data)
