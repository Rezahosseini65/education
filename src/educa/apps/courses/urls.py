from rest_framework.routers import SimpleRouter

from educa.apps.courses.views import SubjectViewSet, CourseViewSet

router = SimpleRouter()
router.register('subjects',SubjectViewSet,basename='subject')
router.register('courses',CourseViewSet,basename='course')

urlpatterns = []+router.urls