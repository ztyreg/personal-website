from django.db import models


# Create your models here.

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=400)
    image = models.ImageField(upload_to='portfolio/images')
    priority = models.IntegerField(blank=True)
    url = models.URLField(blank=True)

    def __str__(self):
        return self.title


class CourseProject(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=400)
    image = models.ImageField(upload_to='portfolio/images')
    priority = models.IntegerField(blank=True)
    url = models.URLField(blank=True)

    def __str__(self):
        return self.title
