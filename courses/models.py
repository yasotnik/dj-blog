from django.db import models


class Course(models.Model):
    name = models.CharField(max_length=50)
    teacher = models.CharField(max_length=50)
    length = models.IntegerField()
    field = models.CharField(max_length=150)
    course_logo = models.CharField(max_length=1000)

    def __str__(self):
        return self.name + " by " + self.teacher


class Lecture(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    file_type = models.CharField(max_length=10)
    lecture_name = models.CharField(max_length=100)
    lecture_url = models.URLField(max_length=1000, default='')

    def __str__(self):
        return self.lecture_name
