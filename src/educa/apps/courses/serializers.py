from rest_framework import serializers

from educa.apps.courses.models import Subject, Module, Course


class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = ('id','title','slug')

class ModuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Module
        fields = ('order','description','title')

class CourseSerializer(serializers.ModelSerializer):
    modules = ModuleSerializer(read_only=True,many=True)
    subject = SubjectSerializer(read_only=True)
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Course
        fields = ('id','subject','title','slug','owner','overview','modules','created')