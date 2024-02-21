from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response

from educa.apps.courses.models import Subject, Course
from educa.apps.courses.permissions import IsEnrolled
from educa.apps.courses.serializers import SubjectSerializer, CourseSerializer, CourseWithContentsSerializer


# Create your views here.

class SubjectViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Subject.objects.filter(is_public=True)
    serializer_class = SubjectSerializer

class CourseViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    @action(detail=True,
            methods=['post'],
            authentication_classes=[TokenAuthentication],
            permission_classes=[IsAuthenticated]
            )
    def enroll(self, request, *args, **kwargs):
        course = self.get_object()
        course.students.add(request.user)
        return Response({'enrolled': True})

    @action(detail=True,
            methods=['get'],
            serializer_class=CourseWithContentsSerializer,
            authentication_classes=[TokenAuthentication],
            permission_classes=[IsAuthenticated,IsEnrolled]
            )
    def contents(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
