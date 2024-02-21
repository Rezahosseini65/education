from rest_framework import serializers

from educa.apps.courses.models import Subject, Module, Course, Text, File, Image, Video, Content


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

class ItemRelatedField(serializers.RelatedField):
    def to_representation(self, value):
        if isinstance(value,Text):
            return 'Text: ' + value.text
        elif isinstance(value,File):
            return 'File: ' + value.file
        elif isinstance(value,Image):
            return 'Image: ' + value.image
        elif isinstance(value,Video):
            return 'Video: ' + value.video
        raise Exception('Unexpected type of tagged object')

class ContentSerializer(serializers.ModelSerializer):
    item = ItemRelatedField(read_only=True)
    class Meta:
        model = Content
        fields = ('order','item')

class ModuleWithContentsSerializer(serializers.ModelSerializer):
    contents = ContentSerializer(many=True)
    class Meta:
        model = Module
        fields = ('order','title','description','contents')

class CourseWithContentsSerializer(serializers.ModelSerializer):
    modules = ModuleWithContentsSerializer(many=True)
    class Meta:
        model = Course
        fields = ('id', 'subject', 'title', 'slug','overview', 'created', 'owner', 'modules')



