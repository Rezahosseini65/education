from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django.template.loader import render_to_string

from educa.apps.courses.fields import OrderField


# Create your models here.

class Subject(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True,allow_unicode=True)
    is_public = models.BooleanField(default=True)

    class Meta:
        ordering = ['title']
        verbose_name = 'Subject'
        verbose_name_plural = 'Subjects'

    def __str__(self):
        return self.title

class Course(models.Model):
    owner = models.ForeignKey('users.User',on_delete=models.CASCADE,
                              related_name='course_created')
    subject = models.ForeignKey(Subject,on_delete=models.CASCADE,related_name='courses')
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True,allow_unicode=True)
    overview = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)

    students = models.ManyToManyField('users.User',related_name='course_joined',blank=True)

    class Meta:
        ordering = ['-created']
        verbose_name = 'Course'
        verbose_name_plural = 'Courses'

    def __str__(self):
        return self.title

class Module(models.Model):
    course = models.ForeignKey(Course,on_delete=models.CASCADE,related_name='modules')
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    order = OrderField(blank=True,for_fields=['course'])

    class Meta:
        ordering = ['order']
        verbose_name = 'Module'
        verbose_name_plural = 'Modules'

    def __str__(self):
        return f'{self.order}.{self.title}'

class Content(models.Model):
    module = models.ForeignKey(Module,on_delete=models.CASCADE,related_name='contents')
    content_type = models.ForeignKey(ContentType,on_delete=models.CASCADE,limit_choices_to={'model__in':(
                                                                                            'text','file','image','video'
                                                                                            )})
    object_id = models.PositiveIntegerField()
    item = GenericForeignKey('content_type','object_id')
    order = OrderField(blank=True,for_fields=['module'])


    class Meta:
        verbose_name = 'Content'
        verbose_name_plural = 'Contents'
        ordering = ['order']

class ItemBase(models.Model):
    owner = models.ForeignKey('users.User',on_delete=models.CASCADE,related_name='%(class)s_related')
    title = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


    class Meta:
        abstract = True

class Text(ItemBase):
    text = models.TextField()

class File(ItemBase):
    file = models.FileField(upload_to='files/')

class Image(ItemBase):
    image = models.ImageField(upload_to='images/')

class Video(ItemBase):
    video = models.URLField()