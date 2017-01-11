from django.shortcuts import render, get_object_or_404
from django.views.generic import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from .models import Course

from django.views import generic


class CoursesView(generic.ListView):
    template_name = 'courses/index.html'

    def get_queryset(self):
        return Course.objects.all()


class DetailView(generic.DetailView):
    model = Course
    template_name = 'courses/course.html'


class CourseCreate(CreateView):
    model = Course
    fields = ['name', 'teacher', 'length', 'field', 'course_logo']


class CourseUpdate(UpdateView):
    model = Course
    fields = ['name', 'teacher', 'length', 'field', 'course_logo']


class CourseDelete(DeleteView):
    model = Course
    success_url = reverse_lazy('courses:index')


def follow(request):
    all_courses = Course.objects.all()
    context = {'all_courses': all_courses}
    error_msg = 'Could not follow course'
    try:
        followed_course = all_courses.get(pk=request.POST['course'])
        print('Followed course: ' + str(followed_course))
    except (KeyError, Course.DoesNotExist):
        return render(request, 'courses/index.html', context, error_msg)
    else:
        followed_course.is_followed = True
        followed_course.save()
        return render(request, 'courses/index.html', context)


def un_follow(request):
    all_courses = Course.objects.all()
    context = {'all_courses': all_courses}
    print("form post: " + str(request.POST['course']))
    try:
        followed_course = all_courses.get(pk=request.POST['course'])
        print('Unfollowed course: ' + str(followed_course))
    except (KeyError, Course.DoesNotExist):
        return render(request, 'courses/index.html', context)
    else:
        followed_course.is_followed = False
        followed_course.save()
        return render(request, 'courses/index.html', context)
