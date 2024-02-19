from django.contrib import admin

from educa.apps.courses.models import Subject, Module, Course


# Register your models here.

@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('title','slug','is_public')
    list_filter = ('is_public',)
    prepopulated_fields = {'slug':('title',)}
    list_editable = ['is_public']

class ModuleAdminInLine(admin.StackedInline):
    model = Module
    extra = 2

@admin.register(Course)
class Course(admin.ModelAdmin):
    list_display = ('title','subject','owner','created')
    list_filter = ('created',)
    search_fields = ('title','overview')
    prepopulated_fields = {'slug':('title',)}

    inlines = [ModuleAdminInLine]