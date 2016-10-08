from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404
from .models import Course


def index(request):
    all_courses = Course.objects.all()
    context = {'all_courses': all_courses}
    return render(request, 'courses/index.html', context)


def course(request, course_id):
    try:
        course = Course.objects.get(pk=course_id)
    except Course.DoesNotExist:
        raise Http404("No such course with id " + course_id)
    return render(request, 'courses/course.html', {'course': course})
