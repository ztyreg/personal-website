from django.contrib import admin
from .models import Project
from .models import CourseProject

admin.site.register(Project)
admin.site.register(CourseProject)

