from django.shortcuts import render
from .models import Project
from .models import CourseProject


def home(request):
    projects = Project.objects.all().order_by('-priority')
    course_projects = CourseProject.objects.all().order_by('-priority')
    return render(request, 'portfolio/home.html', {'projects': projects, 'course_projects': course_projects})
