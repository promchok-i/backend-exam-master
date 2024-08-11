from rest_framework.routers import DefaultRouter

from apis.views.v1 import school, teacher, student


router = DefaultRouter(trailing_slash=False)
router.register(r'schools', school.SchoolViewSet)
router.register(r'classrooms', school.ClassroomViewSet)
router.register(r'teachers', teacher.TeacherViewSet)
router.register(r'students', student.StudentViewSet)

urlpatterns = router.urls