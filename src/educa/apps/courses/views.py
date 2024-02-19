from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

from educa.apps.courses.models import Subject, Course
from educa.apps.courses.serializers import SubjectSerializer, CourseSerializer


# Create your views here.

class SubjectViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Subject.objects.filter(is_public=True)
    serializer_class = SubjectSerializer

class CourseViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Course.objects.all().select_related('owner','subject')
    serializer_class = CourseSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]
